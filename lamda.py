import xml.etree.ElementTree as Xet 
import pandas as pd 
  
cols = ["MasterPath", "InFiles", "Processed", "Exception", "Logs"] 
rows = [] 
  
# Parsing the XML file 
xmlparse = Xet.parse('sample.xml') 
root = xmlparse.getroot() 
for i in root: 
    MasterPath = i.find("MasterPath").text 
    InFiles = i.find("InFiles").text 
    Processed = i.find("Processed").text 
    Exception = i.find("Exception").text 
    Logs = i.find("Logs").text 
  
    rows.append({"MasterPath": MasterPath, 
                 "InFiles": InFiles, 
                 "Processed": Processed, 
                 "Exception": Exception, 
                 "Logs": Logs}) 
  
df = pd.DataFrame(rows, columns=cols) 
  
# Writing dataframe to csv 
df.to_csv('output.csv') 