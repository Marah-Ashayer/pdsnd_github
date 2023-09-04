# import neede pakages
import time
import pandas as pd
import numpy as np
#data files we will use
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
    city=input("\n Enter a City  (chicago, new york city, washington):\n").lower()
    while(city not in ['chicago','new york city','washington']):
        print("City Name is Not Valid")
        city=input("\n Enter a City  (chicago, new york city, washington):\n").lower()
        if city in ['chicago','new york city','washington']:
            break
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("\n Enter a month (all, january, february,march,april,may,june) \n").lower()
    while(month not in ['all','january', 'february','march','april','may','june']):
        print("Month is Not Valid")
        city=input("\n Enter a month  ['all','january', 'february','march','april','may','june']:\n").lower()
        if month in ['all','january', 'february','march','april','may','june']:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("\n Enter a day (all, monday, tuesday,wednesday,thursday,friday,saturday, sunday) \n").lower()
    while(day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']):
        
        print("day is not valid")
        day=input("\n Enter a day  ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:\n").lower()
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
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
    df=pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all' :
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print( "popular_month: ",popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print( "popular_day: ",popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print( "popular_hour: ",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('popular start station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('popular end station:', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Station'] = df['Start Station'] + ' - ' + df['End Station']
    popular_combination_station = df['Combination Station'].mode()[0]
    print('popular combination station:', popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('Count Of User Types: ', count_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df :
        counts_of_gender = df['Gender'].value_counts()
        print(' Count of genders is: ',counts_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print(' earliest birth year: ',earliest_birth_year)
            
        most_recent_birth_year= df['Birth Year'].max()
        print(' most recent birth year : ',most_recent_birth_year)

        most_common_birth_year = df['Birth Year'].mode()[0]
        print(' most common birth year: ',most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def view_data(df):
    view_data = input("Would you like to view data? Enter yes or no?\n")
    view_data = view_data.lower()
    start_loc1 = 0
    start_loc2 = 5
    while view_data == "yes":
        print(df.iloc[start_loc1:start_loc2])
        start_loc1 += 5
        start_loc2 += 5
        cont = input("Want to continue?\n").lower()
        while cont not in ["yes", "no"]:
            print("Invalid input, Yes or No.\n")
            cont = input("Want to continue?\n").lower()
            if cont in ["yes", "no"]:
                break
        if cont == "yes":
            continue
        elif cont == "no":
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
        print("Game Over")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    


if __name__ == "__main__":
    main()




