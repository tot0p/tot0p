import os
import requests

class Project:

    def __init__(self,Name,description,Url,Stars,MostUseLa,lc,langURL):
        self.Name = Name
        self.Url = Url
        self.Stars = Stars
        self.MostUseLa = MostUseLa
        self.license = lc
        self.description = description
        r = requests.get(langURL)
        g = list(r.json().keys())
        if g != []:
            self.langs = ', '.join(g)
        else:
            self.langs = ""

user = 'tot0p'
url = "https://api.github.com/users/"+user+"/repos"
DEL_START  ="<!--TABLE-->"
DEL_END    ="<!--/TABLE-->"
n = 0
readmefile=open('README.md','r')
lines = readmefile.readlines()
readmefile.close()
start =-1
end = -1
for line in lines:
    if DEL_START in line:
        start = n
    if DEL_END in line:
        end = n
    n+=1
if start == -1 or end == -1:
    print("Error: Delimiter not found")
    exit(1)
partONe = lines[:start+1]
conttemp = lines[start+1:end]
partTwo = lines[end:]
r = requests.get(url)

repos = []
for repo in r.json():
    func = lambda : repo['license']['name'] if repo['license'] else None
    repos.append(Project(repo['name'],repo['description'],repo['html_url'],repo['stargazers_count'],repo['language'],func(),repo['languages_url']))


reposSort = sorted(repos, key=lambda x: x.Stars, reverse=True)



txt = ["| Name | Description | Languages used | NbStars | License |\n", "| --- | --- | --- | --- | --- |\n"]

for repo in reposSort[:3]:
    if repo.Name != "tot0p":
        txt.append("["+repo.Name+"]("+repo.Url+") | "+str(repo.description)+" | "+str(repo.langs)+" | "+str(repo.Stars)+" | "+str(repo.license)+" |\n")

if conttemp == txt:
    print("No new content")
    exit(0)
result = partONe + txt + partTwo
readmefile=open('README.md','w')
readmefile.writelines(result)
readmefile.close()
os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
os.system('git config --local user.name "github-actions[bot]"')
os.system('git add .')
os.system('git commit -m "nasa picture was added"')
os.system('git push')