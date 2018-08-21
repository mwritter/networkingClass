'''
Matthew Ritter
CS4121
Assignment 1
Due Date 08/23/18

MATPLOTLIB IS NEEDED TO RUN THIS PROGRAM.
IT IS USED TO SHOW THE DATA GRAPHICALY.
pip install matplotib
'''

# import math and pyplot
import math
from matplotlib import pyplot as plt


# Need to call for both graphs
def makeGraph():
    # Use pyplot to show and clean up data
    plt.xlabel("Packet Size In Bits")
    plt.ylabel("End to End In Seconds")
    plt.title("Packet Switching")
    # Invert the x-axis, make the graph easier to read
    plt.gca().invert_xaxis()
    # Create a legend to under stand each line
    plt.legend()

# Method to create and plot each line with correct amount of overhead


def packetSwitching(overhead=0):

    # Matplotlib needs two arrays to create a graph
    listx = []
    listy = []

    # This problem only uses kb which is 10^3 we easly make add mb or gb
    kb = math.pow(10, 3)
    # Only needed if the problem changes
    #mb = math.pow(10,6)
    #gb = math.pow(10,9)

    # Bandwith rate of 4kbps
    R = 4 * kb

    # Message of size 16kb
    L = 16 * kb

    # Number of Routers/Switches
    numberOfRouters = 2

    # Packets vary from (largest) 4kb to 2kb to 1kb ... to (smallest)125 bits
    largestPacket = (4 * kb)
    smallestPacket = 125

    # Terminal view info
    print("=======================")
    print("With overhead: ", overhead, " bits")

    # Loop to simulate packet switching segmintation
    while largestPacket >= smallestPacket:
        # Segmentation - we need to divied the total message up
        numberOfPackets = L / largestPacket
        # The number of packets and the total number of routers will give us the number we need to add to the delay
        numberOfTransmissions = numberOfPackets + numberOfRouters
        # The delay is the packetsize along with the overhead infromation (e.g. IP Addresses) divided by the bandwith (R)
        delay = (largestPacket + overhead) / R
        # With all transmissions plus the extra overhead and the extra time due to the number of routers we get end to end delay
        endToEnd = numberOfTransmissions * delay
        # We need an array with x coordinates and one with y coordinates to use matplotlib to make the line graph
        listx.append(largestPacket)
        listy.append(endToEnd)

        # Terminal view of each point
        print((largestPacket + overhead),
              "bits will have and end-to-end delay of", endToEnd)

        # The size of each packet is cut in half and pushed back through the loop
        largestPacket = largestPacket / 2

    # After the loop give pyplot each array of x's and y's, label for the legend, and markers for each point on the line
    # To draw two graphs I had to use the figure function
    plt.figure(1)
    # Plot to first figure and call makeGraph to clean up data
    plt.plot(listx, listy, label="Overhead= "+str(overhead)+"b", marker='o')
    makeGraph()
    # Set better limites to the line graph, makes it look better
    plt.gca().set_ylim([4, 6.5])
    plt.gca().set_xlim([4000, 0])
    # Second figure in plt
    plt.figure(2)
    # Plot to second figure and call makeGraph to clean up data
    plt.plot(listx, listy, label="Overhead= "+str(overhead)+"b", marker='o')
    makeGraph()
    # Give the second graph an x axis scaled logarithmically
    plt.xscale('log')

    # Terminal view delimiter
    print("=======================")


# Call packetSwitching() with each overhead 0 bits, 10 bits, 20 bits
packetSwitching()
packetSwitching(10)
packetSwitching(20)

# Finally, tell pyplot to show both graphs
plt.show()
