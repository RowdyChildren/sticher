Sticher
=======

a simple static site generator written in python

looks for blocks of prewritten code
looks thru the files in the prestich directory
replaces "<blockhtml src="filename" />" tags with the text of the block with the file name
puts that out in the output directory specified in the stichconf.json

stichconf.json
	contains the file paths to the files needed to be stiched, the blocks, and the output directory

stich.py
	contains the sticher class 
	reads stichconf.json

test.py
	a simple initilazion of the sticher and stiches all files found in the prestich directory.
