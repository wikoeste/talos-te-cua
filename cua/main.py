import os

from cua.common import settings
settings.init()
from cua_utils import publisher
from mrt.armory import Armory
import requests,json
import pandas as pd


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
    res     = requests.post("https://armory-sl.sco.cisco.com/web/cua/inject",data=payload,headers=hdrs)
    if res.status_code == 200:
        print("\nCUA Injection Results")
        print(f"Injected url:{urls}\nSuccessfully produced message!")
    else:
        print("\nHTTP ERR:{}".format(res.status_code))

# Read CSV column for urls exported from ACE and inject to cua
def readxls():
    filePath    = None
    fnames      = []
    count       = 1
    os.chdir(os.path.expanduser("~/Downloads"))
    cwd         = os.getcwd()
    print("Listing the Files from your Download  directory to select: ")
    #Print the list of files
    for item in os.listdir():
        if os.path.isfile(item) and not item.startswith('.') and item.endswith('.xlsx'):
            with open(item, "rb") as f:
                fbytes = f.read()  # read entire file as bytes
                print(str(count) + ". " + item)
                fnames.append(item)
                count += 1
    pick     = input("Select the File for CUA Injection from the list above : ")
    choice   = int(pick)
    choice   -= 1
    filePath = cwd + "/" + fnames[choice]
    exclfile = pd.ExcelFile(filePath)
    try:
        df       = exclfile.parse()
        colname  = 'Entry'
        coldata  = df[colname]
        print("Column Name: Entry\n",coldata)
        res = df[colname].tolist()
        return res
        #Print by index of the column
        #col      = 2
        #colindex = df.iloc[:, col]
        #print("Column Index\n", colindex)
    except FileNotFoundError:
        print(f"Error: File not found at '{filePath}'")
        return []
    except KeyError:
        print(f"Error: Column '{coldata}' not found in the sheet")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

####MAIN######
def main():
    urls = ["https://1234computers.com","http://examplemalwaredomain.com","https://phish.opendnstest.com"]
    #print(f"CUA API KEY {settings.cuakey}")
    testapi()
    #inject(urls)
    urls = readxls()
    inject(urls)
    #armory = Armory()
    #armory.inject(urls)
    #armory.query(urls[2])
######################
# Run Main As Program
if __name__ == "__main__":
    main()