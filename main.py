import csv
def readFile():
    with open('CountryData.csv','r') as f:
        return f.readlines()
    f.close()

def createCountryDictionary():
    all = readFile()
    country_dictionary = {}
    for index,value in enumerate(all[1:]):
        # print(index) 
        # print(value.split(',')[0])
        # print(type(value))
        # thisdict = dict.fromkeys(str(index), value.split(',')[0])
        # thisdict.update({'value.split(',')[0]',str(index)})
        country_dictionary[value.split(',')[0]] = str(index+1)

    return country_dictionary

# with open('CountryData.csv','r') as f:
#     all = f.readlines()
#     # print(all)
#     # print(all[2])
#     # print(len(all))
#     country_dictionary = {}
#     for index,value in enumerate(all[1:]):
#         # print(index) 
#         # print(value.split(',')[0])
#         # print(type(value))
#         # thisdict = dict.fromkeys(str(index), value.split(',')[0])
#         # thisdict.update({'value.split(',')[0]',str(index)})
#         country_dictionary[value.split(',')[0]] = str(index+1)
#     print(country_dictionary)
        

def get_country_info():
    country_to_find  = input("Hello! What country would you like information on? ").capitalize()
    countries = createCountryDictionary()
    # print(countries[country_to_find])
    index = countries[country_to_find]

    print(f"index is {index}")
    # countries.get('country_to_find')
    # print(load_data_into_various_list())[0][0]
    data = []
    for country in load_data_into_various_list():
        # print(country[int(index)-1])
        # print(country[int(index)-1])
        data.append(country[int(index)-1])

        # print(f"Country info {i[int(index)]}")
    
    to_print = f"{data[0]} has a population of {data[1]} and a literacy rate of {data[2]}%. The estimate of the number of mobile subscriptions is {data[3]}, while that of internet users {data[4]}."
    to_print_2 = f"{data[0]} produces {data[5]} billion KWh of electricity annually, while it consumes {data[6]} billion KWh of electricity."
    print(to_print,to_print_2)
    #call funtion to print to file
    write_data_to_file(data)
    return data
      

def load_data_into_various_list():
    all = readFile()
    
    country_name = [] 
    population= []
    literacy= []
    mobile= []
    internet= []
    elect_production= []
    elect_consumption= []

    for index,value in enumerate(all[1:]):
        # print(value.split(','))
        country_name.append(value.split(',')[0])
        population.append(value.split(',')[1])
        literacy.append(value.split(',')[2])
        mobile.append(value.split(',')[3])
        internet.append(value.split(',')[4])
        elect_production.append(value.split(',')[5])
        elect_consumption.append(value.split(',')[6])
    # print(country_name, population, literacy, mobile, internet, elect_production,elect_consumption)
    return (country_name, population, literacy, mobile, internet, elect_production,elect_consumption)
    # print(country_name,population)

# PART 2 : Q3
def write_data_to_file(country):
    # open file for write
    header = ['Country Name','Mobile Subscription per capita','Internet users per capita']

    # filename = f'{country}.txt'
    filename = f'{country[0].lower()}.txt'
    # print(country)
    data = [country[0],int(country[3])/int(country[1]),int(country[4])/int(country[1])]
    # print(data)
    with open(filename, 'w', newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerow(data)
    # Write headings
    # Use user input to get data write to file
    # f. write(header)
    f.close()
    

# readFile()
# print(createCountryDictionary())

# PART 2 : Q4
def compute_and_report():
    all = load_data_into_various_list()
    # print(all[1])
    # print(type(a[1]))

    #cast all string values to integers
    casted_population = [int(population) for population in all[1]]
    casted_literacy = [int(literacy) for literacy in all[2]]
    casted_mobile = [int(mobile) for mobile in all[3]]
    casted_internet = [int(internet) for internet in all[4]]
    casted_electricity_production = [int(electricity_production) for electricity_production in all[5]]
    casted_electricity_consumption = [int(electricity_consumption) for electricity_consumption in all[6]]
    # print(f"casted elect: {casted_electricity_production}")

    print()
    print(f"Total population of Africa is: {sum(casted_population)}")
    print()
    # get index
    index_of_least_populous_country = casted_population.index(min(casted_population))
    index_of_most_populous_country = casted_population.index(max(casted_population))
    print(f"{all[0][index_of_least_populous_country]} is the least populated country in Africa")
    print(f"{all[0][index_of_most_populous_country]} is the Most populated country in Africa")
    print()
    #The most populous and least populous African countries
    # print(f"Least populous : {all[0][casted_population.index(min(casted_population))]}")
    # print(f"Most populous: {all[0][casted_population.index(max(casted_population))]}")
    # print()

    # The countries with the highest and lowest literacy rates
    index_of_least_literacy_country = casted_literacy.index(min(casted_literacy))
    index_of_most_literacy_country = casted_literacy.index(max(casted_literacy))
    print(f"{all[0][index_of_least_literacy_country]} is the country with the least literacy rate in Africa")
    print(f"{all[0][index_of_most_literacy_country]} is the country with the highest literacy rate in Africa")
    print()

    # The “average” literacy rate in Africa, computed by weighting each country’s literacy
    # rate by the country’s population, and dividing by the total population.
    total_literacy_rate = sum(casted_literacy)/sum(casted_population)
    print(f"The average literacy rate in Africa is: {total_literacy_rate}%")
    print()

    #The countries with the highest and lowest number of mobile subscriptions per capita
    mobile_sub_per_capita = [ i/j for i,j in zip(casted_mobile,casted_population)] 
    # print(len(x))
    index_of_highest_mobile_sub = mobile_sub_per_capita.index(max(mobile_sub_per_capita))
    index_of_lowest_mobile_sub = mobile_sub_per_capita.index(min(mobile_sub_per_capita))
    print(f"{all[0][index_of_highest_mobile_sub]} is the country with the highest number of mobile subscriptions per capita")
    print(f"{all[0][index_of_lowest_mobile_sub]} is the country with the lowest number of mobile subscriptions per capita")
    print()

    #The countries with the highest and lowest numbers of internet users per capita
    internet_users_per_capita = [ i/j for i,j in zip(casted_internet,casted_population)] 
    # print(len(x))
    index_of_highest_internet_users = internet_users_per_capita.index(max(internet_users_per_capita))
    index_of_lowest_internet_users = internet_users_per_capita.index(min(internet_users_per_capita))
    print(f"{all[0][index_of_highest_internet_users]} is the country with the highest number of internet users per capita")
    print(f"{all[0][index_of_lowest_internet_users]} is the country with the lowest number of internet users per capita")
    print()

    x = [ index for index, (i,j) in enumerate(zip(casted_electricity_production,casted_electricity_consumption)) if i>j]
    print("LIST OF ELECTRICITY EXPORTERS:")
    # print(x)

    for index in x:
        # print(index)
        print(f"{all[0][index]}")



    y = [ index for index, (i,j) in enumerate(zip(casted_electricity_production,casted_electricity_consumption)) if j>i]
    print()
    print("LIST OF ELECTRICITY IMPORTERS:")
    for index in y:
        # print(index)
        print(f"{all[0][index]}")
    


    
    



if __name__ == "__main__":
    # get_country_info()
    compute_and_report()
    # write_data_to_file("ghana")
    # print(tuple(load_data_into_various_list())[0][0])
    # all_list = load_data_into_various_list()
    # for i in all_list:
    #     print(i[0])