import os,requests,json,re
import sys

from cua.common import settings
settings.init()
import pandas as pd
from cua_utils import publisher
from mrt.armory import Armory

# Test API access
def testapi():
    res = requests.get("https://armory-sl.sco.cisco.com/whoami",headers={"x-armory-key":settings.cuakey},verify=False)
    if res.status_code == 200:
        rj  = res.json()
        print("CUA API Test Successful!!!!\n", json.dumps(rj, indent=2))
    else:
        print("CUA API Test FAIL!!!!\n HTTP ERR:{}".format(res.status_code))

# POST / Inject
def inject(urls):
    hdrs    = {"x-armory-key":settings.cuakey}
    payload = {"url":urls}
    res     = requests.post("https://armory-sl.sco.cisco.com/web/cua/inject",data=payload,headers=hdrs,verify=False)
    if res.status_code == 200:
        print("\n===CUA Injection Results===")
        print(f"Injected url:\n{urls}\nSuccessfully injected telemetry data to CUA!")
    else:
        print("\nCUA Injection Failed! | HTTP ERR:{}".format(res.status_code))

# Read CSV column for urls exported from ACE and inject to cua
def readxls():
    filePath    = None
    fnames,res  = ([],[])
    count       = 1
    choice      = 0
    os.chdir(os.path.expanduser("~/Downloads"))
    cwd         = os.getcwd()
    print("\n\nListing the Files from "+cwd)
    print("===Type q to quit/exit the program===")
    #Print the list of files
    for item in os.listdir():
        if os.path.isfile(item) and not item.startswith('.') and not item.startswith('~$') and item.endswith('.xlsx'):
            with open(item, "rb") as f:
                print(str(count) + ". " + item)
                fnames.append(item)
                count += 1
    # User selects the excel file to parse for URLs or domains
    pick     = input("\nSelect the File for CUA Injection from the list above: ")
    if pick.isdigit():
        choice   = int(pick)
        choice   -= 1
        filePath = cwd + "/" + fnames[choice]
        exclfile = pd.ExcelFile(filePath)
        if 'sdr' in str(filePath):
            colname = 'Domain Name'
        else:
            colname = 'Entry'
        try:
            df       = exclfile.parse()
            coldata  = df[colname]
            res = df[colname].tolist()
            return res
        except FileNotFoundError:
            print(f"Error: File not found at '{filePath}'")
            return []
        except KeyError:
            print(f"Error: Column '{coldata}' not found in the sheet")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []
    elif pick == "q" or pick == "Q":
        sys.exit()
    else:
        readxls()           # if the input is not an integer than reloas the options

####MAIN######
def main():
    urls = ["https://1234computers.com","http://examplemalwaredomain.com","https://phish.opendnstest.com"]
    testapi()           # verify our access/authentication
    inject(urls)        # injects a hardcoded url list to cua
    urls = readxls()    # user selects a xls file from ace to create a url list to inject to cua
    inject(urls)        # api call to armory which injects the urls to cua
    '''
    #armory = Armory()
    #armory.inject(urls)
    #armory.query(urls[2])
    '''
######################
# Run Main As Program
if __name__ == "__main__":
    main()