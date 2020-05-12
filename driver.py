import os

cur = os.getcwd();
os.chdir(cur+"/app/templates")

# open the homepage
os.system("index.html")

print("After you have downloaded 'buyme.jpg' into images backend that you wish to SHOP, click enter...")
input()

os.chdir(cur+"/backend")

# run the reverse image searcher
os.system("rsearch.py")

print("Thanks for shopping with us!")


