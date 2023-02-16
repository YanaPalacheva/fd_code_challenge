"""This file describes an Event dataclass, structuring the crawled data"""

from dataclasses import dataclass


@dataclass
class Event:
    title: str
    date: str
    time: str
    location: str
    artists: list
    program: str
    image_link: str

