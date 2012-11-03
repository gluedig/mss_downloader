'''
Created on Nov 3, 2012

@author: raber
'''
from xml.dom.minidom import parse

class PlaylistParse(object):
    '''
    classdocs
    '''
    def __init__(self, playlist):
        '''
        Constructor
        '''
        self.dom = parse(playlist)
        
    def getStreams(self):
        output = []
        
        streams = self.dom.getElementsByTagName('StreamIndex')
        for stream in streams:
            stream_dict = dict()
            
            #stream_dict['Node'] = stream
            attrs = stream.attributes
            for i in range(0, len(attrs)):
                attr = attrs.item(i)
                stream_dict[attr.name] = attr.value
             
            bitrates = stream.getElementsByTagName('QualityLevel')
            stream_dict['Bitrates'] = []
            for bitrate in bitrates:
                bitrate_dict = dict()
                #bitrate_dict['Node'] = bitrate
                attrs = bitrate.attributes
                for i in range(0, len(attrs)):
                    attr = attrs.item(i)
                    bitrate_dict[attr.name] = attr.value
            
                stream_dict['Bitrates'].append(bitrate_dict)
            
            chunks = stream.getElementsByTagName('c')
            stream_dict['Chunks'] = []
            for chunk in chunks:
                chunk_dict = dict()
                attrs = chunk.attributes
                for i in range(0, len(attrs)):
                    attr = attrs.item(i)
                    chunk_dict[attr.name] = attr.value
            
                stream_dict['Chunks'].append(chunk_dict)
               
            output.append(stream_dict)
        
        return output

