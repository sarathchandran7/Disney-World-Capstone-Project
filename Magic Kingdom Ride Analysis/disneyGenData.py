# Import required modules
import datetime
import numpy as np
import pandas as pd
import random
import math
from datetime import timedelta
from datetime import time

# Set seed for reproducibility
random.seed(42)

# Define ride names and park areas
rides = ['Enchanted Tiki Room', 'Jungle Cruise', 'The Magic Carpets of Aladdin', 'Pirates of the Caribbean', 'Swiss Family Treehouse', 'Fantasyland', 'The Barnstormer', 'Dumbo the Flying Elephant', 'Enchanted Tales with Belle', "it's a small world", 'Mad Tea Party', "Mickey's PhilharMagic", 'The Many Adventures of Winnie the Pooh', "Peter Pan's Flight", "Prince Charming's Regal Carrousel", 'Princess Fairytale Hall', 'Seven Dwarfs Mine Train', 'Under the Sea: Journey of the Little Mermaid', 'Frontierland', 'Big Thunder Mountain', 'Country Bear Jamboree', 'Tom Sawyer Island', 'Splash Mountain', 'Liberty Square', 'The Hall of Presidents', 'Haunted Mansion', 'Liberty Square Riverboat', 'Main Street USA', 'Tomorrowland', 'Astro Orbiter', "Buzz Lightyear's Space Ranger Spin", 'Carousel of Progress', 'Monsters, Inc. Laugh Floor', 'Space Mountain', "Stitch's Great Escape! (Seasonal)", 'Tomorrowland Speedway', 'Tomorrowland Transit Authority', 'TRON Lightcycle Power Run Rollercoaster']

# Generate synthetic data
data = []
for i in range(1,7):
    currentDate = (datetime.datetime.today() - datetime.timedelta(days=i)).date()
    for ride in rides:
        for time in range(9,23):
            currentTime = datetime.time(hour=time,minute=0,second=0)
            ride_name = ride
            if (time <= 12):
                totalSales = random.randint(50, 120)
                fastPassReserv = math.ceil(totalSales*random.randint(5,45)/100)
            elif (time > 12 and time <= 19):
                totalSales = random.randint(100, 300)
                fastPassReserv = math.ceil(totalSales*random.randint(30,60)/100)
            else:
                totalSales = random.randint(50, 100)
                fastPassReserv = math.ceil(totalSales*random.randint(20,55)/100)
            age_group = random.choice(['Child', 'Teen', 'Adult', 'Senior'])    
            data.append([currentDate, currentTime, ride_name, fastPassReserv ,totalSales, age_group])


# Create a DataFrame
columns = ['Date', 'Daytime', 'Ride_Name', 'Fast_Pass_Plus_Tickets', 'Total_Ticket_Sale_In_Last_Hour', 'Highest_Age_Group']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('./disney_data_custom_separated_time.csv', index=False)
