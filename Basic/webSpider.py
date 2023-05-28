#!/usr/bin/python3
import requests

def checkUrlList(URL):
    if URL in urlList:
        return True
    else:
        return False

def isFollowedCheck(URL):
    for entry in isFollowed.keys():
        if URL != entry:
            return False
        else:

            if isFollowed[URL] == "yes":
                return True
            else:
                return False


URLInicial = "http://192.168.60.101"
isFollowed = {}

urlList = []

#page = requests.get(URL)
#print(page.text)
#print(urlList)
urlList.append(URLInicial)
#print(urlList)
print("------")
#print(isFollowed)
#isFollowed[URL] = "yes"

#print(isFollowedCheck(URL))
#print(isFollowedCheck("http://offsec.com"))
#print(checkUrlList(URL))
#print(checkUrlList("http://www.offsec.com/"))


#print(isFollowed)

for URL in urlList:
    if isFollowedCheck(URL) != True:
        page = requests.get(URL)
        isFollowed[URL] = "yes"
        #print("agregado: "+URL)
    
    #counter=0
    start = "http://"
    end = "\">"
    for line in page.text.split("\n"):
        #counter+=1
        if 'http' in line:
            if URLInicial in line:
                if "\">" in line:
                    end = "\">"
                else:
                    end = "\" "
                sliced = line[line.index(start):line.index(end)]
                if  "\" " in sliced:
                    end = "\""
                    parsedUrl=sliced[sliced.index(start):sliced.index(end)]
                else:
                    parsedUrl=sliced

                #print(line)
                #print(line[line.index(start)])
                #print(line[line.index(end)])
                if (checkUrlList(parsedUrl) == False):
                    urlList.append(parsedUrl)
                
    #print("URLs:")
    #print(urlList)

#print("fin del loop:")   
for URL in urlList:
    print(URL)

