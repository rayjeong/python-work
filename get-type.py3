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


def pickem_fromtype(tfile, sfile):
	server_found = []
	ntype = []
	server_list = []
	s = open(sfile)
	t = open(tfile)
	
	for line in t:
		ntype.append(line)

	for line in s:
		server_list.append(line)

	print (ntype)
	print (server_list)
	for svr in server_list:
		#server.rstrip()
		for typ in ntype:
			#stype.rstrip()
			#print( svr + "=" + typ)
			server_found = re.findall(rf"\b.*{typ}.*", svr)
			print(server_found)

	s.close()
	t.close()


#get_type("mysall") 
pickem_fromtype("tfile", "afile")
