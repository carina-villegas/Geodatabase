# Delete the airports where the field TOT_ENP has a larger value than 100000. How many airports were deleted?
import arcpy
arcpy.env.workspace="C:\\Data\\ex_7"
fc="airports.shp"
cursor=arcpy.da.UpdateCursor(fc, ["NAME", "TOT_ENP"], '"TOT_ENP">1000000')#Name just to verify
count=0
for row in cursor:
    print row[0] 
    cursor.deleteRow()
    count+=1
print count
del cursor
print "Done"
#Create a new airport with the name New Airport and 120000 in the field TOT_ENP.
import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
fc="MyResults/airports.shp"
cursor=arcpy.da.InsertCursor(fc, ["NAME", "TOT_ENP"])
new=[]
new.append("New airport")
new.append(120000)
cursor.insertRow(new)
del cursor
print "Done"

# A variation of the previous one
from arcpy import env 
env.workspace="C:\Data\ex_7"
fc="Myresults/airports.shp"
cursor=arcpy.da.InsertCursor(fc,["NAME", "TOT_ENP", "COUNTY"])

for i in range(10):
    new_values=[]
    new_values.append('New Airport_'+str(i+1))
    new_values.append((i+1)*120000)
    new_values.append('My county')
    cursor.insertRow(new_values)
del cursor  
print "Done"

# Add a new field to the table that is a 12 long text with the name NewCode.
import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
fc="MyResults/airports.shp"
arcpy.AddField_management(fc,"NEW CODE","TEXT",12)

print "Done"

# Develop the previous exercise further to check whether the new field (specified by the user) exists or not.
import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
fc="MyResults/airports.shp"
cursor=arcpy.ListFields(fc)
fd=[]
for row in cursor:
    fd.append(row.name)
ind=1
pos=1
value=raw_input("Enter a value of the field: ")
for n in fd:
    if n==value:
        print "This exists"
        ind=pos
    pos=pos+1

else:
    arcpy.AddField_management(fc,value, "TEXT",12)#Error if I run twice since fc is unique
del row
del cursor
print "The position of this field is ", ind
print "Done"

#Write a script that adds a new field to the file roads.shp. The field name is FERRY, its type is string with a length of 5. The 
#field value is Yes if the FEATURE field has a value of Ferry otherwise No is stored in the field.
import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
fc="MyResults/roads.shp"
arcpy.AddField_management(fc,"FERRY6", "TEXT",5)
cursor=arcpy.da.SearchCursor(fc,"FEATURE")
for row in cursor:
    if row[0]=='Ferry Crossing':
        cursor=arcpy.da.UpdateCursor(fc,"FERRY6")
        for n in cursor:
            n[0]="Yes"
            cursor.updateRow(n)
    else:
        "It is not stored in the field"

del cursor
print "Done"

# List the field names of file airport.shp, than list the values of the field the user selects.Change the previous script so that only every second values are listed.
import arcpy
from arcpy import env
env.workspace="C:\\Data\\ex_7"
fc="MyResults/airports.shp"
field=arcpy.ListFields(fc)
for item in field:
    print "These are the fields of this shape: ", item.name
fd=raw_input("Please, which field name is of your interest: ")
cursor=arcpy.da.SearchCursor(fc, [fd])
vL=[]
for row in cursor:
    #print row[0]
    vL.append(row[0])
print vL[::2] 
        
del cursor
print "Done"

# List only the country names that are longer than 
10 characters
import arcpy
from arcpy import env
env.workspace="C:\\Data\\ex_7"
fc="MyResults/airports.shp"
cursor=arcpy.da.SearchCursor(fc, ["COUNTY"])
for row in cursor:
    if len(row[0])>10:
        print row[0]

# Ask the user to type a country name. Check for the existence of this country in the file.
import arcpy
arcpy.env.workspace="C:\\Data\\ex_7"
fc="MyResults/airports.shp"
fd=raw_input("Please, enter a field name ")
cursor=arcpy.da.SearchCursor(fc, ["COUNTY"])
for row in cursor:
    if row[0]==fd:
        print "This exists"
    else:
        print "It does not exist"
        
