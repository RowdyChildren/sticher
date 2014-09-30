Stitcher
=======

a simple static site generator written in python

looks for blocks of pre-written code
looks threw the files in the prestich directory
replaces `<blockhtml src="filename" />` tags with the text of the block with the file name
puts that out in the output directory specified in the stichconf.json

stichconf.json
	contains the file paths to the files needed to be stitched, the blocks, and the output directory

stich.py
	contains the stitcher class
	reads stichconf.json

test.py
	a simple initialization of the stitcher and stitches all files found in the prestich directory.
