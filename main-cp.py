
with open('CountryData.csv','r') as f:
    all = f.readlines()
    # print(all)
    # print(all[2])
    # print(len(all))
    country_dictionary = {}
    for index,value in enumerate(all[1:]):
        # print(index) 
        # print(value.split(',')[0])
        # print(type(value))
        # thisdict = dict.fromkeys(str(index), value.split(',')[0])
        # thisdict.update({'value.split(',')[0]',str(index)})
        country_dictionary[value.split(',')[0]] = str(index+1)
    print(country_dictionary)
        

def get_country_info(country):
    country  = input("Enter Country Name: ")
    pass