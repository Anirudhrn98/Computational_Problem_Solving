import sys

from cs_queue import Queue
from cs_stack import Stack


class Airit_simulation:
    self = None
    __slots__ = "gate_capacity", "aircraft_capacity", "presentGC", "presentAC", "zonesBG", "zonesAC", "totalPassengers", "listOfPassengers", "passengerProcessed"

    def __init__(self, gC, aC, list_of_passengers: list):
        """
        Initializes all the values.
        :param      gC:                     Gate Capacity
        :param      aC:                     Aircraft Capacity
        :param      list_of_passengers:     List of passengers from text file
        """
        self.aircraft_capacity = aC
        self.gate_capacity = gC
        self.presentGC = 0
        self.presentAC = 0
        self.zonesBG = [Queue(), Queue(), Queue(), Queue()]
        self.zonesAC = [Stack(), Stack()]
        self.listOfPassengers = list_of_passengers
        self.totalPassengers = len(self.listOfPassengers)
        self.passengerProcessed = 0

    def assembly_at_boarding_gate(self):
        """
        Lines up the passengers at the gate in different zones till the gate capacity is reached and prints the information
        of each passenger. Uses queue data structure for this process.

        :return:    None
        """
        if self.presentGC == 0:
            print("Passengers are lining up at the gate...")

        while self.presentGC < self.gate_capacity:
            if self.totalPassengers == self.passengerProcessed:
                break
            self.zonesBG[int(self.listOfPassengers[self.passengerProcessed][1][0]) - 1].enqueue(
                self.listOfPassengers[self.passengerProcessed])
            self.print_passenger_info(self.listOfPassengers[self.passengerProcessed])
            self.presentGC += 1
            self.passengerProcessed += 1

        if self.presentGC == self.gate_capacity:
            print("The gate is full; remaining passengers must wait.", end="\n")
        if self.passengerProcessed == self.totalPassengers:
            print("The last passenger is in line!")

    def boarding_flight(self):
        """
        Boards passengers from different gate zones to the flight in order till the aircraft is full.
        Also calls the deboard function to start deboard once boarding is complete

        :return:    None
        """
        print("Passengers are boarding the aircraft...")
        zone = len(self.zonesBG) - 1

        while zone >= 0:
            if self.zonesBG[zone].is_empty():
                zone -= 1
            else:
                if self.presentAC >= self.aircraft_capacity:
                    print("The aircraft is full.")
                    break
                passengerInfo = self.zonesBG[zone].peek()
                self.zonesBG[zone].dequeue()
                self.print_passenger_info(passengerInfo)

                if passengerInfo[2] == "True":
                    self.zonesAC[1].push(passengerInfo)
                else:
                    self.zonesAC[0].push(passengerInfo)
                self.presentAC += 1
                self.presentGC -= 1
        if self.presentGC < self.gate_capacity:
            print("There are no more passengers at the gate.", end="\n")
        print("Ready for taking off ...")
        self.deboarding_flight()

    def deboarding_flight(self):
        """
        Starts the disembarking process once the destination. Passengers are stored in two stacks based on the carry on.
        The stack with passengers without carry on are disembarked first and then the other stack.
        If the passengers present at gate is zero it stops the process.

        :return:    None
        """
        print("The aircraft has landed.", end="\n")
        print("Passengers are disembarking...")
        while self.presentAC > 0:
            if not self.zonesAC[0].is_empty():
                self.print_passenger_info(self.zonesAC[0].peek())
                self.zonesAC[0].pop()
            elif not self.zonesAC[1].is_empty():
                self.print_passenger_info(self.zonesAC[1].peek())
                self.zonesAC[1].pop()

            self.presentAC -= 1
        if self.presentGC == 0 and self.passengerProcessed < self.totalPassengers:
            self.run_simulation()
        elif self.presentGC > 0:
            self.boarding_flight()
        else:
            print("Simulation Complete")

    def run_simulation(self):
        """
        calls functions to assemble the passengers at gate and then calls function to start the boarding of the flight.

        :return:    None
        """
        self.assembly_at_boarding_gate()
        self.boarding_flight()

    def print_passenger_info(self, passengerInfo):
        """
        Function to print out the passenger information

        :param      passengerInfo:      Contains the passenger information to print out
        :return:    None
        """
        print(" " + passengerInfo[0] + " ," + "ticket: " + passengerInfo[1] + " ," + "carry_on: " + passengerInfo[2])
        return


def read_Passenger_Info(file):
    """
    Reads the file line by line , stores the lines
    in a List and returns the List

    :param  file: File name containing the Passenger info
    :return     : List of passengers with their info
    """
    listOfPassengers = []

    with open(file) as f:
        for word in f:
            word = word.strip()
            listOfPassengers.append(word)
    f.close()

    listinfoseparated = []

    for Passenger in listOfPassengers:
        listinfoseparated.append(Passenger.split(','))

    return listinfoseparated


def valid_input_gc():
    """
    Function for user input error checking for gate capacity

    :return:    data :      value of gate capacity
    """
    flag = False
    valid_data = 0
    while not flag:
        data = input("Gate Capacity: ")
        check = valid_input(data)
        flag = check[0]
        valid_data = check[1]

    return valid_data


def valid_input_ac():
    """
    Function for user input error checking for aircraft capacity

    :return:    data :      value of gate capacity
    """
    flag = False
    valid_data=0
    while not flag:
        data = input("Aircraft Capacity: ")
        check=valid_input(data)
        flag=check[0]
        valid_data=check[1]

    return valid_data



def valid_input(data):
    """
    Function for user input error checking

    :return:    tuple :      if value provided is corrent and the value
    """
    try:
        data = int(data)
        if data > 0:
            return(True,data)
        else:
            print("Entered data is negative or zero ! Please try again.")
            return(False, data)
    except ValueError:
        print("Entered data of type: " + str(type(data)) + " Please try again.")
        return(False, data)


def main(args):
    """
    This is the main function. Stores all the user input values and starts simulation.

    :return:    None
    """

    if len(args) != 2:
        print("Usage: python3 airit_simulation.py {filename} ")
    else:
        try:
            passenger_list = read_Passenger_Info(args[1])
            gate_capacity = valid_input_gc()
            aircraft_capacity = valid_input_ac()
            flight = Airit_simulation(gate_capacity, aircraft_capacity, passenger_list)
            print("Beginning simulation...")
            flight.run_simulation()

        except FileNotFoundError:
            print("File not found: " + args[1])


if __name__ == '__main__':
    args=sys.argv
    main(args)
