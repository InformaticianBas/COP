AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
def prompt():
    print('********************************\nAutoCountry Vehicle Finder v0.3\n********************************\nPlease Enter the following number below from the following menu:\n\n1. PRINT all Authorized Vehicle\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. Exit')

menu_number = 0
while menu_number < 4:
    prompt()
    menu_number = int(input())
    if menu_number == 1:
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        for make in AllowedVehiclesList:
            print(make)
    elif menu_number == 2:
        search_field = str(input('Vehicle Search: '))
        if search_field in AllowedVehiclesList:
            print(search_field,'is an authorized vehicle.')
            continue
        else:
            print(search_field,'is not an authorized vehicle, if you received this in error please check the spelling and try again')
            continue
    elif menu_number == 3:
        new_listing = str(input('Add new vehicle: '))
        AllowedVehiclesList.append(new_listing)
        print('You have added "',new_listing,'" as an authorized vehicle.')
        continue
else:
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')