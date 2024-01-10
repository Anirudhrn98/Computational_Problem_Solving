"""
file: escapePond.py
description: Given a maze finds out the escape route from every block
language: python3

author: Anirudh Narayanan, an9425@g.rit.edu
author: Vineet Singh     , vs9779@rit.edu
"""
import math
import sys

from graph import Graph


class escapePond:
    """
    The escapepond class consists of:
    :slot filename: the name of the source file (string)
    :slot height: height of the maze
    :slot width: width of the maze
    :slot MazeGraph: Graph which stores the maze
    :slot rockList: List of rock locations on the maze
    :slot escapeRow: Row which contains the escape location from the maze
    :slot outputDict: Dictionary storing all the outputs depending on number of moves required
    :slot escapeNode: The escape location from the maze
    """
    __slots__ = "filename", "height", "width", "MazeGraph", "rockList", "escapeRow", "outputDict", "escapeNode", "nodeschecked", "rocks_count"

    def __init__(self, filename):
        """
        Initializes all the values
        :param filename: The input file.
        """
        self.MazeGraph = Graph()
        self.rockList = []
        self.__parseInputFile(filename)
        self.outputDict = {}
        self.nodeschecked = 0
        self.rocks_count = 0

    def __parseInputFile(self, filename: str):
        """
        Reads and stores the values from input file
        :param filename: the input file
        """
        rowNum = 0
        with open(filename) as f:
            heightR, widthR, escapeRowR = f.readline().split()  # Stores the height, width and escape row of the maze
            self.height, self.width, self.escapeRow = int(heightR) - 1, int(widthR) - 1, int(escapeRowR)

            for row in f:
                readRow = row.split()

                # Cross checking the maze dimensions with dimensions provided
                if len(readRow)!=(self.width + 1):
                    print("Input width does not match the maze provided")
                    sys.exit(0)

                # Iterating through the maze and creating graphs
                for col in range(0, self.width + 1):
                    self.MazeGraph.addVertex(str(rowNum) + " " + str(col))
                    if readRow[col] == '*':
                        self.rockList.append(str(rowNum) + " " + str(col))  # Adds rocks(blocks)
                rowNum += 1

        if rowNum != (self.height + 1):
            print("Input height does not match the maze provided")
            sys.exit(0)

        self.escapeNode = self.MazeGraph.getVertex(str(self.escapeRow) + " " + str(self.width))  # Stores the escape vertex of the maze

    def getPathEnds(self, node_id):
        """
        Finds the  end node for each path of each node in the maze
        :param node_id: Node for which the end nodes will be returned
        :return: the end point of each path for a node
        """
        x, y = self.string_to_tuple(node_id)

        topEnd = (0, y)
        bottomEnd = (self.height, y)
        leftEnd = (x, 0)
        rightEnd = (x, self.width)

        for rock in self.rockList:
            rock_x, rock_y = self.string_to_tuple(rock) # Stores the coordinates of the rock on the maze
            if rock_x == x:
                if rock_y < y and rock_y >= leftEnd[1]:
                    leftEnd = (x, rock_y + 1)  # Updates the left end point if a rock is present in the path
                elif rock_y > y and rock_y <= rightEnd[1]:
                    rightEnd = (x, rock_y - 1)  # Updates the right end point if a rock is present in the path

            if rock_y == y:
                if rock_x < x and rock_x >= topEnd[0]:
                    topEnd = (rock_x + 1, y)  # Updates the top end point if a rock is present in the path
                elif rock_x > x and rock_x <= bottomEnd[0]:
                    bottomEnd = (rock_x - 1, y)  # Updates the bottom end point if a rock is present in the path

        return topEnd, bottomEnd, leftEnd, rightEnd

    def connectMazeBlocks(self):
        """
        Connects the maze nodes to it's neighbouring nodes
        """
        for node in self.MazeGraph.getVertices():
            possibleConnects = self.getPathEnds(node)

            for connections in possibleConnects:
                conenctionStr = self.tuple_to_string(connections)
                # self.MazeGraph.addEdge(node, conenctionStr)
                if conenctionStr != node:
                    self.MazeGraph.addEdge(node, conenctionStr)

    def solveMaze(self):
        """
        Finds the number of steps each node requires to exit the maze.
        """
        for rock in self.rockList:
            self.rocks_count += 1
            if rock == self.escapeNode.id:
                print("Exit Blocked. Please check the maze.")

        self.outputDict["No path: "] = []
        for node in self.MazeGraph:
            if node.id not in self.rockList:  # Does not check for nodes that have a rock
                steps = self.findShortestPath(node, self.escapeNode)

                if steps is None:
                    steps = ""

                stepsCount = len(steps)

                # Formatting to required format
                formattedNode = self.string_to_tuple(node.id[::-1])

                # Block at escape node escapes in one step
                if node.id == self.escapeNode.id:
                    stepsCount += 1
                if stepsCount == 0:
                    self.outputDict["No path: "].append(formattedNode)  # adds nodes that do not a have exit from maze
                    self.nodeschecked += 1
                elif str(stepsCount - 1) in self.outputDict:
                    self.outputDict[str(stepsCount - 1)].append(formattedNode)  # add node if key is already present in the dictionary
                    self.nodeschecked += 1
                else:
                    self.outputDict[str(stepsCount - 1)] = [formattedNode]  # creates new key and stores nood if key is not present in the dictionary
                    self.nodeschecked += 1

    def findShortestPath(self, start, end):
        """
        Find the shortest path, if one exists, between a start and end vertex
        :param start : the start vertex
        :param end : the destination vertex
        :return: A list of Vertex objects from start to end, if a path exists,
            otherwise None
        """
        # Using a queue as the dispenser type will result in a breadth first
        # search
        queue = [start]

        # The predecessor dictionary maps the current Vertex object to its
        # immediate predecessor.  This collection serves as both a visited
        # construct, as well as a way to find the path
        predecessors = {start: None}

        # Loop until either the queue is empty, or the end vertex is encountered
        while len(queue) > 0:
            current = queue.pop(0)
            if current == end:
                break
            for neighbor in current.getConnections():
                if neighbor not in predecessors:  # if neighbor unvisited
                    predecessors[neighbor] = current  # map neighbor to current
                    queue.append(neighbor)  # enqueue the neighbor

        # If the end vertex is in predecessors a path was found
        if end in predecessors:
            path = []
            current = end
            while current != start:  # loop backwards from end to start
                path.insert(0, current)  # prepend current to the path list
                current = predecessors[current]  # move to the predecessor
            path.insert(0, start)
            return path
        else:
            return None

    def tuple_to_string(self, t):
        """
        Returns the string format of the vertex
        :param t: Tuple form of the vertex
        """
        return str(t[0]) + " " + str(t[1])

    def string_to_tuple(self, s):
        """
        Returns the tuple format of the vertex
        :param s: String format of the vertex
        """
        parse = s.split()
        return int(parse[0]), int(parse[1])

    def print(self):
        """
        Prints the output according to the number of moves taken to reach exit
        """
        for i in range(1, len(self.outputDict)):
            pos = str(i)
            print(pos + ": ", end="")
            print(self.outputDict[pos])
        print("No path: ", end="")

        print(self.outputDict["No path: "])  # Prints the vertex with no paths to exit.

        if (self.nodeschecked) == (((self.height+1) * (self.width+1)) - self.rocks_count):
            print("All nodes have been checked for escape from Maze" )

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 escapePond.py maze.txt')
        return

    maze = escapePond(sys.argv[1])

    #Connects graph vertices to neighbours
    maze.connectMazeBlocks()

    # Solves the maze
    maze.solveMaze()

    #Prints output
    maze.print()

if __name__ == '__main__':
    main()
