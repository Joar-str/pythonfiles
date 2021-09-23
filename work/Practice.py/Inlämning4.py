import pandas as pd
import datetime
import matplotlib.pyplot as plt

def file_to_explore():
    '''Funktion att läsa in fil'''
    loop = True
    while loop:
        file = input('Name of file to explore:')
        try:
            sample = open(file,'r').read()
            if sample:
                
                break
        
        except IOError:
            print('There is no such file, try again!')
         
    return str(file) 




def head_menu():
    '''huvud menyn som kallar på samtliga funktioner'''
    loop = True
    while loop:
        print('Menu\n-----')
        print('1.Numeric presentation\n2.Graphic presentation\n3.Quit program')
        choise = input('Ditt val:')
        if choise.isdigit() == True:
            choise = int(choise)
            if choise == 1:
                print(number_to_show())
            elif choise == 2:
                print(confirmed_graph(input_file))
                print(recovered_graph(input_file))
                print(death_graph(input_file))
            elif choise == 3:
                print('Exiting program...\nGood bye!')
                loop = False
            else:
                print('Wrong input, please try again!')
        else:
            print('Wrong input, please try agian!')


def number_to_show():
    '''Undermeny efter huvudmenyn'''
    print('What Number should be shown?\n--------------\n1.Total\n2.Specific Country\n3.Specific time period')
    choise2 = input('Ditt val:')
    if choise2.isdigit() == True:
        choise2 = int(choise2)
        if choise2 == 1:
            print(total(input_file))
        elif choise2 == 2:
            print(specific_country(input_file))
        elif choise2 == 3:
            print(specfic_time(input_file))
        else:
            print('Wrong input, please try agian!')
    else:
        print('Wrong input, please try agian!')

def total(input_file):
    '''Funktion som beräknar totala fall'''
    try:
        data = pd.read_csv(input_file)
        Total_Deaths = sum(data['Deaths'])
        Total_Recovered = sum(data['Recovered'])
        Total_Confirmed = sum(data['Confirmed'])
        print('Total statistic overwiev\n----------\nConfirmed:' + str(Total_Confirmed), '\nDeaths:'+ str(Total_Deaths),'\nRecovered:'+ str(Total_Recovered))
        
    except:
        print('No such file exists, please try again!')
    


def specific_country(input_file):
    

    '''Funktion som ger läsaren de olika land alternativen med hjälp av en lista och printar ut totalen för det land'''
    try:
        my_list = [] 
        data = pd.read_csv(input_file, index_col = 0)
        country1 = data['Country_Region']    
        for i in country1:
            my_list.append(i)
            my_list = list(dict.fromkeys(my_list))
            

        my_list.sort()


        print('Choose the country to show statistics for.\nPossible options are:'+'\n'.join(my_list),'\n----------')   
        country_choice = str(input('Choose country:'))
        print('Statistics for',country_choice, '\n--------------')
        
        country_filter = data.Country_Region == country_choice
        data2 = data[country_filter]
        total_conf_country = sum(data2['Confirmed'])
        total_death_country = sum(data2['Deaths'])
        total_rec_country = sum(data2['Recovered'])
        if country_choice in my_list:
            print('Confirmed:'+ str(total_conf_country),'\nRecovered:'''+ str(total_rec_country),'\nDeaths:'''+ str(total_death_country))
            
        else:
            print('Country does not exist in file, try again!\n--------------')
    
    except:
        print('Wrong input try again!\n--------------')
        
       

def specfic_time(input_file):
    '''Funktion som ger läsaren möjligheten att kolla specifika datum'''
    
    try:
        loop = True
        while loop:
            print('Give the interval dates formatted as YYYY-MM-DD:')  
            data = pd.read_csv(input_file, delimiter = ',')
            data.ObservationDate = pd.to_datetime(data['ObservationDate'])  
                
            start_date = str(input('Interval start date:'))
            end_date = str(input('Interval end date:')) 

            nr_start = pd.to_datetime(start_date)
            nr_end = pd.to_datetime(end_date)

            data = data.set_index(['ObservationDate'])
            
            if nr_end > nr_start:
                Data_filter = data.loc[Nr_start : nr_end]   
                
                date_confirmed = sum(Data_filter['Confirmed'])
                date_recovered = sum(Data_filter['Recovered'])
                date_Deaths = sum(Data_filter['Deaths'])   

                print('Statistics for time period', start_date,' to', end_date)
                print('Confirmed:'+ str(date_confirmed), '\nRecovered:''' + str(date_recovered),'\nDeaths:'''+str(date_Deaths))

                loop = False

            else:
                print('Start date cannot occur after end date!')
    except: 
        print('Wrong input, try again!\n--------------')

    


def confirmed_graph(input_file):
    
    '''Visar en scatter graf för bekfrätade fall mellan 2020-02-01 till 2020-02-10'''
    
    try:
        value_list = []
        data = pd.read_csv(input_file, delimiter = ',') 
        data.ObservationDate = pd.to_datetime(data['ObservationDate']) 
        dates = pd.date_range('2020-02-01','2020-02-10', freq = 'D').strftime('%Y-%m-%d')

        for ele in dates:
            summa_1 = data.ObservationDate.isin([ele])
            slo = data[summa_1]
            co_value = sum(slo['Confirmed'])
            value_list.append(co_value)
        
        y = value_list   
        x = dates
        
        plt.figure(figsize = (10,7))
        plt.xticks(rotation = 45, size = 8)
        plt.title('Confirmed cases day by day from covid-19')
        plt.xlabel('Dates'); plt.ylabel('Confirmed cases')
        plt.scatter(x,y)
        plt.show()
    except:
        print('Wrong input try again!\n--------------')



def recovered_graph(input_file):
    
    '''Visar en scatter graf för återhämtade fall mellan 2020-02-01 till 2020-02-10'''
    
    try:

        value_list = []
        data = pd.read_csv(input_file, delimiter = ',') 
        data.ObservationDate = pd.to_datetime(data['ObservationDate']) 
        dates = pd.date_range('2020-02-01','2020-02-10', freq='D').strftime('%Y-%m-%d')

        for ele in dates:
            summa_1 = data.ObservationDate.isin([ele])
            slo = data[summa_1]
            co_value = sum(slo['Recovered'])
            value_list.append(co_value)
        
        y = value_list   
        x = dates

        plt.figure(figsize = (10,7))
        plt.xticks(rotation = 45, size = 8)
        plt.title('Recovered cases day by day from covid-19')
        plt.xlabel('Dates'); plt.ylabel('Recovered cases')
        plt.scatter(x,y)
        plt.show()
    except:
        print('Wrong input try again!\n--------------')

     
def death_graph(input_file):
    
    '''Visar en scatter graf för dödsfall mellan 2020-02-01 till 2020-02-10'''
    
    try:

        value_list = []
        data = pd.read_csv(input_file, delimiter = ',') 
        data.ObservationDate = pd.to_datetime(data['ObservationDate']) 
        dates = pd.date_range('2020-02-01','2020-02-10', freq='D').strftime('%Y-%m-%d')

        for ele in dates:
            summa_1 = data.ObservationDate.isin([ele])
            slo = data[summa_1]
            co_value = sum(slo['Deaths'])
            value_list.append(co_value)
        
        y = value_list   
        x = dates
        
        plt.figure(figsize = (10,7))
        plt.xticks(rotation = 45, size = 8)
        plt.title('Deaths day by day from covid-19')
        plt.xlabel('Dates'); plt.ylabel('Death cases')
        plt.scatter(x,y)
        plt.show()
    except:
        print('Wrong input try again!\n--------------!')    

input_file = file_to_explore()
head_menu()