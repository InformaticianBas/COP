AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
print('********************************\nAutoCountry Vehicle Finder v0.1\n********************************\nPlease Enter the following number below from the following menu:\n\n1. PRINT all Authorized Vehicle\n2. Exit\n')

menu_number = int(input())
if menu_number == 1:
    print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for make in AllowedVehiclesList:
        print(make)
elif menu_number == 2:    
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
else: # Extra that I added
    print('Invalid number. Try again.')