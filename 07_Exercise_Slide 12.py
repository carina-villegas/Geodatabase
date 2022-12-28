#Slide 11
# 7_Exercise
import arcpy
from arcpy import env
env.workspace="C:\\Data\\Ex_6"
fc=arcpy.ListFeatureClasses()
if fc:
    for item in fc:
        desc=arcpy.Describe(item)
        name=desc.name[0]
        fd=arcpy.CreateFolder_management("C:\\Data\\Ex_6\\Copy\\", name)
        fod=arcpy.Describe(fd)
        
        if name[0]==fod.name:
            arcpy.Copy_management(desc.name, "C:\\Data\\Ex_6\\Copy\\"+name+"\\"+desc.name)
            
        
    
        
print "Bye"
