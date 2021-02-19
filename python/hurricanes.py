# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def update_damages(damages_list):
  updated_damages = []
  for item in damages_list:
    if item == 'Damages not recorded':
      updated_damages.append('Damages not recorded')
    elif "B" in item:
      updated_damages.append(float(item.replace('B', '')) * 1000000)
    elif "M" in item:
      updated_damages.append(float(item.replace('M', '')) * 1000000000)
  
  return updated_damages

# print(update_damages(damages))

# 2 
# Create a Table
def create_dict_hurricane(names, months, years, max_sustained_winds, areas_affected, update_damages, deaths):
  # key = name, value = resto
  dict_hurricane = {}
  for i in range(len(names)):
    dict_hurricane[names[i]] = {"Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": update_damages[i],
      "Deaths": deaths[i]}

  return dict_hurricane

# Create and view the hurricanes dictionary
hurricanes = create_dict_hurricane(names, months, years, max_sustained_winds, areas_affected, update_damages(damages), deaths)
# print(hurricanes)

# 3
# Organizing by Year
def convert_hurricanes(hurricanes):
  year_hurricanes = {}
  current_cane = []
  for value in hurricanes.values():
    current_year = value["Year"]
    current_cane = [value]

    if current_year in year_hurricanes.keys():
      year_hurricanes[current_year].append(current_cane)
    else:
      year_hurricanes[current_year] = current_cane

  return year_hurricanes

# create a new dictionary of hurricanes with year and key
hurricanes_year = convert_hurricanes(hurricanes)
# print(hurricanes_year)

# 4
# Counting Damaged Areas
# print(hurricanes["Cuba I"]["Areas Affected"])
def counting_damaged_areas(dictionary):
  # keys = areas afetadas, values = quantas vezes a area foi afetada
  damaged_areas = {}
  for key in dictionary.keys():
    for value in dictionary[key]["Areas Affected"]:
      if value in damaged_areas.keys():
        damaged_areas[value] += 1
      else:
        damaged_areas[value] = 1
  
  return damaged_areas

# create dictionary of areas to store the number of hurricanes involved in
affected_areas_count = counting_damaged_areas(hurricanes)
# print(affected_areas_count)

# 5 
# Calculating Maximum Hurricane Count
def maximun_hurricane_count(dictionary):
  max_area = list(dictionary.keys())
  max_area = max_area[1]
  max_area_count = 0
  for key in dictionary.keys():
    if max_area_count < dictionary[key]:
      max_area_count = dictionary[key]
      max_area = key
  return max_area, max_area_count
# find most frequently affected area and the number of hurricanes involved in
max_affected_areas = maximun_hurricane_count(affected_areas_count)
# print(max_affected_areas)

# 6
# Calculating the Deadliest Hurricane

def deadliest_hurricane(dictionary):
  hurricane = list(dictionary.keys())
  hurricane = hurricane[1]
  max_deaths = 0
  for key in dictionary.keys():
    num_deaths = dictionary[key]["Deaths"]
    if max_deaths < num_deaths:
      max_deaths = num_deaths
      hurricane = key
  return hurricane, max_deaths
# find highest mortality hurricane and the number of deaths
most_mortal_hurricane = deadliest_hurricane(hurricanes)
# print(most_mortal_hurricane)

# 7
# Rating Hurricanes by Mortality
def rating_hurricanes_mortality(dictionary):
  mortality_rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for key in dictionary.keys():
    mortality = dictionary[key]["Deaths"]
    if mortality <= 0:
      mortality_rating[0].append(key)
    elif (mortality > 0) and (mortality <= 100):
      mortality_rating[1].append(key)
    elif (mortality > 100) and (mortality <= 500):
      mortality_rating[2].append(key)
    elif (mortality > 500) and (mortality <= 1000):
      mortality_rating[3].append(key)
    elif (mortality > 1000) and (mortality <= 10000):
      mortality_rating[4].append(key)
    else:
      mortality_rating[5].append(key)

  return mortality_rating
# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = rating_hurricanes_mortality(hurricanes)
# print(hurricanes_by_mortality)

# 8 Calculating Hurricane Maximum Damage
def maximum_damage(hurricanes_dict):
  hurricane = list(hurricanes_dict.keys())
  hurricane = hurricane[1]
  max_damage = 0
  for key in hurricanes_dict.keys():
    damage = hurricanes_dict[key]["Damage"]
    if isinstance(damage, str):
      max_damage = max_damage
    elif max_damage < damage:
      max_damage = damage
      hurricane = key
  return hurricane, max_damage
# find highest damage inducing hurricane and its total cost
mostly_damage_hurricane = maximum_damage(hurricanes)
# print(mostly_damage_hurricane)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def rating_hurricanes_damage(dictionary):
  damage_scale = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for key in dictionary.keys():
    damage = dictionary[key]["Damage"]
    if isinstance(damage, str):
      damage = damage
    elif damage <= 0:
      damage_scale[0].append(key)
    elif (damage > 0) and (damage <= 100000000):
      damage_scale[1].append(key)
    elif (damage > 100000000) and (damage <= 1000000000):
      damage_scale[2].append(key)
    elif (damage > 1000000000) and (damage <= 10000000000):
      damage_scale[3].append(key)
    elif (damage > 10000000000) and (damage <= 50000000000):
      damage_scale[4].append(key)
    else:
      damage_scale[5].append(key)

  return damage_scale
# categorize hurricanes in new dictionary with damage severity as key
damage_severity = rating_hurricanes_damage(hurricanes)
print(damage_severity)
