import os
import time
import requests
import json
from bs4 import BeautifulSoup
from zipfile import ZipFile
listfile = ['plugin.json', 'src\chap.js', 'src\detail.js', 'src\gen.js',
            'src\genre.js', 'src\home.js', 'src\search.js', 'src\\toc.js']
def newurl():
    print('Đang get url...')
    query = "nhattruyen"
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    # mobile user-agent
    MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
    headers = {"user-agent" : MOBILE_USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        results = str(soup.findAll('a')).split('NhatTruyen')[0].split('http://')[-1].split('</')[0]
        return results


def oldurl():
    f = open('plugin.json', 'r', encoding='UTF8')
    data = json.load(f)

    old_url = data['metadata']['source'].split('/')[2]
    return old_url


def replance_text(patchfile, old, new):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, patchfile)

    # Read in the file
    with open(filename, 'r', encoding='UTF8') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(old, new)

    # Write the file out again
    with open(filename, 'w', encoding='UTF8') as file:
        file.write(filedata)

def createzip():
    zipObj = ZipFile('plugin.zip', 'w')
    for file in listfile:
        zipObj.write(file)
    zipObj.write('icon.png')
    zipObj.close()

if __name__ == "__main__":
    old = oldurl()
    new = newurl()
    print('Old url: ' + old)
    print('New url: ' + new)
    print('Đang replance...')
    for file in listfile:
        replance_text(file, old, new)
    print('Đang đóng gói file zip...')
    createzip()
    print('done')
    time.sleep(3)