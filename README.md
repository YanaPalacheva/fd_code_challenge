Event crawler for [Lucerne Summer Festival](https://www.lucernefestival.ch/en/program/summer-festival-23)

Crawler implemented with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), data then inserted into a PostgreSQL database.

How to run:

0. Make sure you have Docker installed on your machine.
1. Clone this repository.
2. Open your command-line shell and change directory: `cd your/path/fd_code_challenge`
3*. If you're running this on M1-based Mac: run this command prior to docker-compose build: `export DOCKER_DEFAULT_PLATFORM=linux/amd64`. [Reference](https://github.com/psycopg/psycopg2/issues/1360)
4. Run `docker-compose up --build`

Ta-daam! A table with events should be displayed (if it looks weird, try to resize the window)
