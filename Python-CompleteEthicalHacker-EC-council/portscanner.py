from socket import *
import optparse
from threading import *

def connScan(tgtHost,tgtPort):
    # Create socket object
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        # Connect to target host and port
        sock.connect(tgtHost,tgtPort)
        # Print open port
        print('[+]%d/tcp Open'% tgtPort)
    except:
        # Print closed port
        print('[-]%d/tcp Closed' %tgtPort)
    finally:
        # Close socket connection
        sock.close()
def portScan(tgtHost,tgtPorts):
    # Resolve target hostname to IP
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Unknown host %s " %tgtHost)
    # Resolve target IP to hostname
    try:
        tgtName = gethostbyaddr(tgtIP)
        print ("[+] Scan results for: %s" % (tgtName[0])) 
    except:    
        print ("[+] Scan results for: %s" % (tgtIP)) 
    # Set default timeout for socket connections
    setdefaulttimeout(1)
    # Iterate through target ports
    for tgtPort in tgtPorts:
        # Create a new thread for each port scan
        t = Thread(target=connScan, args=(tgtHost,int(tgtPort)))
        t.start()

def main():
    # Create option parser
    parser = optparse.OptionParser('Usage of program: ' +'-H <target host -p <target port>' )
    
    # Add options to parser
    parser.add_option('-H', dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-p',dest="tgtPort",type='string', help='specify target ports seperated by comma')
    
    # Parse command line arguments
    (options,args) = parser.parse_args()
    
    # Retrieve target host and target ports
    tgtHost= options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    
    # Check if target host and target ports are provided
    if(tgtHost == None) | (tgtPorts[0] ==None):
        print(parser.usage)
        exit(0)
    
    # Call port scan function
    portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
    main()

