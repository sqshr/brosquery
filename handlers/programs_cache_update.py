import requests,json,os

outdir="../cache/"

headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'Referrer': 'github.com'  # This is another valid field
                }
url = 'https://api.github.com/repos/microsoft/winget-pkgs/git/trees/master'
response = requests.get(url, headers=headers)

jsondata = response.json()
print(jsondata)
shahash = ""
for item in jsondata['tree']:
    if item['path'] == "manifests":
        shahash = item['sha']

url = "https://api.github.com/repos/microsoft/winget-pkgs/git/trees/"+shahash+"?depth=1"
response = requests.get(url, headers=headers)

jsondata = response.json()
applist = jsondata['tree']
f = open(os.path.join(outdir,"applist.cache"),"w")
f.write(str(applist))
f.close()


for item in applist:
    character = item['path']
    url = item['url']+"?recursive=1"
    response = requests.get(url, headers=headers)
    jsondata = response.json()
    f = open(os.path.join(outdir,character+".appcache"),"w")
    f.write(str(jsondata))
    f.close()



