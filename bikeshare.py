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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in CITY_DATA:
        city  = input("Would you like to see data for chicago, new york city or washington ?:\n")
        city = city.lower()
 
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in ["all", "january", "february", "march", "april", "may", "june"]:
        month  = input("Which month all, january, february, march, april, may, june?:\n")
        month = month.lower()
 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = ""
    while day_of_week not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        day_of_week  = input("Which day of week all, monday, tuesday, wednesday, thursday, friday, saturday, sunday?:\n")
        day_of_week  = day_of_week.lower()

    print('-'*40)
    return city, month, day_of_week


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
    # filter by month if applicable
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
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

    # TO DO: display the most common month
    most_month = df['month'].value_counts().idxmax()
    print('Most common month is :', most_month)

    # TO DO: display the most common day of week
    most_day = df['day_of_week'].value_counts().idxmax()
    print('Most common day of week is :', most_day)

    # TO DO: display the most common start hour
    most_day = df['start_hour'].mode()[0]
    print('Most common start hour is :', most_day)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()   #.mode()[0]
    print('Most commonly used start station is :', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station is :', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df[df['Start Station'] == df['End Station']]
    print('Most frequent combination of start station and end station trip is :', frequent_combination['Start Station'].value_counts().idxmax())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time :', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #df.fillna(method = 'backfill', axis = 0, inplace = True)
    df.fillna('', inplace = True)
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types :\n' , user_types)


    # TO DO: Display counts of gender
    try:
        users_gender = df['Gender'].value_counts()
    except:
        print('No Gender column in this file')
    else:
        print('Users gender :\n', users_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        common_year = df['Birth Year'].value_counts().idxmax()
        recent_year = df['Birth Year'].max()
    except:
        print('No Birth year column in this file')
    else:
        print('Earliest year is {} , Most recent year is {} , and Most common year of birth is {}'.format( earliest_year, recent_year, common_year))
    
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def print_rawdata(df, start):
    """
        This function is used to print raw data 
    """
    from itertools import islice
    stop = start+5
    for index, data in islice(df.iterrows(), start, stop):
        data_print = {'':data[0], 'End Station':data['End Station'],'End Time':data['End Time'],'Start Station':data['Start Station'],'Start Time':data['Start Time'], 'Trip Duration':data['Trip Duration'],'User Type':data['User Type']}
        try:
            dic = {'Birth Year':data['Birth Year'],'Gender':data['Gender']}
        except:
            data_print['Birth Year'] = ''
            data_print['Gender'] = ''
        else:
            data_print['Birth Year'] = data['Birth Year']
            data_print['Gender'] = data['Gender']
        print(data_print)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        #Print raw data
        start = 0
        raw_data = ''
        while  raw_data !='no':
            raw_data  = input("Do you want to see 5 lines of raw data ?:\n")
            raw_data = raw_data.lower()
            print_rawdata(df, start)
            start+=5
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
