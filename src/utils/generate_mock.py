import time
from datetime import date, timedelta, datetime
from pathlib import Path

import pandas as pd
from faker import Faker
from numpy import random


def _generate_events(end_date):
    """Generates a fake dataset with events for 30 days before end date."""

    events = pd.concat(
        [
            _generate_events_for_day(date=end_date - timedelta(days=(30 - i)))
            for i in range(30)
        ],
        axis=0,
    )

    return events


def _generate_events_for_day(date):
    """Generates events for a given day."""

    # Use date as seed.
    seed = int(time.mktime(date.timetuple()))

    Faker.seed(seed)
    random_state = random.RandomState(seed)

    # Determine how many users and how many events we will have.
    n_users = random_state.randint(low=50, high=100)
    n_events = random_state.randint(low=200, high=2000)

    # Generate a bunch of users.
    fake = Faker()
    users = [fake.ipv4() for _ in range(n_users)]

    return pd.DataFrame(
        {
            "user": random_state.choice(users, size=n_events, replace=True),
            "date": pd.to_datetime(date),
        }
    )


def get_dates_between(start_date, end_date):
    return [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]


date_list = get_dates_between(date(2023, 10, 1), date(2023, 10, 30))

# for _date in date_list:
#     dataframe = _generate_events(end_date=_date)
#     output_path = f'/Users/rafael_negrao/projects/fialabdata/data-engineer-toolkit/airflow/data/events/{_date.strftime("%Y-%m-%d")}/events.json'
#     Path(output_path).parent.mkdir(exist_ok=True)
#     dataframe.to_json(output_path, orient="records")

# Teste
# input_path = f'/Users/rafael_negrao/projects/fialabdata/data-engineer-toolkit/airflow/data/events/{datetime.now().strftime("%Y-%m-%d")}/events.json'
# events = pd.read_json(input_path)
# stats = events.groupby(["date", "user"]).size().reset_index()
#
# print(stats)