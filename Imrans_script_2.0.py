import sys
from obspy import UTCDateTime #import the relevant libraries
from obspy import read_inventory
from obspy.clients.fdsn import Client
client = Client("IRIS")

def extract_info (file_path): #extracts the required information
	inv = read_inventory(file_path) #pass file path for XML file as
                                        #parameter for read_inventory
                                #initialise object inv from Inventory class
	for k,v in sorted(inv.get_contents().items()): #for loop to find number of networks
#passes through dictionary of all channels, networks, stations (sorted alphabetically).
#This loop also defines the length of the value stored in v after each stage of the for loop is complete.
    		if k == 'stations':
        		N_Stations = len(v)
    		if k == 'networks':
        		N_Networks = len(v)
	my_stations = []
	for network in range (0,N_Networks): #for loop to store [station code, latitude, and longitude]
                                        #for each station in my_stations array
    		for station in range (0,N_Stations):
        		my_stations.append ([inv[network][station].code,
                             inv[network][station].latitude,
                             inv[network][station].longitude])
	print (my_stations)
	return my_stations

def main (): #gets the file path from the command line
	file_path = sys.argv[1]
	my_stations = [] #makes sure my_stations is clear
	if len(sys.argv)== 2 : #checks there are 2 arguments (script and file path)
		my_stations = extract_info (file_path) #puts the info extracted from previous
							#function into my_stations
	else:
    		sys.exit('Incorrect number of arguments provided')
	return my_stations 

main ()
