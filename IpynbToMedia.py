from os import listdir
from os.path import isfile, join
from nbconvert import HTMLExporter
 
inputDir= "ipynbFiles\\"
outputDir= "htmlFiles\\"



# Converts ipynb file to Html.
def convertToHtml(filePath):
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'
 
    (body, resources) = html_exporter.from_filename(filePath)
    return body
 
# Filter files from input dir.
onlyFiles = [f for f in listdir(inputDir) if isfile(join(inputDir, f))]
  
# filter html files
ipynbFiles = [f for f in onlyFiles if f.find('ipynb')>0]
 
mediawikiContent=""

for ipynbFile in ipynbFiles:
    filePath = inputDir + ipynbFile
    fileOutPath = outputDir + ipynbFile.replace('ipynb','html')
 
    myHtml=convertToHtml(filePath)
    mediawikiContent += '='+ipynbFile+'='
    file = open(fileOutPath,"w", encoding="utf-8") 
    htmlText = '<html>{0}</html>'.format(myHtml)
    file.write( htmlText)
    mediawikiContent += '\n{0}\n'.format(htmlText)
    file.close() 
 
# Prepare one mediawiki file for all ipynb.
file = open(outputDir+ "wiki.txt","w",, encoding="utf-8") 
file.write(mediawikiContent)
file.close()
