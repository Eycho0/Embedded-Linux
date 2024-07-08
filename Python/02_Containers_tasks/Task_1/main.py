import firelink

print("choose site : ")
for i in range (len(firelink.sites)):
        
    print(" "+ str(i+1) + "-" + str(list(firelink.sites.keys())[i]) )

choice = int(input()) - 1

firelink.webbrowser.open(list(firelink.sites.values())[choice])
