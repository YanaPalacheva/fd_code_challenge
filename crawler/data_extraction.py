"""This file contains methods extracting information from the relevant HTML blobs"""


def get_date_time_location(candidates) -> list:
    """
    Extracts date, time and location from block candidates selected by the BS4's CSS selector.
    :param candidates: ordered matches for date-venue (guaranteed) and program (optional) information
    :return: list of three strings: date (in format "Mon dd.mm."), time (in format HH.MM) and location
    Possible todo: cast date and time to datetime format using postprocessing in pandas
    """
    if candidates and candidates[0].get_text() == 'Date and Venue':
        raw_text = candidates[0].find_next_siblings(string=True)[0]
        date, time, location = [item.strip() for item in raw_text.split('|')]
        time = time.replace('.', ':')
        # avoiding typecasting like 19.30 -> 19.3
        return date, time, location
    else:
        return ['']*3


def get_program(candidates) -> str:
    """
    Extracts event program description if present.
    :param candidates: ordered matches for date-venue (guaranteed) and program (optional) information
    :return: short text describing an event's program (empty string if no information present)
    """
    if len(candidates) > 1 and candidates[1].get_text() == 'Program':
        raw_text = candidates[1].find_next_siblings(string=True)[0]
        return raw_text.strip()
    else:
        return ''


def get_image_link(image_link_section, homepage) -> str:
    """
    Extracting image url.
    :param image_link_section: HTML blob (processed by the BS4) containing all information abour the event pic.
    :param homepage: homepage of the website, needed since all links in the HTML are relevant (not absolute URLs)
    :return: absolute link to the relevant image, '' if no data found.
    """
    image_link = image_link_section.figure.picture.source['srcset']
    if image_link:
        image_link = homepage + image_link
    return image_link
