import getpass,re,json,os
from cua_utils import publisher
#from databricks.sdk import WorkspaceClient
#from databricks.sdk.runtime import dbutils

# initialize global variables
def init():
    global uname,cuakey,cuser,cpass,cuaurl,armory

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

#cuser   = "cua"
#cpass   = "thisisthepassword"
#cpass   = dbutils.secret("dns-and-web", "cua_utils_publisher_pass")

cuaurl  = "https://cua-publisher.sl.talos.cisco.com/api/v1/cua/analysis"
armory  = '"MnwxOjB8MTA6MTc0NDIyMzA5OXwxMTphcm1vcnktY2VydHwzNDQ6VkdOSmQxRXlVVE5zTkdVMFRtcDFOU3RPZG05aWJEQmtVbEZzYUhOamNDczJRVkptVDBSSGVFaEpOMVJFU0djMU5YaDRlbW95WXl0V1lWcG9Va3B1VkRKaEx5dHdkVVZGVW5rMVRpdG9kVnB1VERGMVZIaDJlVWxZUTNaaU5IcENMMU5NY0VFelZ5c3lMMlZEVVVRemQyczBkM2c1VFROVU0xTlhZM1YzVWxKcFFrTXhValo0Y2pjdk1sZExkM0JsTUZkVmVYb3dZamQwU1djMWNVdEZaV0p0YXpneVVqVkxabW81S3prelQwWjBhbEI0YlZwcmVXZHZWazVHTDNsSVFrOU9TMEl5UTJ0VWFYZEtheXRWVUhKbWR5dGFZMWxPZFdZNE1uY3dkRTlYYlVKU2JrSklVMlk0YXpGblRXUm9RM3AwWW1aelUxVjVNbEJHZVdkUlp3PT18NDNhMTJkZDRlYjM5OGM2NmQ5ZjA0ZWIyNjdjYTY0NmEwNTUwMjdmZWQ2ZTY3ZjU3N2I2NTQxYjhiNmEzNGYxYg=="'

