import time
import os

black = 0
blue = 1
green = 2
aqua = 3
red = 4
purple = 5
yellow = 6
white = 7
gray = 8
lightblue = 9
lightgreen = "a"
lightaqua = "b"
lightred = "c"
lightpurple = "d"
lightyellow = "e"
brightwhite = "f"

os.system("color {0}{1}" .format(black,lightgreen))

def new():
#gather user input for new liquid
    os.system("color {0}{1}" .format(black,lightblue))
    print("LIQUID PREFERENCE")
    flavor = eval(input("Flavor(1-5): "))
    pgperc = eval(input("PG percent(whole number): "))
    vgperc = 100 - pgperc
    pgn= eval(input("Nicotine (mg/ml): "))
    ml_total = eval(input("Total volume: "))

    #needs ml to drop ratio
    ml_d = .4/15
    #subtotal of PG in ml
    mlpg_sub = (pgperc / 100) * ml_total
    
    #getting flavor percentage via "flavor level prompt"
    flavor_perc = (flavor * .04)
    fperc = flavor_perc * 100 #whole number % of flavor

    #displayable format (ml)'s
    mlflavor = flavor_perc * ml_total
    dflavor = mlflavor / ml_d 
    mlnic = pgn / (100/ml_total)
    mlpg = mlpg_sub - mlflavor - mlnic
    mlvg = ml_total - round(mlflavor,1) - round(mlnic,1) - round(mlpg,1)
    '''new/file'''#START
    os.system("color {0}{1}" .format(black,lightgreen))
    name = input("Save Name?: ") #had str(), removed
    print("\n\n")

#display mixture details
    print("Okay, here's what your looking for:\n\n")
    os.system("color {0}{1}" .format(black,lightpurple))
    print("PGN: ",round(mlnic,1),"ml",sep='')
    print("PGF: ",round(mlflavor,1),"ml(",round(dflavor)," drops)",sep='')
    print("PG: ",round(mlpg,1),"ml",sep='')
    print("VG: ",round(mlvg,1),"ml",sep='')

    if name != "":
#set filename.txt
        filename = '{0}{1}{2}{3}{4}{5}' .format(name,"_",pgperc,"-",pgn,".txt")
#set file location
        file = filename
#append results to file [new or old]
        with open(file, 'a') as output:
            output.write("____MIX____\n")
            output.write("PGn: {0}ml\n" .format(round(mlnic)))
            output.write("PGf: {0}ml, ({1} drops)\n" .format(round(mlflavor,1),round(dflavor,1)))
            output.write("PG: {0}ml\n" .format(round(mlpg,1)))
            output.write("VG: {0}ml\n" .format(round(mlvg,1)))
            output.write("____MIX_OVERVIEW____\n")
            output.write("PG/VG: {0}%/{1}%\n" .format(pgperc,vgperc))
            output.write("TOTAL ml: {0}\n" .format(ml_total))
            output.write("FLAVOR: {0}%\n" .format(fperc))
            output.write("NICOTINE: {0}mg/ml\n" .format(pgn))
            output.write("inserted on {1} at {0}\n\n\n" .format(time.strftime("%I:%M:%S"),time.strftime("%d/%m/%Y")))
        os.system("color {0}{1}" .format(black,lightgreen))
        print("saved to Desktop/notes/vapeLogs/",filename, sep='')
    '''new/file''' #END
    
    print("\n")
    

    if name != "":
        os.system("color {0}{1}" .format(black,lightgreen))
        tank = input("Add tank information?(y/n): ")
        if tank == "y":
    #gather user input for tank settings    
            os.system("color {0}{1}" .format(black,lightblue))
            watt = input("watt: ")
            ohm = input("ohms: ")
            volt = input("volts: ")
            amp = input("amps: ")
            bat1 = input("battery 1: ")
            bat2 = input("battery 2: ")
            print("\n"*2)
        #display tank details
            print("watts:",watt)
            print("ohms:",ohm)
            print("volts: ",bat1,"/",bat2,"->",volt,sep='')
            print("amps:",amp)

        #from previous file name and file location, appends tank information to file.
            with open(file, 'a') as output:
                output.write("___TANK_SETTINGS___\n")
                output.write("WATTS: {0}\n" .format(watt))
                output.write("OHMS: {0}\n" .format(ohm))
                output.write("VOLTS: {0}/{1}->{2}\n" .format(bat1,bat2,volt))
                output.write("AMPS: {0}\n" .format(amp))
                output.write("inserted on {1} at {0}\n\n\n" .format(time.strftime("%I:%M:%S"),time.strftime("%d/%m/%Y")))
                output.write("COMMENTS:\n\n\n")

    #open notepad to add comments
        comment = input("add comment?(y/n): ")
        if comment == "y":
            os.system("notepad C:/Users/katdayt/Desktop/notes/vapeLogs/{0}\n" .format(filename))
    
def tank():
    old = input("add to existing?(y/n):")
    if old == "y":
        print("LIQUID INFORMATION")
        pgperc = eval(input("What percent (whole number) PG?: "))
        pgn= eval(input("What mg/ml nicotine PG?: "))
        name = str(input("name of flavor: "))
        #set filename.txt
        filename = '{0}{1}{2}{3}{4}{5}' .format(name,"_",pgperc,"-",pgn,".txt")
        #set file location
        file = filename
        #display file info
        print("created file info for {0}" .format(filename))

    #gather info about tank
    print("\nTANK SETTINGS")
    watt = input("watt: ")
    ohm = input("ohms: ")
    volt = input("volts: ")
    amp = input("amps: ")
    bat1 = input("battery 1: ")
    bat2 = input("battery 2: ")
    print("\n"*2)

    #write info about tank to file
    if old == "y":
        with open(file, 'a') as output:
            output.write("\n\n\n")
            output.write("___TANK_SETTINGS___\n")
            output.write("WATTS: {0}\n" .format(watt))
            output.write("OHMS: {0}\n" .format(ohm))
            output.write("VOLTS: {0}/{1}->{2}\n" .format(bat1,bat2,volt))
            output.write("AMPS: {0}\n" .format(amp))
            output.write("inserted on {1} at {0}\n\n\n" .format(time.strftime("%I:%M:%S"),time.strftime("%d/%m/%Y")))
            output.write("COMMENTS:\n\n\n")
        comment = input("would you like to leave a comment?(y/n):")
        if comment == "y":
            os.system("notepad C:/Users/katdayt/Desktop/notes/vapeLogs/{0}\n" .format(filename))
    

    
    
    

loop = 1
while loop == 1:
    print("\n"*2)
    cmd = input("cmd: ")
    
    if cmd == "tank":
        tank()
    if cmd == "new":
        new()
    if cmd == "":
        exit()
