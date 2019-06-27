import pygal.maps.world

COUNTRIES = pygal.maps.world.COUNTRIES.items()

# for code, name in sorted(COUNTRIES):
#     print(name)
count = 0
def get_country_code(country_name):
    print(COUNTRIES)
    for code,name in sorted(COUNTRIES):
        print(code,name)
    #    if country_name == name:
    #        print(name,code)
    #        return code
    #    return None

#print(get_country_code('Arab World'))

