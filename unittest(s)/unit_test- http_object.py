
import urllib3
import regex


__version__=0.1
url="https://raw.githubusercontent.com/Mainakdey1/pcecho-python/main/finalmodule.pyw"
connection_pool=urllib3.PoolManager()
resp=connection_pool.request("GET",url)
match_regex=regex.search(r'__version__*= *(\S+)', resp.data.decode("utf-8"))
match_regexno=float(match_regex.group(1))
print(match_regexno)