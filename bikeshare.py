import time
import pandas as pd
import numpy as np
import math

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    
    # get user input for city 
    city=input("Which city would you like to see the data!!Chicago,New York City or Washington: ").lower()
    print()
    count = 1
    while city not in CITY_DATA:
        if(count == 3):
            print("You have exceeded the number of tries!!Please enter valid inputs")
            print()
            print()
            main()
        city=input("Enter a valid city name from the given list!!! chicago,new york city or washington: ").lower()
        print()
        count+=1
        
    exit_contnue=input("Looks like you wanted to see the data for {}!!If no, Exit the program!! (yes/no): ".format(city.title()))
    print()
    
    # get user input for month & day of week 
    if(exit_contnue.lower()=='no'):
        exit()
    elif(exit_contnue.lower()=='yes'):
        
        month_day=input("Would you like to filter by month, day, both or none.If no filter, type 'none': ")
        print()
        
        if(month_day.lower()=='month'):
            
            month=input("Please enter the month from the provided list only!!!['january','february','march','april','may','june']: ").lower()
            print()
            day='all'
            while month not in ['january','february','march','april','may','june']:
                
                month=input("Please enter a valid month name from the list provided: ")
                print()
                
        elif(month_day.lower()=='day'):
            month='all'
            day=input("Please enter the day from the provided list only!! :['mon','tue','wed','thu','fri','sat','sun']: ").lower()
            print()
            while day not in ['mon','tue','wed','thu','fri','sat','sun']:
                day=input("Please enter a valid day from the list provided: ")
                print()
        elif(month_day.lower()=='both'):
            month=input("Please enter the month from the provided list only!!!['january','february','march','april','may','june']: ").lower()
            print()
            while month not in ['january','february','march','april','may','june']:
                
                month=input("Please enter a valid month name from the list provided: ")
                print()
            day=input("Please enter the day from the provided list only!! :['mon','tue','wed','thu','fri','sat','sun']: ").lower()
            print()
            while day not in ['mon','tue','wed','thu','fri','sat','sun']:
                day=input("Please enter a valid day from the list provided: ")
                print()
                
        elif (month_day.lower()=='none'):     
            month='all'
            day='all'
            
        else:
            print("Kindly enter valid datas")
            print()
            print()
            main()
            
    else:
        print("Could you please try again?")
        print()
        print()
        main()
    
    print('-'*40)
    #print(city,month,day)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day"""
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name.apply(lambda x: x[:3])  
    if month != 'all':       
        months = ['january', 'february', 'march', 'april', 'may', 'june']    
        month = months.index(month)+1
        df = df[df['month']==month]

    if day != 'all':  
        df = df[df['day_of_week']==day.title()]
    
    df.drop(columns='day_of_week',inplace=True)
    df.drop(columns='month',inplace=True)
    #print(df)
    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #print(df)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    #print(df)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month_number=df['month'].mode()[0]
    common_month=months[common_month_number-1]
    common_day_of_week=df['day_of_week'].mode()[0]
    common_start_hour=df['hour'].mode()[0]
    
    # display the most common month, most common day of week & most common start hour
    
    if(month!='all' and day!='all'):     
        print("The Most Common Month: ",common_month.title())
        print("The Most Common Day Of Week: ",common_day_of_week)
        print("The Most Common Start Hour: ",common_start_hour)
        print("Filtered By Both: ",month,day)
        
    elif(month=='all' and day!='all'):
        
        print("The Most Common Month: ",common_month.title())
        print("The Most Common Day Of Week: ",common_day_of_week)
        print("The Most Common Start Hour: ",common_start_hour)
        print("Filtered By Day: ",day)
    elif(month!='all' and day=='all'):
        print("The Most Common Month: ",common_month.title())
        print("The Most Common Day Of Week: ",common_day_of_week)
        print("The Most Common Start Hour: ",common_start_hour)
        print("Filtered By Month: ",month)
    else:
        print("The Most Common Month: ",common_month.title())
        print("The Most Common Day Of Week: ",common_day_of_week)
        print("The Most Common Start Hour: ",common_start_hour)
        print("Filtered By None: ",month,day)
        
    #print(common_month,common_day_of_week,common_start_hour)
    
    df.drop(columns='day_of_week',inplace=True)
    df.drop(columns='month',inplace=True)
    df.drop(columns='hour',inplace=True)
    #print(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    Common_Start_Station=df['Start Station'].mode()[0]
    Common_End_Station=df['End Station'].mode()[0]
    Common_Start_End_Station='From '+(df['Start Station'] +' To '+df['End Station']).mode()[0]

    # TO DO: display most commonly used start station
  
    print("The Most Common Start Station: {}".format(Common_Start_Station))
    
    # TO DO: display most commonly used end station
    
    print("The Most Common End Station: {}".format(Common_End_Station))
    
    # TO DO: display most frequent combination of start station and end station trip
    
    print("The Most Common Start & End Station : {}".format(Common_Start_End_Station))
    
    
    #print(df)
    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    
    trip_duration_sum=df['Trip Duration'].sum()
    print("The Total Travel Time in Seconds : {}".format(trip_duration_sum))

    
    
    days=trip_duration_sum//(86400)
    trip_duration_sum=trip_duration_sum-(86400*days)
    hours=trip_duration_sum//(3600)
    trip_duration_sum=trip_duration_sum-(3600*hours)
    minutes=trip_duration_sum//(60)
    trip_duration_sum=trip_duration_sum-(60*minutes)
    seconds=trip_duration_sum
    print("The total travel time is {} days , {} hours , {} minutes and {} seconds".format(np.math.ceil(days),np.math.ceil(hours),minutes,seconds))
    
    #print(days,hours,minutes,seconds)
    
    # TO DO: display mean travel time
    trip_duration_mean=df['Trip Duration'].mean()
    
    print("The Mean Travel Time in Seconds : {}".format(trip_duration_mean))
    mean_days=trip_duration_mean//(86400)
    trip_duration_mean=trip_duration_mean-(86400*mean_days)
    mean_hours=trip_duration_mean//(3600)
    trip_duration_mean=trip_duration_mean-(3600*mean_hours)
    mean_minutes=trip_duration_mean//(60)
    trip_duration_mean=trip_duration_mean-(60*mean_minutes)
    mean_seconds=trip_duration_mean
  
    
    print("The mean travel time is {} days , {} hours , {} minutes and {} seconds".format(np.math.ceil(mean_days),np.math.ceil(mean_hours),mean_minutes,mean_seconds))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #print(df)
    # TO DO: Display counts of user types
    user_type=df.groupby('User Type', as_index=False).count()
    print("The Number of User Types: ",len(user_type))
    for i in range(len(user_type)):
        print("{} : {} ".format(user_type['User Type'][i],user_type['Start Time'][i]))
        
        
    print()    
    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print("No Gender data available for this month!!")
    else:
        gender_type=df.groupby('Gender', as_index=False).count()
        gender_data_NaN=df['Gender'].isnull().sum().sum()
        print("The Number of Gender : ",len(gender_type))
        for i in range(len(gender_type)):
            print("{} : {} ".format(gender_type['Gender'][i],gender_type['Start Time'][i]))
        
        print("The total number of unavailble gender data: ",gender_data_NaN)
    
    print()
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print("No Birth data available for this month!!")
    else:
        
        print("The Earliest Birth Year : {} ".format(np.math.ceil(df['Birth Year'].min())))
        
        print("The Most Recent Birth Year : {} ".format(np.math.ceil(df['Birth Year'].max())))
        
        print("The Most Common Birth Year : {} ".format(np.math.ceil(df['Birth Year'].mode()[0])))
    
    
    
    
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
