#!/usr/bin/env python3

import re 

def get_type(filename):

        server=[]
        server_type=[]

        with open(filename) as f:
                for line in f:
                        newline = line.rstrip()
                        server = newline.split('-',)
                        #print (server) 
                        if server[1] not in server_type: 
                                server_type.append(server[1])

        #print(server_type)
        server_type.sort()
        #print(server_type)
        with open(filename + ".out", "w") as outfile:
                for entry in server_type:
                        outfile.write(entry + "\n") 

        return(server_type)

def validate_infile(input_file):
	bad_types = [ "db" ] 
	sx_types = [ "aaa", "fp"]
	all_types =  bad_types + sx_types

	bad_list = []

	with open(input_file) as f:
		for line in f:
			for bad in all_types:
				my_regex = r"\w+-.?" + re.escape(bad).rstrip() + r".?-\w+"
				#print( line + "=" + my_regex)
				#print( my_regex )
				server_found = re.findall(my_regex, line, re.IGNORECASE)
				#print(server_found)
				if server_found !=  []:
					bad_list.append(server_found)

	#print(bad_list)
	return( bad_list )
					


def pickem_fromtype(tfile, sfile):
	server_found = []
	ntype = []
	server_list = []


	#s = open(sfile)
	t = open(tfile)
	
	for line in t:
		ntype.append(line)

	#for line in s:
	#	server_list.append(line)

	#print (ntype)
	#print (server_list)

	with open(sfile) as s:
		for line in s:
			for typ in ntype:
				typ.rstrip('\n')
				#my_regex = r"ash1-" + re.escape(typ) + r"-001"
				my_regex = r"\w+-" + re.escape(typ).rstrip() + r"-\w+"
				#my_regex = r"\w+-jan-\w+"
				print( line + "=" + my_regex)
				#print( my_regex )
				server_found = re.findall(my_regex, line, re.IGNORECASE)
				print(server_found)

	t.close()


#get_type("mysall") 
#pickem_fromtype("tfile", "afile")

return( validate_infile("file"))
