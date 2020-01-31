import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("Please select a city: chicago, new york city, washington: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Invalid city name. Please try again: ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("Please select a month or type 'all' to view all months: ").lower()

    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Invalid month. Please try again: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please select a day or type 'all' to view all days: ").lower()

    while day not in ['all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']:
        day = input("Invalid selection. Please try again: ").lower()

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']

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
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: {}".format(
        str(df['month'].mode().values[0]))
    )

    # display the most common day of week
    print("The most common day of the week is: {}".format(
        str(df['day_of_week'].mode().values[0]))
    )

    # display the most common start hour
    print("The most common hour is: {}".format(
        str(df['hour'].mode().values[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is: {}".format(
        str(df['Start Station'].mode().values[0]))
    )

    # display most commonly used end station
    print("The most common end station is: {}".format(
        str(df['End Station'].mode().values[0]))
    )

    # display most frequent combination of start station and end station trip
    print("The most common trip is: {}".format(
        str(df['trip'].mode().values[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Travel Time is: {}".format(
        str(df['Trip Duration'].sum()))
    )

    # display mean travel time
    print("Average Travel Time is: {}".format(
        str(df['Trip Duration'].mean()))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("User Types:\n",user_type,"\n")

    # Display counts of gender

    if 'Gender' in df:

        gender = df['Gender'].value_counts()
        print("Gender:\n",gender,"\n")

    # Display earliest, most recent, and most common year of birth
        print("The earliest year is: {}".format(
            str(int(df['Birth Year'].min())))
        )
        print("The latest birth year is: {}".format(
            str(int(df['Birth Year'].max())))
        )
        print("The most common birth year is: {}".format(
            str(int(df['Birth Year'].mode().values[0])))
        )
    else:
        print("No Gender or Birth Year data available for this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

#show raw data

    start_line = 0
    end_line = 5

    show_data = input("Would you like to see raw data?: (yes)(no) ").lower()

    if show_data == 'yes':
        while end_line <= df.shape[0] - 1:

            print(df.iloc[start_line:end_line,:])
            start_line += 5
            end_line += 5

            show_data_end = input("More?: ").lower()
            if show_data_end == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
