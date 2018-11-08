import subprocess
import requests


i = 1
#15 web = "https://www.hatebase.org/search_results/keywords=%7Cfilter_about_ethnicity=1%7Cfilter_about_nationality=%7Cfilter_about_religion=%7Cfilter_about_gender=%7Cfilter_about_sexual_orientation=%7Cfilter_about_disability=%7Cfilter_about_class=%7Cfilter_archaic=%7Cinclude_meaning=%7Cfilter_language=eng/"
#5 web = "https://www.hatebase.org/search_results/keywords=%7Cfilter_about_ethnicity=%7Cfilter_about_nationality=1%7Cfilter_about_religion=%7Cfilter_about_gender=%7Cfilter_about_sexual_orientation=%7Cfilter_about_disability=%7Cfilter_about_class=%7Cfilter_archaic=%7Cinclude_meaning=%7Cfilter_language=eng/"
#2 web = "https://www.hatebase.org/search_results/keywords=%7Cfilter_about_ethnicity=%7Cfilter_about_nationality=%7Cfilter_about_religion=1%7Cfilter_about_gender=%7Cfilter_about_sexual_orientation=%7Cfilter_about_disability=%7Cfilter_about_class=%7Cfilter_archaic=%7Cinclude_meaning=%7Cfilter_language=eng/"
#1 web = "https://www.hatebase.org/search_results/keywords%3D%7Cfilter_about_ethnicity%3D%7Cfilter_about_nationality%3D%7Cfilter_about_religion%3D%7Cfilter_about_gender%3D1%7Cfilter_about_sexual_orientation%3D%7Cfilter_about_disability%3D%7Cfilter_about_class%3D%7Cfilter_archaic%3D%7Cinclude_meaning%3D%7Cfilter_language%3Deng"
#1 web = "https://www.hatebase.org/search_results/keywords%3D%7Cfilter_about_ethnicity%3D%7Cfilter_about_nationality%3D%7Cfilter_about_religion%3D%7Cfilter_about_gender%3D%7Cfilter_about_sexual_orientation%3D1%7Cfilter_about_disability%3D%7Cfilter_about_class%3D%7Cfilter_archaic%3D%7Cinclude_meaning%3D%7Cfilter_language%3Deng"
#1 web = "https://www.hatebase.org/search_results/keywords%3D%7Cfilter_about_ethnicity%3D%7Cfilter_about_nationality%3D%7Cfilter_about_religion%3D%7Cfilter_about_gender%3D%7Cfilter_about_sexual_orientation%3D%7Cfilter_about_disability%3D1%7Cfilter_about_class%3D%7Cfilter_archaic%3D%7Cinclude_meaning%3D%7Cfilter_language%3Deng"
#2 web = "https://www.hatebase.org/search_results/keywords%3D%7Cfilter_about_ethnicity%3D%7Cfilter_about_nationality%3D%7Cfilter_about_religion%3D%7Cfilter_about_gender%3D%7Cfilter_about_sexual_orientation%3D%7Cfilter_about_disability%3D%7Cfilter_about_class%3D1%7Cfilter_archaic%3D%7Cinclude_meaning%3D%7Cfilter_language=eng/"
#web = "https://www.hatebase.org/search_results/keywords%3D%7Cfilter_about_ethnicity%3D%7Cfilter_about_nationality%3D%7Cfilter_about_religion%3D%7Cfilter_about_gender%3D%7Cfilter_about_sexual_orientation%3D%7Cfilter_about_disability%3D%7Cfilter_about_class%3D%7Cfilter_archaic%3D1%7Cinclude_meaning%3D%7Cfilter_language=eng/"
#web = "http://www.rsdb.org/full?fbclid=IwAR3DizGV9Hql3dUhB3ZkVBHKktGQ2FwnySivQVgCwzPQ22Z_mr20tDTEolk"
web = "https://en.wikipedia.org/wiki/List_of_LGBT_slang_terms"
cat = "LGBT"

while i<=1:
    f = open("html/"+cat+".html","w")
    tar = web 
    response = requests.get(tar)
    f.write(response.text)
    f.close()
    i+=1




