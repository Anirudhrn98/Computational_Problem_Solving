from airit_simulation import read_Passenger_Info
from airit_simulation import main as airit_main
from airit_simulation import valid_input
from airit_simulation import Airit_simulation

def test_Passenger_Info_Reader():
    """
    Tests whether file reader funtion works as expected

    Check :If every passenger in the file is read succefully or not

    :return:    None
    """

    # Below are the list of files and total Passenger in each of them
    fileList=["passengers_very_small.txt","passengers_small.txt","passengers_large.txt"]
    PassengerCounts=[10,100,1000]

    print("Beginning Test 1 , Data Reader Check")
    print("-----------------------------------")
    # Looping through all files
    for i in range(0,len(fileList)):
        print("Testing for file : "+ fileList[i])
        print("Expected Customer count : "+str(PassengerCounts[i]))

        listOfPassengers=read_Passenger_Info(fileList[i])
        print("Customer count from file reader method : "+str(len(listOfPassengers)))
        print()

def test_missing_or_incorrect_filename():
    """
    Tests if the input file is missing or file was not provided

    Check 1 : Passess a list of file names to the funtion among
              which only one file is present in working directory

    Check 2 : Not providing file

    :return:    None
    """

    sys_argument_list=[["","smalls.txt"],[],["","large.txt"],["","some_other_text.txt"]]

    print("Beginning Test 2 , Input File Checker ")
    print("---------------------------------------")


    for argument in sys_argument_list:

        print("Checking when argument provided to commanf line was: "+str(argument))
        airit_main(argument)
        print()

def test_for_incorrect_capacity_values():
    """
    Tests if the values provided for Aircraft and gate capacities are
    postive integer values

    :return:    None
    """
    capacity=[-1,-2,-3,0,0,1.1,0.1]

    print("Beginning Test 3 , Capacity value checker ")
    print("---------------------------------------")


    for value in capacity:
        print("Capacity value provided : "+str(value))
        valid_input(str(value))
        print()

def test_gate_assemebly():
    """
    Tests how people are arranged in zones at the gate
    for various values of gate capacity

    :return:    None
    """

# Manually passing passenger info
    passenger_info=[
["Matthew Martin Phouthavong","10380","False"],["Taylor Simmons","40703","False"],
["Austin Todd Sgambati","30870","False"],
["Sparsh Lamirande","40159","False"],
["Victoria Moses","30538","False"],
["Justin Bradley Ickes","10408","False"],
["Alexander Elias Melfi","10360","False"],
["Bridget Stepanida Higgins","40095","False"],
["Andrew Benjamin Mughal","10896","True"],
["Drew Michael Peryer Jr","40851","True"],
["Simon James Dorrell","10512","True"],
["Rachel Marie Swink","30230","True"],
["Charles Carnation","30882","False"],
["Brett Michael Foley","20865","True"]]

    Gate_capacity_list=[4,5,6,7]

    print("Beginning Test 4 , Gate zone test ")
    print("--------------------------------------")

    for i in range(len(Gate_capacity_list)):
        flight = Airit_simulation(Gate_capacity_list[i], 4, passenger_info)
        flight.assembly_at_boarding_gate()
        print()
        print("Check for gate capacity : "+str(Gate_capacity_list[i]))
        print()

        print("Queue representation of Zone 1")
        print(flight.zonesBG[0])
        print("Queue representation of Zone 2")
        print(flight.zonesBG[1])
        print("Queue representation of Zone 3")
        print(flight.zonesBG[2])
        print("Queue representation of Zone 4")
        print(flight.zonesBG[3])
        print()
        print()



def main():
    test_Passenger_Info_Reader()
    test_missing_or_incorrect_filename()
    test_for_incorrect_capacity_values()
    test_gate_assemebly()

if __name__ == '__main__':
    main()

