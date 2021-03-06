
__all__ = 'content_type, responses'


content_type = {
 #"*":"application/octet-stream",
 "001":"application/x-001",
 "301":"application/x-301",
 "323":"text/h323",
 "906":"application/x-906",
 "907":"drawing/907",
 "a11":"application/x-a11",
 "acp":"audio/x-mei-aac",
 ".ai":"application/postscript",
 "aif":"audio/aiff",
 "ifc":"audio/aiff",
 "iff":"audio/aiff",
 "anv":"application/x-anv",
 "asa":"text/asa",
 "asf":"video/x-ms-asf",
 "asp":"text/asp",
 "asx":"video/x-ms-asf",
 ".au":"audio/basic",
 "avi":"video/avi",
 "awf":"application/vnd.adobe.workflow",
 "biz":"text/xml",
 "bmp":"application/x-bmp",
 "bot":"application/x-bot",
 "c4t":"application/x-c4t",
 "c90":"application/x-c90",
 "cal":"application/x-cals",
 "cat":"application/vnd.ms-pki.seccat",
 "cdf":"application/x-netcdf",
 "cdr":"application/x-cdr",
 "cel":"application/x-cel",
 "cer":"application/x-x509-ca-cert",
 "cg4":"application/x-g4",
 "cgm":"application/x-cgm",
 "cit":"application/x-cit",
 "ass":"java/*",
 "cml":"text/xml",
 "cmp":"application/x-cmp",
 "cmx":"application/x-cmx",
 "cot":"application/x-cot",
 "crl":"application/pkix-crl",
 "crt":"application/x-x509-ca-cert",
 "csi":"application/x-csi",
 "css":"text/css",
 "cut":"application/x-cut",
 "dbf":"application/x-dbf",
 "dbm":"application/x-dbm",
 "dbx":"application/x-dbx",
 "dcd":"text/xml",
 "dcx":"application/x-dcx",
 "der":"application/x-x509-ca-cert",
 "dgn":"application/x-dgn",
 "dib":"application/x-dib",
 "dll":"application/x-msdownload",
 "doc":"application/msword",
 "dot":"application/msword",
 "drw":"application/x-drw",
 "dtd":"text/xml",
 "dwf":"Model/vnd.dwf",
 "dwf":"application/x-dwf",
 "dwg":"application/x-dwg",
 "dxb":"application/x-dxb",
 "dxf":"application/x-dxf",
 "edn":"application/vnd.adobe.edn",
 "emf":"application/x-emf",
 "eml":"message/rfc822",
 "ent":"text/xml",
 "epi":"application/x-epi",
 "eps":"application/x-ps",
 "eps":"application/postscript",
 "etd":"application/x-ebx",
 "exe":"application/x-msdownload",
 "fax":"image/fax",
 "fdf":"application/vnd.fdf",
 "fif":"application/fractals",
 "fo":"text/xml",
 "frm":"application/x-frm",
 ".g4":"application/x-g4",
 "gbr":"application/x-gbr",
 #"":"application/x-",
 "gif":"image/gif",
 "gl2":"application/x-gl2",
 "gp4":"application/x-gp4",
 "hgl":"application/x-hgl",
 "hmr":"application/x-hmr",
 "hpg":"application/x-hpgl",
 "hpl":"application/x-hpl",
 "hqx":"application/mac-binhex40",
 "hrf":"application/x-hrf",
 "hta":"application/hta",
 "htc":"text/x-component",
 "htm":"text/html",
 "tml":"text/html",
 "htt":"text/webviewhtml",
 "htx":"text/html",
 "icb":"application/x-icb",
 "ico":"image/x-icon",
 "ico":"application/x-ico",
 "iff":"application/x-iff",
 "ig4":"application/x-g4",
 "igs":"application/x-igs",
 "iii":"application/x-iphone",
 "img":"application/x-img",
 "ins":"application/x-internet-signup",
 "isp":"application/x-internet-signup",
 "IVF":"video/x-ivf",
 "ava":"java/*",
 "fif":"image/jpeg",
 "jpe":"image/jpeg",
 #"jpe":"application/x-jpe",
 "peg":"image/jpeg",
 "jpg":"image/jpeg",
 "jpg":"application/x-jpg",
 ".js":"application/x-javascript",
 "jsp":"text/html",
 "la1":"audio/x-liquid-file",
 "lar":"application/x-laplayer-reg",
 "tex":"application/x-latex",
 "avs":"audio/x-liquid-secure",
 "lbm":"application/x-lbm",
 "sff":"audio/x-la-lms",
 ".ls":"application/x-javascript",
 "ltr":"application/x-ltr",
 "m1v":"video/x-mpeg",
 "m2v":"video/x-mpeg",
 "m3u":"audio/mpegurl",
 "m4e":"video/mpeg4",
 "mac":"application/x-mac",
 "man":"application/x-troff-man",
 "ath":"text/xml",
 "mdb":"application/msaccess",
 "mdb":"application/x-mdb",
 "mfp":"application/x-shockwave-flash",
 "mht":"message/rfc822",
 "html":"message/rfc822",
 ".mi":"application/x-mi",
 "mid":"audio/mid",
 "idi":"audio/mid",
 "mil":"application/x-mil",
 "mml":"text/xml",
 "mnd":"audio/x-musicnet-download",
 "mns":"audio/x-musicnet-stream",
 "cha":"application/x-javascript",
 "vie":"video/x-sgi-movie",
 "mp1":"audio/mp1",
 "mp2":"audio/mp2",
 "p2v":"video/mpeg",
 "mp3":"audio/mp3",
 "mp4":"video/mpeg4",
 "mpa":"video/x-mpg",
 "mpd":"application/vnd.ms-project",
 "mpe":"video/x-mpeg",
 "peg":"video/mpg",
 "mpg":"video/mpg",
 "pga":"audio/rn-mpeg",
 "mpp":"application/vnd.ms-project",
 "mps":"video/x-mpeg",
 "mpt":"application/vnd.ms-project",
 "mpv":"video/mpg",
 "pv2":"video/mpeg",
 "mpw":"application/vnd.ms-project",
 "mpx":"application/vnd.ms-project",
 "mtx":"text/xml",
 "mxp":"application/x-mmxp",
 "net":"image/pnetvue",
 "nrf":"application/x-nrf",
 "nws":"message/rfc822",
 "odc":"text/x-ms-odc",
 "out":"application/x-out",
 "p10":"application/pkcs10",
 "p12":"application/x-pkcs12",
 "p7b":"application/x-pkcs7-certificates",
 "p7c":"application/pkcs7-mime",
 "p7m":"application/pkcs7-mime",
 "p7r":"application/x-pkcs7-certreqresp",
 "p7s":"application/pkcs7-signature",
 "pc5":"application/x-pc5",
 "pci":"application/x-pci",
 "pcl":"application/x-pcl",
 "pcx":"application/x-pcx",
 "pdf":"application/pdf",
 "pdf":"application/pdf",
 "pdx":"application/vnd.adobe.pdx",
 "pfx":"application/x-pkcs12",
 "pgl":"application/x-pgl",
 "pic":"application/x-pic",
 "pko":"application/vnd.ms-pki.pko",
 ".pl":"application/x-perl",
 "plg":"text/html",
 "pls":"audio/scpls",
 "plt":"application/x-plt",
 "png":"image/png",
 "png":"application/x-png",
 "pot":"application/vnd.ms-powerpoint",
 "ppa":"application/vnd.ms-powerpoint",
 "ppm":"application/x-ppm",
 "pps":"application/vnd.ms-powerpoint",
 "ppt":"application/vnd.ms-powerpoint",
 "ppt":"application/x-ppt",
 ".pr":"application/x-pr",
 "prf":"application/pics-rules",
 "prn":"application/x-prn",
 "prt":"application/x-prt",
 ".ps":"application/x-ps",
 #".ps":"application/postscript",
 "ptn":"application/x-ptn",
 "pwz":"application/vnd.ms-powerpoint",
 "r3t":"text/vnd.rn-realtext3d",
 "ra":"audio/vnd.rn-realaudio",
 "ram":"audio/x-pn-realaudio",
 "ras":"application/x-ras",
 "rat":"application/rat-file",
 "rdf":"text/xml",
 "rec":"application/vnd.rn-recording",
 "red":"application/x-red",
 "rgb":"application/x-rgb",
 "rjs":"application/vnd.rn-realsystem-rjs",
 "rjt":"application/vnd.rn-realsystem-rjt",
 "rlc":"application/x-rlc",
 "rle":"application/x-rle",
 "rm":"application/vnd.rn-realmedia",
 "rmf":"application/vnd.adobe.rmf",
 "rmi":"audio/mid",
 "rmj":"application/vnd.rn-realsystem-rmj",
 "rmm":"audio/x-pn-realaudio",
 "rmp":"application/vnd.rn-rn_music_package",
 "rms":"application/vnd.rn-realmedia-secure",
 "mvb":"application/vnd.rn-realmedia-vbr",
 "rmx":"application/vnd.rn-realsystem-rmx",
 "rnx":"application/vnd.rn-realplayer",
 "rp":"image/vnd.rn-realpix",
 "rpm":"audio/x-pn-realaudio-plugin",
 "sml":"application/vnd.rn-rsml",
 ".rt":"text/vnd.rn-realtext",
 "rtf":"application/msword",
 "rtf":"application/x-rtf",
 "rv":"video/vnd.rn-realvideo",
 "sam":"application/x-sam",
 "sat":"application/x-sat",
 "sdp":"application/sdp",
 "sdw":"application/x-sdw",
 "sit":"application/x-stuffit",
 "slb":"application/x-slb",
 "sld":"application/x-sld",
 "slk":"drawing/x-slk",
 "smi":"application/smil",
 "mil":"application/smil",
 "smk":"application/x-smk",
 "snd":"audio/basic",
 "sol":"text/plain",
 "sor":"text/plain",
 "spc":"application/x-pkcs7-certificates",
 "spl":"application/futuresplash",
 "spp":"text/xml",
 "ssm":"application/streamingmedia",
 "sst":"application/vnd.ms-pki.certstore",
 "stl":"application/vnd.ms-pki.stl",
 "stm":"text/html",
 "sty":"application/x-sty",
 "svg":"text/xml",
 "swf":"application/x-shockwave-flash",
 "tdf":"application/x-tdf",
 "tg4":"application/x-tg4",
 "tga":"application/x-tga",
 "tif":"image/tiff",
 "tif":"application/x-tif",
 "tiff":"image/tiff",
 "tld":"text/xml",
 "top":"drawing/x-top",
 "ent":"application/x-bittorrent",
 "tsd":"text/xml",
 "txt":"text/plain",
 "uin":"application/x-icq",
 "uls":"text/iuls",
 "vcf":"text/x-vcard",
 "vda":"application/x-vda",
 "vdx":"application/vnd.visio",
 "vml":"text/xml",
 "vpg":"application/x-vpeg005",
 "vsd":"application/vnd.visio",
 "vsd":"application/x-vsd",
 "vss":"application/vnd.visio",
 "vst":"application/vnd.visio",
 "vst":"application/x-vst",
 "vsw":"application/vnd.visio",
 "vsx":"application/vnd.visio",
 "vtx":"application/vnd.visio",
 "xml":"text/xml",
 "wav":"audio/wav",
 "wax":"audio/x-ms-wax",
 "wb1":"application/x-wb1",
 "wb2":"application/x-wb2",
 "wb3":"application/x-wb3",
 "bmp":"image/vnd.wap.wbmp",
 "wiz":"application/msword",
 "wk3":"application/x-wk3",
 "wk4":"application/x-wk4",
 "wkq":"application/x-wkq",
 "wks":"application/x-wks",
 ".wm":"video/x-ms-wm",
 "wma":"audio/x-ms-wma",
 "wmd":"application/x-ms-wmd",
 "wmf":"application/x-wmf",
 "wml":"text/vnd.wap.wml",
 "wmv":"video/x-ms-wmv",
 "wmx":"video/x-ms-wmx",
 "wmz":"application/x-ms-wmz",
 "wp6":"application/x-wp6",
 "wpd":"application/x-wpd",
 "wpg":"application/x-wpg",
 "wpl":"application/vnd.ms-wpl",
 "wq1":"application/x-wq1",
 "wr1":"application/x-wr1",
 "wri":"application/x-wri",
 "wrk":"application/x-wrk",
 ".ws":"application/x-ws",
 "ws2":"application/x-ws",
 "wsc":"text/scriptlet",
 "sdl":"text/xml",
 "wvx":"video/x-ms-wvx",
 "xdp":"application/vnd.adobe.xdp",
 "xdr":"text/xml",
 "xfd":"application/vnd.adobe.xfd",
 "fdf":"application/vnd.adobe.xfdf",
 "tml":"text/html",
 "xls":"application/vnd.ms-excel",
 "xls":"application/x-xls",
 "xlw":"application/x-xlw",
 "xml":"text/xml",
 "xpl":"audio/scpls",
 ".xq":"text/xml",
 "xql":"text/xml",
 "ery":"text/xml",
 "xsd":"text/xml",
 "xsl":"text/xml",
 "slt":"text/xml",
 "xwd":"application/x-xwd",
 "x_b":"application/x-x_b",
 "x_t":"application/x-x_t"
}



 
responses_stat = {
 100: ('Continue', 'Request received, please continue'),
 101: ('Switching Protocols',
       'Switching to new protocol; obey Upgrade header'),
 
 200: ('OK', 'Request fulfilled, document follows'),
 201: ('Created', 'Document created, URL follows'),
 202: ('Accepted',
       'Request accepted, processing continues off-line'),
 203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
 204: ('No Content', 'Request fulfilled, nothing follows'),
 205: ('Reset Content', 'Clear input form for further input.'),
 206: ('Partial Content', 'Partial content follows.'),
 
 300: ('Multiple Choices',
       'Object has several resources -- see URI list'),
 301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
 302: ('Found', 'Object moved temporarily -- see URI list'),
 303: ('See Other', 'Object moved -- see Method and URL list'),
 304: ('Not Modified',
       'Document has not changed since given time'),
 305: ('Use Proxy',
       'You must use proxy specified in Location to access this '
       'resource.'),
 307: ('Temporary Redirect',
       'Object moved temporarily -- see URI list'),
 
 400: ('Bad Request',
       'Bad request syntax or unsupported method'),
 401: ('Unauthorized',
       'No permission -- see authorization schemes'),
 402: ('Payment Required',
       'No payment -- see charging schemes'),
 403: ('Forbidden',
       'Request forbidden -- authorization will not help'),
 404: ('Not Found', 'Nothing matches the given URI'),
 405: ('Method Not Allowed',
       'Specified method is invalid for this resource.'),
 406: ('Not Acceptable', 'URI not available in preferred format.'),
 407: ('Proxy Authentication Required', 'You must authenticate with '
       'this proxy before proceeding.'),
 408: ('Request Timeout', 'Request timed out; try again later.'),
 409: ('Conflict', 'Request conflict.'),
 410: ('Gone',
       'URI no longer exists and has been permanently removed.'),
 411: ('Length Required', 'Client must specify Content-Length.'),
 412: ('Precondition Failed', 'Precondition in headers is false.'),
 413: ('Request Entity Too Large', 'Entity is too large.'),
 414: ('Request-URI Too Long', 'URI is too long.'),
 415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
 416: ('Requested Range Not Satisfiable',
       'Cannot satisfy request range.'),
 417: ('Expectation Failed',
       'Expect condition could not be satisfied.'),
 428: ('Precondition Required',
       'The origin server requires the request to be conditional.'),
 429: ('Too Many Requests', 'The user has sent too many requests '
       'in a given amount of time ("rate limiting").'),
 431: ('Request Header Fields Too Large', 'The server is unwilling to '
       'process the request because its header fields are too large.'),
 
 500: ('Internal Server Error', 'Server got itself in trouble'),
 501: ('Not Implemented',
       'Server does not support this operation'),
 502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
 503: ('Service Unavailable',
       'The server cannot process the request due to a high load'),
 504: ('Gateway Timeout',
       'The gateway server did not receive a timely response'),
 505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
 511: ('Network Authentication Required',
       'The client needs to authenticate to gain network access.'),
}