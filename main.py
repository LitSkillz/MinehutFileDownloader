import requests
import time
import os

authToken = input("Auth token here (Include Bearer): ")
serverId = input("Server id here: ")
profileId = input("Profile id here: ")
sessionId = input("Session id here: ")

requestHeaders = {
    "Host": "api.minehut.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Authorization": authToken,
    "x-profile-id": profileId,
    "x-session-id": sessionId,
    "Origin": "https://app.minehut.com",
    "DNT": "1,",
    "Connection": "keep-alive",
    "Referer": "https://app.minehut.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}

def ensurePath(path):
    path = "files"+path

    if not os.path.exists(path):
        os.makedirs(path)
        print("Made path",path)
        return
    print("Didn't make path",path)

def downloadFile(pathToFile):
    url = f"https://{serverId}.manager.minehut.com/file/download?files=[%22{pathToFile}%22]"
    o = requests.options(url,headers=requestHeaders,allow_redirects=True) # required
    r = requests.get(url,headers=requestHeaders,allow_redirects=True)

    with open("files"+pathToFile, 'wb') as file:
        file.write(r.content)
    print(f"Wrote {pathToFile}.")

    time.sleep(0.5)

url = f"https://api.minehut.com/file/{serverId}/list/"

def handleFolder(path):
    o = requests.options(url+path,headers=requestHeaders,allow_redirects=True) # required
    contents = requests.get(url+path,headers=requestHeaders,allow_redirects=True).json()

    for file in contents["files"]:
        if file["directory"] == True:
            ensurePath(path+"/"+file["name"])
            handleFolder(path+"/"+file["name"])
            continue
        downloadFile(path+"/"+file["name"])
        
ensurePath("")
handleFolder("")
