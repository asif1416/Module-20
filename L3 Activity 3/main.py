# Get the country code
SPCMcountry_code = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}

# search dictionary for country code of India
print("Country code for India -")
print(SPCMcountry_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print("Country code for Japan -")
print(SPCMcountry_code.get('Japan', 'Not Found'))
