from datetime import datetime
from isoweek import Week

from .utils import date_to_datetime, add_months


class TimePeriod:
    TIME_PERIODS = {
        'year': get_year_range,
        'week': get_week_range,
        'month': get_month_range,
        'day': get_day_range,
    }

    def __init__(self, start_date):
        pass

    def get_year_range(start_date):
        """
        Get the start and end datetimes for the year

        :param start_date: period start_date
        :type start_date: datetime.datetime()
        :return: tuple start_datetime, end_datetime
        """
        start_date = datetime(start_date.year, 1, 1)
        end_date = date_to_datetime(add_months(start_date, 12), 'max')
        return start_date, end_date


    def get_month_range(start_date):
        """
        Get the start and end datetimes for the month

        :param start_date: period start_date
        :type start_date: datetime.datetime()
        :return: tuple start_datetime, end_datetime
        """
        start_date = datetime(start_date.year, start_date.month, 1)
        end_date = date_to_datetime(
            add_months(start_date.date(), 1),
            'max'
        )
        return start_date, end_date


    def get_week_range(start_date):
        """
        Get the start and end datetimes for the week

        :param start_date: period start_date
        :type start_date: datetime.datetime()
        :return: tuple start_datetime, end_datetime
        """
        period = Week(start_date.year, start_date.date().isocalendar()[1])
        start_date = date_to_datetime(period.monday())
        end_date = date_to_datetime(period.sunday(), 'max')
        return start_date, end_date


    def get_day_range(start_date):
        """
        Get the start and end datetimes for the day

        :param start_date: period start_date
        :type start_date: datetime.datetime()
        :return: tuple start_datetime, end_datetime
        """
        start_date = date_to_datetime(start_date.date(), 'min')
        end_date = date_to_datetime(start_date.date(), 'max')
        return start_date, end_date
