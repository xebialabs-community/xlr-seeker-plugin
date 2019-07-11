#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import com.xhaus.jyson.JysonCodec as json
import sys

# example API connection URL https://seeker-vm.synopsys-alliances.com:8443/rest/api/latest/vulnerabilities?format=JSON&maxResults=1
params = { 'url': configuration.url }
req = HttpRequest(params)

api_url = "/rest/api/latest/vulnerabilities?format=JSON&maxResults=1"

headers = {'Accept': 'application/json', 'Authorization': 'Bearer %s' % configuration.accessToken }

# Get http response from the server
response = req.get(api_url, contentType = 'application/json', headers=headers )

logger.info('Http Response code is %s' % response.status)
# check response status code, if is different than 200 exit with error code
if response.status != 200:
    error("Couldn't establish the connection with server.", response)
    sys.exit(1)
    
