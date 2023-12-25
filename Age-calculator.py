from datetime import date,datetime

def calculate_age(birthdate):
    today = date.today()
    if(birthdate < date.today()):
        
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            months = 12 - birthdate.month + today.month
        else:
            months = today.month - birthdate.month

        if today.day < birthdate.day:
            days = birthdate.day - today.day
            if months == 0:
                age -= 1
                months = 11
    
        else:
            days = today.day - birthdate.day

        return age, months, days
    else:
        print('enter valid date')
# Ask for user input
birthdate_str = input("Enter your birthdate in YYYY-MM-DD format: ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

# Calculate age
print('(years , months , days) = ',calculate_age(birthdate))
