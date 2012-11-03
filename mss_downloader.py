#!/usr/local/bin/python2.7
# encoding: utf-8
'''
mss_downloader -- shortdesc

mss_downloader is a description

It defines classes_and_methods

@author:     user_name
        
@copyright:  2012 organization_name. All rights reserved.
        
@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

__all__ = []
__version__ = 0.1
__date__ = '2012-11-03'
__updated__ = '2012-11-03'

DEBUG = 1

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''
    
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by user_name on %s.
  Copyright 2012 organization_name. All rights reserved.
  
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        parser.add_argument(dest="paths", help="URL of MSS assets", metavar="path", nargs='+')
        
        # Process arguments
        args = parser.parse_args()
        
        paths = args.paths
        verbose = args.verbose
        base_url = 'http://mediadl.microsoft.com/mediadl/iisnet/smoothmedia/Experience/BigBuckBunny_720p.ism/'
        import playlist
        import download
        for inpath in paths:
            print(inpath)
            parser = playlist.PlaylistParse(inpath)
            streams = parser.getStreams()
            #print (streams)
            down = download.Download()
            down.get(streams, base_url, 'video', '350000', 'out1.vc1')
            
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception, e:
        if DEBUG:
            import traceback
            traceback.print_exc()
            raise(e)
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        return 2

if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-v")
    sys.exit(main())