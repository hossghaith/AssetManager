import csv
newList={}
with open('AssetSheet.csv', newline="") as csvfile:
    read=csv.DictReader(csvfile)
    for i in read:
        newList.update(i)

# for k,v in newList.items():
#     print(v)

with open('newAssetSheet.csv','w',newline='') as newCsvFile:
    write=csv.DictWriter(newCsvFile,fieldnames=newList.keys())
    write.writeheader()
    write.writerow(newList)




#
#
#
#
#
