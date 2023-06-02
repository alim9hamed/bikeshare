import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            'Enter the city (Chicago, New York City, Washington):\n').lower()
        if city in CITY_DATA:
            break
        else:
            print("="*50)
            print(f'WARINNG: "{city}" invalid syntsx'.center(50))
            print("="*50)

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input(
            'Which month? all or (january, february, march, april, may, june)\n').lower()
        if month in months:
            break
        else:
            print("="*50)
            print(f'WARINNG: "{month}" invalid syntsx'.center(50))
            print("="*50)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    daysOfWeek = ['all', 'sunday', 'monday', 'tuesday',
                  'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        day = input(
            'which day? all or ( sunday, monday, tuesday, wednesday, thursday, friday, saturday)\n').lower()
        if day in daysOfWeek:
            break
        else:
            print("="*50)
            print(f'WARINNG: "{day}" invalid syntsx'.center(50))
            print("="*50)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    # convert the Start Time column to datetime

    df['start_time'] = pd.to_datetime(df['start_time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['start_time'].dt.month
    df['day_of_week'] = df['start_time'].dt.day_of_week

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        daysOfWeek = ['sunday', 'monday', 'tuesday',
                      'wednesday', 'thursday', 'friday', 'saturday']
        day = int(daysOfWeek.index(day))
        df = df[df['day_of_week'] == day]

    return df


def display_data(df):
    """Display data when user wants"""
    view_data = input(
        "Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()

    start_loc = 0
    while (True):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input(
            "Do you wish to continue? Enter yes or no:\n").lower()
        if view_display.lower() != 'yes':
            break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['start_time'].dt.hour
    # display the most common month
    print(f"The most common moth: {df.month.mode()[0]}")
    # display the most common day of week
    print(f"The most common day: {df.day_of_week.mode()[0]}")
    # display the most common start hour?????????????????????
    print(f"The most common hour: {df.hour.mode()[0]}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(f"The most common start station: {df.start_station.mode()[0]}")

    # display most commonly used end station
    print(f"The most common end station: {df.end_station.mode()[0]}")

    # display most frequent combination of start station and end station trip
    print(
        f'most frequent combination of start station and end station: "{df.start_station.mode()[0]}" & "{df.end_station.mode()[0]}"')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f"The AVG of Trip Duration: {round(df.trip_duration.mean(),2)}")

    # display mean travel time
    print(f"The SUM of Trip Duration: {round(df.trip_duration.sum(),2)}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df["user_type"].value_counts())
    if len(df.columns) > 11:
        # Display counts of gender
        print(df["gender"].value_counts())

        # Display earliest, most recent, and most common year of birth
        print(f"Earliest Year of Birth: {round(df.birth_year.min())}")
        print(f'Most Recent Year of Birth: {round(df.birth_year.max())}')
        print(
            f'Most common Year of Birth: {round(int(df.birth_year.mode()[0]))}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
