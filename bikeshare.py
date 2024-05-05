import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITY_NAME = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?").strip().lower()
        if city in CITY_NAME:
            break
        else:
            print("Invalid input. Please choose from Chicago, New York City, or Washington.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? January, February, March, April, May, June, or all?").strip().lower()
        if month in MONTHS:
            break
        else:
            print("Invalid input. Please choose a valid month or 'all'.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?").strip().lower()
        if day in DAYS:
            break
        else:
            print("Invalid input. Please choose a valid day of the week or 'all'.")

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
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert 'Start Time' column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time' to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day_of_Week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month.lower() != 'all':
        df = df[df['Month'].str.lower() == month.lower()]

    # Filter by day of week if applicable
    if day.lower() != 'all':
        df = df[df['Day_of_Week'].str.lower() == day.lower()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['Month'].mode()[0]
    print("The most popular month for travel is: {}".format(most_month))

    # TO DO: display the most common day of week
    most_day_of_week = df['Day_of_Week'].mode()[0]
    print("The most popular day for travel is: {}".format(most_day_of_week))

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_hour = df['Hour'].mode()[0]
    print("The most popular start hour for travel is: {}".format(most_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: {}".format(most_start_station))
    # TO DO: display most commonly used end station
    most_end_station= df['End Station'].mode()[0]
    print("The most commonly used end station: {}".format(most_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station: {} ".format(most_frequent))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time: {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print("The user types are:\n{}".format(counts_user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print("The counts of gender are:\n{}".format(counts_gender))
    else:
        print("Gender data is not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        print("\nEarliest year of birth: {}".format(int(earliest)))
        
        most_recent = df['Birth Year'].max()
        print("\nMost recent year of birth: {}".format(int(most_recent)))
        
        most_common = df['Birth Year'].mode()[0]
        print("\nMost common year of birth: {}".format(int(most_common)))
    else:
        print("\nBirth year data is not available for this city.")

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()