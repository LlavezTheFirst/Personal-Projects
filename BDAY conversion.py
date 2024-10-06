from datetime import datetime

def calculate_age(birth_date, current_date):
    # Calculate the difference between the current date and birth date
    difference = current_date - birth_date
    
    # Calculate years
    years = difference.days // 365
    
    # Calculate remaining months and days
    remaining_days = difference.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    
    return years, months, days

def main():
    # Get birth date from user
    birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    
    # Get current date from user
    current_date_str = input("Enter the current date (YYYY-MM-DD): ")
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    
    # Calculate age
    years, months, days = calculate_age(birth_date, current_date)
    
    # Print result
    print(f"You have been alive for {years} years, {months} months, and {days} days.")

if __name__ == "__main__":
    main()
