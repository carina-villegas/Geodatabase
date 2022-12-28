#Verification of existence and propierties
# 1. Shape in folder

import arcpy
arcpy.env.workspace=r'C:\Data\Ex_8'
fc='dams.shp'
if arcpy.Exists(fc):
    desc=arcpy.Describe(fc)
    if hasattr(desc, "name"):
        print desc.name
        print "Shape Type", desc.shapeType
        print "Reference system", desc.spatialReference.name
        print "Extension", desc.spatialReference.domain
print "DONE"

# 2. Shape in gdb

import arcpy
arcpy.env.workspace=r'C:\Data\airport.gdb'
fc='schools'
if arcpy.Exists(fc):
    desc=arcpy.Describe(fc)
    if hasattr(desc, "shapeType"):
        print "Shape Type", desc.shapeType
    print "Name of feature, ", desc.name
    print "Reference system", desc.spatialReference.name
    print "Extension", desc.spatialReference.domain
else:
    print "It does not exist"
print "DONE"

# Feature classes from a folder

import arcpy
arcpy.env.workspace=r'C:\Data\Ex_8'
fclist=arcpy.ListFeatureClasses()
for item in fclist:
    desc=arcpy.Describe(item)
print desc.name
print desc.shapeType
print desc.name, "is a", desc.shapeType, "feature class"

#Create a geodatabase from shapefiles of a folder

import arcpy
arcpy.env.workspace=r'C:\Data\ex_7'
arcpy.env.overwriteOutput=True
fc=arcpy.ListFeatureClasses()
if fc:
    for item in fc:
        arcpy.CreateFileGDB_management(r'C:\Data', "New.gdb")
        arcpy.CopyFeatures_management(item, r'C:\Data\New.gdb ')
   
print "Done"

#Getting feature classes and shape types

import arcpy
arcpy.env.workspace=r'C:\Data\Ex_8'
fc=arcpy.ListFeatureClasses()
for item in fc:
    desc=arcpy.Describe(item)
    print desc.name, " is a ", desc.datatype, " feature class."

# Features classes copied to folders which name is determined by the first letter of the feature

import arcpy
arcpy.env.workspace=r'C:\Data\Ex_8'
fc=arcpy.ListFeatureClasses()
if fc:
    for item in fc:
     desc=arcpy.Describe(item)
     name=desc.name[0]
     fd=arcpy.CreateFolder_management("C:\\Data\\Ex_8\\", name)
     fod=arcpy.Describe(fd)

     if fod.name==desc.name[0]:
        arcpy.Copy_management(desc.name, "C:\\Data\\Ex_8\\"+name+"\\"+desc.name)
print "Done"

# Projections of shape files. Collect the list of shp and prj files. If the two lists have the same lenght, 
then sort them, and compare the file names (excluding the last 4 caharacters).

import arcpy
arcpy.env.workspace=r'C:\Data\Ex_8'
fc=arcpy.ListFeatureClasses()
fl=arcpy.ListFiles()
s=[]
for item in fl:
    desc=arcpy.Describe(item)
    if desc.name[:-3]=="prj":
        print "yes"        
print "Done"

