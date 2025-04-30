# Opens and writes AllowedVehicleList file
AllowedVehiclesList =  open("AllowedVehiclesList.txt", "w")
AllowedVehiclesList.write('Ford F-150\nChevrolet Silverado\nTesla CyberTruck\nToyota Tundra\nRivian R1T\nRam 1500\n')
AllowedVehiclesList.close()

# Prints the prompt
def prompt():
    print('********************************\nAutoCountry Vehicle Finder v0.3\n********************************\nPlease Enter the following number below from the following menu:\n\n1. PRINT all Authorized Vehicle\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. DELETE Authorized Vehicle\n5. Exit')

exit_number = 5
menu_number = 0
while menu_number != exit_number:
    prompt()
    menu_number = int(input())
    if menu_number == 1:
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:\n')
        with open("AllowedVehiclesList.txt", "r+") as vehiclelist:
            filecontent = vehiclelist.read()
        print(filecontent)
        continue
    elif menu_number == 2:
        search_field = str(input('Vehicle Search: '))
        with  open("AllowedVehiclesList.txt", "r") as vehiclelist:
            searchcontent = vehiclelist.read()
            if search_field in searchcontent:
                print(search_field,'is an authorized vehicle.')
            else:
                print(search_field,'is not an authorized vehicle, if you received this in error please check the spelling and try again')
        continue
    elif menu_number == 3:
        new_listing = str(input('Add new vehicle: '))
        with open("AllowedVehiclesList.txt", "a") as vehiclelist:
            vehiclelist.write(new_listing + '\n')
        print('You have added "'+ new_listing +'" as an authorized vehicle.')
        continue
    elif menu_number == 4:
        remove_listing = str(input('Remove vehicle: '))
        confirmation = str(input('Are you sure you want to remove "' + remove_listing + '" from the Authorized Vehicles List? \n'))
        if confirmation.lower() == 'yes': # Learned about lower function using online resources
            with open("AllowedVehiclesList.txt", "r") as vehiclelist:
                removecontent = vehiclelist.readlines()
            with open("AllowedVehiclesList.txt", "w") as vehiclelist:
                for vehicle in removecontent:
                    if vehicle.strip() != remove_listing: # Learned about strip() online which removes the \n
                        vehiclelist.write(vehicle)
            print('You have REMOVED "'+ remove_listing +'" an authorized vehicles.')
        elif confirmation.lower() == 'no':
            print('')
        else:   # Extra that I added
            print('Invalid response')
    elif menu_number == 5:
        continue
    elif menu_number > 5: # Extra that I added
        print('Wrong number')
        continue
else:
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')