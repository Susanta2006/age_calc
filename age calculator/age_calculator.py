import pyfiglet
import os
import sys
from datetime import datetime

print('''
**********************
* -------------------*
* | AGE CALCULATOR | *
* -------------------*
**********************
''')
print(" ~~~ version 1.0 ~~~~~~~~~")
print()
print('''
**********************************
* ------------------------------ *
* |Created by Mr. Susanta Banik| *
* ------------------------------ *
**********************************
''')
print()
print(''' ~~HELP CENTER:
  -------------
                    
                 OPTIONS      FULL-FORM OPTION          DESCRIPTIONS
                 
                    h             -help               : Help Command
                    n             -new calculation    : Helps to start a new calculation
                    q             -quit               : Exit
                    c             -clear              : Clear screen
''')
while True:
    print()
    a=input("[+] Enter The Option: ")
    print()
    if a=='help' or a=='h':
        print(''' ~~HELP CENTER:
  --------------
                    
                 OPTIONS      FULL-FORM OPTION          DESCRIPTIONS
                 
                    h             -help               : Help Command
                    n             -new calculation    : Helps to start a new calculation
                    q             -quit               : Exit
                    c             -clear              : Clear screen
                        ''')
        continue
    elif a=='clear' or a=='c':
        print()
        os.system('cls')
        pass
    elif a=='quit' or a=='q':
        print("[-] Exiting...")
        print("[*] Exited at: ",str(datetime.now()))
        sys.exit()
        pass
    elif a=='new' or a=='n':
        print("[+] New Calculation Started...")
        print()
        pass
        dobdt=int(input("[+] Enter Your Birth Date:-- "))
        crdt=int(datetime.now().strftime("%d"))
        dobmnt=int(input("[+] Enter Your Birth Month (0~12):-- "))
        crmnt=int(datetime.now().strftime("%m"))
        dobyr=int(input("[+] Enter Your Birth Year:-- "))
        cryr=int(datetime.now().strftime("%Y"))
        print()
        ######## MONTH OF 28, 30 AND 31 DAYS ###############
                #***************************#              #
        1 or january or January or Jan       #31 days      #
        2 or february or February or Feb     #28-29 days   #
        3 or march or March or Mar           #31 days      #
        4 or april or April or Apr           #30 days      #
        5 or may or May                      #31 days      #
        6 or june or June or Jun             #30 days      #
        7 or july or July or Jul             #31 days      #
        8 or august or August or Aug         #31 days      #
        9 or september or September or Sept  #30 days      #
        10 or october or October or Oct      #31 days      #
        11 or november or November or Nov    #30 days      #
        12 or december or December or Dec    #31 days      #
                                                           #
        ####################################################

        ########### CALCULATION #####################
                   #************#                   #       
        year=(cryr-dobyr)                           #
        yearinc=(year-1)                            #
        month=(crmnt-dobmnt)                        #
        monthinc=(10-month)                         #
        day=(crdt-dobdt)                            #
        dayinc=(31-day)                             #
        dayinc2=(30-day)                            #
        #dayneg=int(365+day)                        #
                                                    #
        #############################################
                                                
    #############  JANUARY  ########################################################################
        if month<0 and dobmnt==1:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc,"days")    
        elif month>0 and dobmnt==1 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==1 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(31+day),"days")
        elif month>0 and dobmnt==1 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==1 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(31+day),"days")
        elif month==0 and dobmnt==1 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==1 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")       
    ############ FEBRUARY ############################################################################    
        elif month<0 and dobmnt==2:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc2,"days")    
        elif month>0 and dobmnt==2 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==2 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(30+day),"days")
        elif month>0 and dobmnt==2 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==2 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(30+day),"days")
        elif month==0 and dobmnt==2 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==2 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")        
    ############  MARCH   #############################################################################  
        elif month<0 and dobmnt==3:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc,"days")    
        elif month>0 and dobmnt==3 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==3 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(31+day),"days")
        elif month>0 and dobmnt==3 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==3 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(31+day),"days")
        elif month==0 and dobmnt==3 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==3 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")       
    ############# APRIL ##############################################################################
        elif month<0 and dobmnt==4:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc2,"days")    
        elif month>0 and dobmnt==4 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==4 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(30+day),"days")
        elif month>0 and dobmnt==4 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==4 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(30+day),"days")
        elif month==0 and dobmnt==4 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==4 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")        
    ############## MAY ################################################################################
        elif month<0 and dobmnt==5:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc,"days")    
        elif month>0 and dobmnt==5 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==5 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(31+day),"days")
        elif month>0 and dobmnt==5 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==5 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(31+day),"days")
        elif month==0 and dobmnt==5 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==5 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")       
    ############## JUNE ###################################################################################
        elif month<0 and dobmnt==6:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc2,"days")    
        elif month>0 and dobmnt==6 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==6 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(30+day),"days")
        elif month>0 and dobmnt==6 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==6 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(30+day),"days")
        elif month==0 and dobmnt==6 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==6 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")      
    ############### JULY ##################################################################################
        elif month<0 and dobmnt==7:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc,"days")    
        elif month>0 and dobmnt==7 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==7 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(31+day),"days")
        elif month>0 and dobmnt==7 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==7 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(31+day),"days")
        elif month==0 and dobmnt==7 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==7 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")       
    ############### AUGUST #################################################################################    
        elif month<0 and dobmnt==8:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc,"days")    
        elif month>0 and dobmnt==8 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==8 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(31+day),"days")
        elif month>0 and dobmnt==8 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==8 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(31+day),"days")
        elif month==0 and dobmnt==8 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==8 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")
    ############### SEPTEMBER ##############################################################################
        elif month<0 and dobmnt==9:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc2,"days")    
        elif month>0 and dobmnt==9 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==9 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(30+day),"days")
        elif month>0 and dobmnt==9 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==9 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(30+day),"days")
        elif month==0 and dobmnt==9 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==9 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")        
    ############### OCTOBER #################################################################################
        elif month<0 and dobmnt==10:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc,"days")    
        elif month>0 and dobmnt==10 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==10 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(31+day),"days")
        elif month>0 and dobmnt==10 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==10 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(31+day),"days")
        elif month==0 and dobmnt==10 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==10 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")        
    ############### NOVEMBER ################################################################################
        elif month<0 and dobmnt==11:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc2,"days")    
        elif month>0 and dobmnt==11 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==11 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(30+day),"days")
        elif month>0 and dobmnt==11 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==11 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(30+day),"days")
        elif month==0 and dobmnt==11 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==11 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")        
    ############### DECEMBER #################################################################################
        elif month<0 and dobmnt==12:
            print("[*] My Age is",yearinc,"years",monthinc,"months",dayinc,"days")    
        elif month>0 and dobmnt==12 and dobdt==crdt:
            print("[*] My Age is",year,"years",month,"months","0 days")
        elif month>0 and dobmnt==12 and dobdt>crdt:
            print("[*] My Age is",year,"years",(month-1),"months",(31+day),"days")
        elif month>0 and dobmnt==12 and dobdt<crdt:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==12 and day<0:
            print("[*] My Age is",yearinc,"years","11 months",(31+day),"days")
        elif month==0 and dobmnt==12 and day>0:
            print("[*] My Age is",year,"years",month,"months",day,"days")    
        elif month==0 and dobmnt==12 and day==0:
            print("[*] My Age is",year,"years",month,"months",day,"days")
            
    ############### END OF THE CALCULATION ####################################################################



