import requests
from tabulate import tabulate
import os
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, text, Text
import pandas as pd

from event import Event
from data_extraction import *

# env variables for connection
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
db = os.environ['POSTGRES_DB']

table_name = 'events_table'

# data source (url)
homepage = "https://www.lucernefestival.ch"
data_source = "/en/program/summer-festival-23"

soup = BeautifulSoup(requests.get(url=homepage+data_source).content, 'html.parser')
events = []

# iterating over all event sections in the html
for event in soup.select('.event-content'):
    # there's no sensible id or a tag for event titles, so here I use the knowledge that
    # 1) there's always a title tagged as '.body-small' 2) HTML is ordered and it always comes first in a block
    title = event.select_one('.body-small').get_text()
    artists = event.select_one('.event-title').get_text().strip().split(' | ')
    date_program_candidates = event.find_all('strong', string=True)
    date, time, location = get_date_time_location(date_program_candidates)

    event_object = Event(title=title,
                         date=date, time=time, location=location,
                         artists=artists,
                         program=get_program(date_program_candidates),
                         image_link=get_image_link(event.select_one('.event-image-link'), homepage))

    events.append(event_object)

# transforming list of events into pandas' DataFrame for convenience
events_df = pd.DataFrame(events, dtype="string")

# connecting to the PG container vie SQLAlchemy and transforming the DataFrame into a table
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')
events_df.to_sql(table_name, engine, if_exists='replace', dtype=Text)

# displaying the table
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM events_table")).fetchall()
    print(tabulate(result, headers=events_df.columns, tablefmt='grid', maxcolwidths=15))


