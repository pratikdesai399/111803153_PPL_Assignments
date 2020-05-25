import time

path = r"C:\Windows\System32\drivers\etc\hosts"
rd = "127.0.0.1"

website_name = input("Enter the name of the website to block: ")
f1 = open(path,'a')
f1.write(redirect + "\t" + website)
print("The website has been blocked")
f1.close()