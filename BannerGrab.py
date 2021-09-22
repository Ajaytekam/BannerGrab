#!/usr/bin/python3  

import subprocess 
import re
import argparse 

# Sucess : return Banner | Failure : return None
def GrepBanner(Domain, verbose=True):
    COMMAND = "curl -sSL -I {} -m 10".format(Domain)
    try:
        Result = subprocess.run(COMMAND, shell=True, check=True, capture_output=True, text=True)
        AllBanner = Result.stdout.split("\n\n")
        for i in AllBanner:
            if re.search('HTTP/1.1 200 OK', i) or re.search('HTTP/2 200', i):
                return i
    except:
        try:
            tDomain = "www."+Domain
            COMMAND = "curl -sSL -I {} -m 10".format(tDomain)
            Result = subprocess.run(COMMAND, shell=True, check=True, capture_output=True, text=True)
            AllBanner = Result.stdout.split("\n\n")
            for i in AllBanner:
                if re.search('HTTP/1.1 200 OK', i) or re.search('HTTP/2 200', i):
                    return i
        except subprocess.CalledProcessError as e:
            if verbose:
                print("[-] Error During Banner Grabbing")
                print(e.output)
            return None 
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="Domain name to Grep Banner")
    parser.add_argument("-o", "--output",help="Output file name to store output")
    args = parser.parse_args()
    if args.domain: 
        DataOP = GrepBanner(args.domain)
        print(DataOP)
        if args.output:
            open(args.output, "w").write(DataOP+"\n")
    else:
        print("+=+=+=+=+=+==+=+=+=+=+")
        print("# Banner Grep Script #")
        print("# By : sec-art.net   #")
        print("+=+=+=+=+=+==+=+=+=+=+\n")
        parser.print_help()

