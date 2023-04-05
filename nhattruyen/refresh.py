import json
from googlesearch import search
import shutil

shutil.unpack_archive("plugin.zip", '.tmp', 'zip')

files = [".tmp\src\chap.js", ".tmp\src\detail.js", ".tmp\src\gen.js", ".tmp\src\genre.js", ".tmp\src\home.js", ".tmp\src\search.js", ".tmp\src\\toc.js", ".tmp\plugin.json"]

old_url = str(json.load(open('.tmp\plugin.json', encoding='utf-8'))['metadata']['source']).replace('https:','').replace('/','')

print("Get new url ...")
for url in search("nhattruyen"):
    newurl = str(url).replace('https:','').replace('/','')
    break

for f in files:
    print("Change file " + str(f) + " ...")
    data = open(file=f, encoding='utf-8').read().replace(old_url,newurl)
    open(file=f,mode='w', encoding='utf-8').write(data)

shutil.make_archive('plugin', 'zip', '.tmp')
shutil.rmtree('.tmp')
