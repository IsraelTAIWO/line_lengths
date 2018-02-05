##Show Lengths=name
##parcel=vector
##tiolengths=output vector
outputs_QGISPOLYGONSTOLINES_1=processing.runalg('qgis:polygonstolines', parcel,None)
outputs_GRASS7V.SPLIT.VERT_1=processing.runalg('grass7:v.split.vert', outputs_QGISPOLYGONSTOLINES_1['OUTPUT'],2.0,None,-1.0,0.0001,0,None)
outputs_QGISDELETEDUPLICATEGEOMETRIES_1=processing.runalg('qgis:deleteduplicategeometries', outputs_GRASS7V.SPLIT.VERT_1['output'],None)
outputs_QGISFIELDCALCULATOR_1=processing.runalg('qgis:fieldcalculator', outputs_QGISDELETEDUPLICATEGEOMETRIES_1['OUTPUT'],'Lengths',0,10.0,2.0,True,'$length',tiolengths)