import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex07"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    desc = arcpy.da.Describe(fc)
    print(f'{desc["baseName"]}: {desc["shapeType"]}')
