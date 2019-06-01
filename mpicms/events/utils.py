# from copy import copy
import calendar
import datetime as dt
from datetime import datetime
from isoweek import Week


# from django.utils import timezone


DATE_FORMAT_RE = r'^([0-9]){4}\.([0-9]){2}\.([0-9]){2}$'


# class datetime(dt.datetime):

#     @classmethod
#     def from_date(cls, init_date, time_choice='min'):
#         """
#         Convert date to datetime.

#         :param date: date to convert
#         :param time_choice: max or min
#         :return: datetime
#         """
#         choice = getattr(cls, 'min' if time_choice == 'min' else 'max').time()
#         return timezone.make_aware(
#             cls.combine(init_date, choice),
#             timezone.get_current_timezone(),
#         )


class date(dt.date):
    # def __init__(self, date):
    #     self.date = date

    #     # If start date = string

    #     if re.match(cls.DATE_FORMAT_RE, start_date):
    #         date_params = [int(i) for i in start_date.split('.')]
    #         start_date = date_to_datetime(datetime.date(*date_params))
    #     else:
    #         start_date = timezone.now().replace(
    #             hour=0,
    #             minute=0,
    #             second=0,
    #             microsecond=0,
    #         )

    # self.time_periods = {
    #     'year': get_year_range,
    #     'week': get_week_range,
    #     'month': get_month_range,
    #     'day': get_day_range,
    # }


    # @property
    # def get_range(start_date, period):
    #     """
    #     Get the start and end datetimes for the given period

    #     :param start_date: period start_date
    #     :type start_date: datetime.datetime()
    #     :type period: String
    #     :return: tuple start_datetime, end_datetime
    #     """
    #     time_periods = {
    #         'year': get_year_range,
    #         'week': get_week_range,
    #         'month': get_month_range,
    #         'day': get_day_range,
    #     }
    #     return time_periods[period.lower()](start_date)


    @property
    def year_range(self):
        """
        Get the start and end datetimes for the year

        :param start_date: period start_date
        :type start_date: datetime.datetime()
        :return: tuple start_datetime, end_datetime
        """
        start_date = datetime.combine(self.replace(month=1, day=1), datetime.min.time())
        end_date = datetime.combine(self.replace(month=12, day=31), datetime.min.time())
        return start_date, end_date

    @property
    def month_range(self):
        """
        Get the start and end datetimes for the month

        :param start_date: period start_date
        :type start_date: datetime.datetime()
        :return: tuple start_datetime, end_datetime
        """
        month_days = calendar.monthrange(self.year, self.month)[1]
        start_date = datetime.combine(self.replace(day=1), datetime.min.time())
        end_date = datetime.combine(self.replace(month_days), datetime.max.time())

        return start_date, end_date

    @property
    def week_range(self):
        """
        Get the start and end datetimes for the week

        :param start_date: period start_date
        :type start_date: datetime.datetime()
        :return: tuple start_datetime, end_datetime
        """
        period = Week(self.year, self.isocalendar()[1])
        start_date = datetime.combine(period.monday(), datetime.min.time())
        end_date = datetime.combine(period.sunday(), datetime.max.time())
        return start_date, end_date

    @property
    def day_range(self):
        """
        Get the start and end datetimes for the day

        :param start_date: period start_date
        :type start_date: datetime.datetime()
        :return: tuple start_datetime, end_datetime
        """
        start_date = datetime.combine(self, datetime.min.time())
        end_date = datetime.combine(self, datetime.max.time())
        return start_date, end_date

    # def add_months(self, months):
    #     """
    #     Add months to the date.

    #     :param date:
    #     :param months:
    #     :return:
    #     """
    #     month = self.month - 1 + months
    #     year = int(self.year + month / 12)
    #     month = month % 12 + 1
    #     day = min(self.day, calendar.monthrange(year, month)[1])

    #     return self.__class__(year, month, day)

    # def remove_months(self, months):
    #     """
    #     Add months to the date.

    #     :param date:
    #     :param months:
    #     :return:
    #     """
    #     month = self.month - 1 - months
    #     year = int(self.year + month / 12)
    #     month = month % 12 + 1
    #     day = min(self.day, calendar.monthrange(year, month)[1])

    #     return self.__class__(year, month, day)










# def date_to_datetime(date, time_choice='min'):
#     """
#     Convert date to datetime.

#     :param date: date to convert
#     :param time_choice: max or min
#     :return: datetime
#     """
#     choice = getattr(datetime.datetime, 'min' if time_choice == 'min' else 'max').time()
#     return timezone.make_aware(
#         datetime.datetime.combine(date, choice),
#         timezone.get_current_timezone(),
#     )




# def get_start_end(period, start_date):
#     if re.match(cls.DATE_FORMAT_RE, start_date):
#         date_params = [int(i) for i in start_date.split('.')]
#         start_date = date_to_datetime(datetime.date(*date_params))
#     else:
#         start_date = timezone.now().replace(
#             hour=0,
#             minute=0,
#             second=0,
#             microsecond=0,
#         )

#     # Clean the start and end dates to conform to the requested period
#     start_date, end_date = cls.TIME_PERIODS[period.lower()](start_date)
#     return start_date, end_date



