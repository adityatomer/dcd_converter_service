import mdtraj as md
import numpy as np


def getArgs(argv):
    infile=None
    outfile=None
    topologyFile=None
    try:
        opts, args = getopt.getopt(argv,"i:t:o:",["inFile","topologyFile","outputFile"])
    except getopt.GetoptError:
        print('convert.py -i <input dcd file> -t<topology file> -o <output file>') 
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-i", "--infile"):
            infile = arg
        elif opt in ("-t","--topologyFile"):
        	topologyFile=arg
        elif opt in ("-o", "--outfile"):
            outfile = arg
    return infile,topologyFile,outfile


main(argv){
	infile,topologyFile,outfile=getArgs(argv)
	# filename='/Users/adityatomer/Desktop/523/convert/sample_dcd.dcd'
	# t = md.load_dcd(,top=None, stride=None, atom_indices=None, frame=None)
	# t=md.load_dcd(filename,None, None, None, None)
	t=md.load_dcd(infile, top=topologyFile)
	nparray=t.xyz
	xyz=np.multiply(nparray,10)
	print xyz	
}

if __name__ == '__main__':
	main(sys.argv[1:])

