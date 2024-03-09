# open additional animals csv and remove repeated rows
dd=dict()
with open('additonal_animals.csv') as f:
    for line in f:
        a=line.split('\t')
        dd[a[0]]=line

print(dd)

#print the corrected version into corrected_animals csv file
with open('corrected_animal.csv','w') as f2:
    for y in dd:
        f2.write(dd[y])



