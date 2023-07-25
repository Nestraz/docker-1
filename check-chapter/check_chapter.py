import requests

print("Request has been imported")

r = requests.get("http://www.volonte-d.com/", verify=False)
print("Requete faite")

is_new_chapter_released = "chapitre 1088" in str(r.content).lower()

if is_new_chapter_released:
    print("Chapitre 1088 dispo")
else: 
    print("Chapitre 1088 pas dispo")