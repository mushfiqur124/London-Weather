
## Name: Mushfiqur Rahman


import matplotlib.pyplot as plt

def load_asn1_data(filename='LondonTemperatures.csv'):
    """
    This function loads the file `LondonTemperatures.csv` and returns a LIST of
    of temperature recods... and each element of the list is ANOTHER LIST
    that contains 13 values: the year followed by a mean temperature for each month
    We'll talk about lists formally in class in a few lectures, but maybe
    you can start guessing how they work based on what you see here...
    """
    import re

    file = open(filename, 'r')
    records = []

    for r in file.readlines():
        r = re.sub(r'[^a-zA-Z0-9.,-]+', '', r)
        records.append(r.split(','))

    return records


records = load_asn1_data()

def coldest_month(records):
    """
    Function to find which month was the coldest on record.

    :returns: A string indicating the month, year, and mean temperature of the coldest month on record.
    """


    coldest_temp = 100   # all time coldet temperature (set to an arbitrarily high number)
    coldest_year = ''    # holds the year associated with the coldest temp
    coldest_month = ''   # holds the month associated with the coldest temp


    # List with all the months, with each month name indexed from 1 - 12
    month_list = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


    for record in records:


        year = int(record[0])
        jan = float(record[1])
        feb = float(record[2])
        mar = float(record[3])
        apr = float(record[4])
        may = float(record[5])
        jun = float(record[6])
        jul = float(record[7])
        aug = float(record[8])
        sep = float(record[9])
        oct = float(record[10])
        nov = float(record[11])
        dec = float(record[12])




        # Finds the lowest temp in each year using the min function (gives you the lowest value in a list)
        current_coldest_temp = min(jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec) 


        # Compares the all time coldest temp with the lowest temp in a given year
        if current_coldest_temp < coldest_temp: 
            coldest_temp = current_coldest_temp
            coldest_year = year     

            # Because the values are represented as strings in the csv file, 
            # I had to convert the coldest temp back into a string to ask python for its index  
            # The indexes of the months in the csv correspond to the indexes of the months in month_list  
           
            coldest_month = month_list[record.index(str(coldest_temp))]


    print(coldest_month, coldest_year, "was the coldest month on record with a temperature of", coldest_temp, "degrees!")
        

coldest_month(records)






def warmest_month(records):
    """
    Function to find which month was the coldest on record.

    :returns: A string indicating the month, year, and mean temperature of the coldest month on record.
    """


    # Used the same method to complete the warmest_month function

    hottest_temp = -100  
    hottest_year = ''   
    hottest_month = ''   

    month_list = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']



    for record in records:

   
        year = int(record[0])
        jan = float(record[1])
        feb = float(record[2])
        mar = float(record[3])
        apr = float(record[4])
        may = float(record[5])
        jun = float(record[6])
        jul = float(record[7])
        aug = float(record[8])
        sep = float(record[9])
        oct = float(record[10])
        nov = float(record[11])
        dec = float(record[12])


        # Used the max() function in this case to find the hottest temp every year (returns the largest value)
        current_hottest_temp = max(jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec) 



        if current_hottest_temp > hottest_temp: 

            hottest_temp = current_hottest_temp
            hottest_year = year
            hottest_month = month_list[record.index(str(hottest_temp))]
        

    print(hottest_month, hottest_year, "was the warmest month on record with a temperature of", hottest_temp, "degrees!")


warmest_month(records)


def print_mean_annual_temperature(year, records):
    """
    Given a year, print the average temperature over that year. If there are no
    records for that year, the program should not crash - instead it should print
    a message saying the data is unavailable.
    :param year: Year for which mean temperature should be printed.
    :param records: A list of lists containing temperature data.
    """


    sum = 0

    for record in records:

        current_year = int(record[0])               # current year python is on while going through the data 

        if 1884 <= year <= 2017:
        
            if year == current_year:                # comparing to see if the year the user chose is the same as the current year python is on

                for x in range(1,13):               # uses a loop to add up all the temps from record[1] to record[12]
                    sum = sum + float(record[x])

        
                mean_temp = round(sum/12, 1)        # divides the sum by 12 to get the average temp. Then rounds the value to one decimal place
                print("The mean temperature in", year, "was", mean_temp, "degrees!")

        else: 
            print("Data not available for this year!")
            break                                   # terminates the loop if the year is not in the range 


print_mean_annual_temperature(2017, records)




# Bonus: Graphing the mean annual temps: 

def plot_annual_mean(records):

    annual_temp_list = []                        #creating a list to hold the annual mean temps 
    year = [i for i in range(1884, 2018)]        #creating a list for the years in the records (this will be the x-axis values)

     

    for record in records:                       #using a for loop to go through all the records and compute the mean temp
        
        sum = 0

        for x in range (1,13):

            sum = sum + float(record[x])
        
        mean = sum/12
        annual_temp_list.append(mean)            #adding the mean temp of year to the list


    plt.plot(year, annual_temp_list, color = "teal")                                           #setting up the x and y axes
    plt.ylabel("Average Annual Temperature\n(Degrees Celcius)", fontweight='bold')             #setting up all the axes lables and the title
    plt.xlabel("Years", fontweight='bold')
    plt.title("Mean Annual Temperature in London, Ontario", fontweight='bold')
    
    
    plt.show()



plot_annual_mean(records)








