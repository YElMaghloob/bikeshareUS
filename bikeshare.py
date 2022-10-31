import time
import pandas as pd
import numpy as np

CITY_DATA = { 'CHI': 'chicago.csv',
              'NY': 'new_york_city.csv',
              'WASH': 'washington.csv' }

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
    city = input('Please input an ALL CAPS abbreviation for the city you would like to view: CHI (Chicago), NY (New York), WASH (Washington\n').upper()
    while city not in CITY_DATA.keys():
        print('There seems to be a mistake. Please check your entry for city.\n')
        city = input('Please input an ALL CAPS abbreviation for the city you would like to view: CHI (Chicago), NY (New York), WASH (Washington\n').upper()
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
    month = input('Please input a 3-letter abbreviation for the month you wish to view (jan, feb, mar, apr, may, or jun); otherwise input "all"\n').lower()
    while month not in months:
        print('There seems to be a mistake. Please check your entry for month.\n')
        month = input('Please input a 3-letter abbreviation for the month you wish to view (jan, feb, mar, apr, may, or jun); otherwise input "all"\n').lower()
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'All']
    day = input('Please input a specific day to view (Saturday, Sunday, Monday, etc.); otherwise input "all"\n').title()
    while day not in days:
        print('There seems to be a mistake. Please check your entry for day.\n')
        day = input('Please input a specific day to view (Saturday, Sunday, Monday, etc.); otherwise input "all"\n').title()
        break

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
    #filtering by city
    df = pd.read_csv(CITY_DATA[city])
    #Start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extracting month and day columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of week'] = df['Start Time'].dt.weekday_name
    
    #filtering by month
    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
        month = months.index(month) + 1
        
        is_month = df['Month']==month
        df = df[is_month]
        
    #filtering by day
    if day != 'All':
        is_day = df['Day of week']==day
        df = df[is_day]
    
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print('The most common month of travel is:', common_month)

    # TO DO: display the most common day of week
    common_day = df['Day of week'].mode()[0]
    print('The most common month of travel is:', common_day)

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_hour = df['Start Hour'].mode()[0]
    print('The most common hour to start travel is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def station_stats(df):#     """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Routes...\n')
    start_time = time.time()

    
    # TO DO: display most commonly used start station
    common_start_stn = df['Start Station'].mode()[0]
    print('The most common start station is:', common_start_stn)

    # TO DO: display most commonly used end station
    common_end_stn = df['End Station'].mode()[0]
    print('The most common end station is:', common_end_stn)

    # TO DO: display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'] + ' --> ' + df['End Station']
    common_route = df['Route'].mode()[0]
    print('THe most common travel route is:', common_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()/3600
    print('The total travel time in hours is:', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()/60
    print('The mean travel time in minutes is:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe breakdown of user types is as folows:\n', user_types)
    
          

    try:
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('\nThe breakdown of user genders is as follows:\n', gender_counts)
        
        # TO DO: Display earliest, most recent, and most common year of birth
        early_YOB = df['Birth Year'].min()
        print('\nEarliest user year of birth:', early_YOB)
        
        recent_YOB = df['Birth Year'].max()
        print('Most recent user year of birth:', recent_YOB)
        
        common_YOB = df['Birth Year'].mode()[0]
        print('Most common user year of birth:', common_YOB)
        
    except:
        print('\n\nGender and Year of Birth user data is not available for the city of Washington.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        more_data = input('\nWould you like to view 5 more lines of the selected raw data? Enter yes or no.\n')
        answers = ['yes', 'no']
        while more_data.lower() not in answers:
            print('There seems to be a mistake. Please enter yes or no.\n')
            more_data = input('\nWould you like to view 5 more lines of the selected raw data? Enter yes or no.\n')
            break
        
        for i in df.index:
            if more_data.lower() == 'yes':
                print(df.iloc[i*5:(i+1)*5])  
                more_data = input('\nWould you like to view 5 more lines of the selected raw data? Enter yes or no.\n').lower()
            else:
                print('End of data.\n')
                break
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you! :)')
            break
            



if __name__ == "__main__":
	main()
