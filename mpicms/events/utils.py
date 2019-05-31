import calendar
import datetime

from django.utils import timezone


DATE_FORMAT_RE = r'^([0-9]){4}\.([0-9]){2}\.([0-9]){2}$'


def get_start_end(period, start_date):
    if re.match(cls.DATE_FORMAT_RE, start_date):
        date_params = [int(i) for i in start_date.split('.')]
        start_date = date_to_datetime(datetime.date(*date_params))
    else:
        start_date = timezone.now().replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

    # Clean the start and end dates to conform to the requested period
    start_date, end_date = cls.TIME_PERIODS[period.lower()](start_date)
    return start_date, end_date


def date_to_datetime(date, time_choice='min'):
    """
    Convert date to datetime.

    :param date: date to convert
    :param time_choice: max or min
    :return: datetime
    """
    choice = getattr(datetime.datetime, 'min' if time_choice == 'min' else 'max').time()
    return timezone.make_aware(
        datetime.datetime.combine(date, choice),
        timezone.get_current_timezone(),
    )


def add_months(date, months):
    """
    Add months to the date.

    :param date:
    :param months:
    :return:
    """
    month = date.month - 1 + months
    year = int(date.year + month / 12)
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def remove_months(date, months):
    """
    Add months to the date.

    :param date:
    :param months:
    :return:
    """
    month = date.month - 1 - months
    year = int(date.year + month / 12)
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)
