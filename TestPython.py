import re

#date_string = "December 1, 2023 December 31, 2023"
#date_string = "August 1, 2023-August 31, 2023"

date_string = " August 1, 2023-August 31, 2023"

# Define a regular expression pattern to match dates in the format "Month Day, Year"
date_pattern = r'(\w+\s\d{1,2},\s\d{4})'

# Find all matches of the date pattern in the input string
dates = re.findall(date_pattern, date_string)

for date in dates:
    print(date)

