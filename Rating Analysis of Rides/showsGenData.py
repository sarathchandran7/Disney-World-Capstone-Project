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

shows = {
    "The Magic Kingdom" : ["Mickey's PhilharMagic", "Monsters, Inc. Laugh Floor", "Country Bear Jamboree", "Enchanted Tiki Room", "The Hall of Presidents", "Cinderella Castle Projection Shows (Seasonal)", "Dapper Dans (Main Street, U.S.A.)]"],
    "Epcot" : ["Impressions de France (in the France Pavilion)", "Reflections of China (in the China Pavilion)", "American Adventure (in the America Pavilion)", "Voices of Liberty (in the America Pavilion)", "Disney & Pixar Short Film Festival (in Future World)", "Mariachi Cobre (in the Mexico Pavilion)", "JAMMitors (Future World)"],
    "Animal Kingdom" : ["Beauty and the Beast - Live on Stage", "Indiana Jones Epic Stunt Spectacular!", "Voyage of the Little Mermaid", "For the First Time in Forever: A Frozen Sing-Along Celebration", "Disney Junior Dance Party!", "Star Wars: A Galaxy Far, Far Away", "Fantasmic!"],
    "Hollywood Studios" : ["Festival of the Lion King", "Finding Nemo - The Musical", "UP! A Great Bird Adventure", "Rivers of Light (Nighttime show at the Discovery River Amphitheater)", "Burudika (in Africa)", "Pandora Utility Suit (in Pandora - The World of Avatar)", "Discovery Island Carnivale (Seasonal)"]
}

# Generate synthetic data
data = []
for i in range(0,21):
    currentDate = (datetime.datetime.today() - datetime.timedelta(days=i)).date()
    for park,showList in shows.items():
        parkName = park
        for show in showList:
            showName = show
            avgDayRating = round(random.uniform(1.5,5),1)
            data.append([currentDate, parkName, showName, avgDayRating])



# Create a DataFrame
columns = ['Date', 'Park', 'Show', 'Average_Rating_Per_Day']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('./Week 4/showsRatingGenData.csv', index=False)