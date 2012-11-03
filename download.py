'''
Created on Nov 3, 2012

@author: raber
'''
import string
import io
import urllib2
class Download(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def get(self, streams, base_url, stream_type, stream_bitrate, outfile, dryrun=False):
        for _stream in streams:
            if _stream['Type'] == stream_type:
                stream = _stream
                break
        if not stream:
            raise Exception('stream type %s not found'%stream_type)
        
        for _bitrate in stream['Bitrates']:
            if _bitrate['Bitrate'] == stream_bitrate:
                bitrate = _bitrate
                break
        
        if not bitrate:
            raise Exception('bitrate %s not found'%stream_bitrate)
        
        print("Downloading stream type: %s bitrate: %s to: %s"%(stream_type, stream_bitrate, outfile))
        
        
        url_pattern = stream['Url']
        
                
        start_time = 0
        with io.open(outfile, 'wb') as file:
            
            for chunk in stream['Chunks']:
                formatter = string.Formatter()
                args = {"start time" : start_time, 'bitrate' : stream_bitrate }
                url = formatter.format(url_pattern, **args)
                print(base_url+url)
                if not dryrun:
                    chunk_data = urllib2.urlopen(base_url+url)
                    file.write(chunk_data.read())
                
                
                start_time += int(chunk['d'])
        
        
        