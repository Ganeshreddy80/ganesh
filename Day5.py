a=int(input("Enter The number of elements in list: "))
weights=[0]*a
for i in range(a):
    weights[i]=int(input("enter elements: "))

very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]

for w in weights:
    if(w < 0):
        invalid_entries+=[w]
    elif(w<=5):
        very_light+=[w]
    elif(w<=25):
        normal_load+=[w]
    elif(w<=60):
        heavy_load+=[w]
    else:
        overload+=[w]

name="GANESH"
L=0
for j in name:
    L+=1
PLI=L%3
affected_count=0

if(PLI==0):
    print("applied Rule A: Move all Overload items to Invalid Entries")
    for j in overload:
        affected_count+=1
        invalid_entries+=[j]
    overload=[]
elif(PLI==1):
    print("applied Rule B: Remove all Very Light items from the final plan")
    for i in very_light:
        affected_count+=1
    very_light=[]

else:
    print("applied Rule C: Keep only Normal and Heavy loads")
    for j in very_light:
        affected_count+=1
    
    for j in overload:
        affected_count+=1

    very_light=[]
    overload=[]
    invalid_entries=[]

valid_count=0

for j in very_light:
    valid_count+=1

for j in normal_load:
    valid_count+=1

for j in heavy_load:
    valid_count+=1

for j in overload:
    valid_count+=1

print("Length of Name: ",L)
print("PLI Value: ",PLI)

print("Very Light: ",very_light)
print("Normal Load: ",normal_load)
print("Heavy Load: ",heavy_load)
print("Overload: ",overload)
print("Invalid Entries: ",invalid_entries)
print("Total Valid Weights: ",valid_count)
print("Total Affected Weights: ",affected_count)
