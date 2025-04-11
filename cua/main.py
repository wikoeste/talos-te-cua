from cua.common import settings
settings.init()
from cua_utils import publisher
from mrt.armory import Armory
import requests,json


# Test API access
def testapi():
    res = requests.get("https://armory-sl.sco.cisco.com/whoami",headers={"x-armory-key":settings.cuakey},verify=False)
    if res.status_code == 200:
        rj  = res.json()
        print("CUA API Test Results:\n", json.dumps(rj, indent=2))
    else:
        print("\nHTTP ERR:{}".format(res.status_code))

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

def main():
    urls = ["https://1234computers.com","http://examplemalwaredomain.com","https://phish.opendnstest.com"]
    #print(f"CUA API KEY {settings.cuakey}")
    testapi()
    inject(urls)
    #armory = Armory()
    #armory.inject(urls)
    #armory.query(urls[2])
######################
# Run Main As Program
if __name__ == "__main__":
    main()