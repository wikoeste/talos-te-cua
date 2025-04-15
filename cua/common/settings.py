import getpass,re,json,os
#from cua_utils import publisher
#from databricks.sdk import WorkspaceClient
#from databricks.sdk.runtime import dbutils

# initialize global variables
def init():
    global uname,cuakey,cuser,cpass,cuaurl,armory,ver

#take the search keyname and return the appropriate api key
def getKey(keyname):
    match     = None
    # read keys based on .profile location
    freebsd   = "/home/{}".format(uname)+"/.profile"
    osx       = "/Users/{}".format(uname)+"/.profile"
    if os.path.exists(freebsd):
        fname   = freebsd
    else:
        fname = osx
    with open(fname, 'r') as fp:
        lines = fp.read().splitlines()
        for l in lines:
            if l.startswith('#'):
                pass
            if keyname.upper() in l:
                match = l
                #print(match)
    fp.close()
    if match is not None:
        key = re.sub(r'.*KEY=','',match)   # remove the key name and = sign
        key = re.sub(r'"','',key)       # remove the quotations from the keys
        return key                      # return api key based on name
    else:
        key = keyname +" - Not found"
        return key

# Set globals
uname   = getpass.getuser()
cuakey  = getKey("armory")
ver     = "0.2"
cuaurl  = "https://cua-publisher.sl.talos.cisco.com/api/v1/cua/analysis"

# For mrt/cua libs but fail to run successfully
#cuser   = "cua"
#cpass   = "thisisthepassword"
#cpass   = dbutils.secret("dns-and-web", "cua_utils_publisher_pass")