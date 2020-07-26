import urllib.request, json 

#Few urls on which this is working fine
#RecipeUrl="https://www.indianhealthyrecipes.com/paneer-tikka-masala-recipe-sanjeev-kapoor/"
#RecipeUrl="https://www.maggi.in/restaurant-style-home/palak-paneer-recipe?utm_source=google&utm_medium=cpc&utm_campaign=OB~TRAFFIC_CH~SEARCH_PB~Google_TG~KWC_IT~RTB_PK~Clicks_CI~_AD~AS_CN~Maggi_MeM_Broad&gclid=CjwKCAjw0_T4BRBlEiwAwoEiAazdLeD7ae6kxZx81xAUD_vg3-ZiuSnNjFjHSa2j838mRSQofS1FsRoCNRMQAvD_BwE&gclsrc=aw.ds"
#RecipeUrl="https://www.vegrecipesofindia.com/rajma-masala-recipe-restaurant-style/"

RecipeUrl=input(">")
webS="https://ingredients.schollz.now.sh/?url="
final=webS+RecipeUrl

ing=[]
with urllib.request.urlopen(final) as url:
    data = json.loads(url.read().decode())
    dict=data["ingredients"]

#print(data["ingredients"][0]["name"])

for i in range (len(dict)):
    ing.append(data["ingredients"][i]["name"])

print(ing)
