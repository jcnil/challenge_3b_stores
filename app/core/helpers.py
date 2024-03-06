from datetime import datetime

import pytz

from app.core.constants import TIMEZONE


def local_now():
    """datetime.datetime.now of local timezone

    Returns:
        datetime.datetime:
    """
    timezone = TIMEZONE
    now = datetime.now(pytz.timezone(
        timezone
    ))
    return datetime(
        year=now.year,
        month=now.month,
        day=now.day,
        hour=now.hour,
        minute=now.minute,
        second=now.second,
        microsecond=now.microsecond
    )
