#.SearchCursor
# List feature classes
import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
fc="airports.shp"
cursor=arcpy.da.SearchCursor(fc,["NAME"])
for row in cursor:
    print row[0]
del cursor
print "DONE"

# List field names when another field feature fullfill a specific requirement ( TOT_ENP has a greater value than 100.000).
import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
fc="airports.shp"
cursor=arcpy.da.SearchCursor(fc,["NAME", "TOT_ENP"],'"TOT_ENP">100000')
for row in cursor:
    print "Airport name: ", row[0], "TOT_ENP", row[1] #only to verify it wont be printed
del cursor
print "DONE"

# List field names when another field feature fullfill a specific requirement ( field FEATURE contains Seaplane Base).
import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
fc="airports.shp"
cursor=arcpy.da.SearchCursor(fc,["NAME", "FEATURE"],'"FEATURE"=\'Seaplane Base\'')
for row in cursor:
    print "Airport name: ", row[0]
del cursor
print "DONE"

# List field names and values when another field feature fullfill a specific requirement (field values of LOCID that are not 
#in the state AK and the field FEATURE has a value of Airport).
import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
fc="airports.shp"
cursor=arcpy.da.SearchCursor(fc,["NAME", "LOCID", "STATE", "FEATURE"],'"STATE"!=\'AK\'' and '"FEATURE"=\'Airport\'') #'"STATE"<>\'AK\''
for row in cursor:
    print "Airport name: ", row[0], "LOCID", row[1]
del cursor
print "DONE"

# Longest field name
import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
fc="airports.shp"
cursor=arcpy.da.SearchCursor(fc,["NAME"])
myList=[]
for row in cursor:
    myList.append(row[0])
print myList
longest=myList[0]
for name in myList:
    if len(name)>len(longest):
        longest=name

print longest

# Another way to identify longest field name
import arcpy
from arcpy import env
env.workspace="C:\\Data\\ex_7"
fclass="airports.shp"

cursor_red=arcpy.da.SearchCursor(fclass, ["NAME"])
for row in cursor_red:
    if len(row[0])>:
        print "The longest airport name:", row[0]
print "Done"
del cursor
print "DONE"

#List field names (airport names) of a county, and copy into a new shapefile.
import arcpy
from arcpy import env
env.workspace="C:\\Data\\ex_7"
fcInput="airports.shp"
cursor=arcpy.da.SearchCursor(fcInput,["NAME", "COUNTY"], '"COUNTY"=\'Anchorage Borough\'')
for row in cursor:
    print "Airport name: ", row[0]
    
fcOutput="aiports_OP.shp"
arcpy.Select_analysis(fcInput,fcOutput, '"COUNTY"=\'Anchorage Borough\'')

print "Done"



