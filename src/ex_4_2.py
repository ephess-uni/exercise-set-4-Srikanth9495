""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """
    logstamp_to_datetime returns a datetime  object for a string object passed.
    """
    date_pattern = "%Y-%m-%dT%H:%M:%S"
    date_obj = datetime.strptime(datestr,date_pattern)
    return date_obj


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')
