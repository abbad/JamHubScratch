'''
Created on 20,Sep, 2013

@author: Abbad
'''

from xml.dom.minidom import parseString

def getIFrameSrc(iframe):
	''' function that will get Iframe src attribute value 
		an example
	<iframe width="100%" height="450" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Fplaylists%2F10659391"></iframe>
	'''
	parsedData = parseString(iframe)
	iframe = parsedData.getElementsByTagName('iframe') 
	return iframe[0].attributes['src'].value

	
	
if __name__ == "__main__":
	getIFrameSrc('<iframe width="100%" height="450" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Fplaylists%2F10659391"></iframe>')