# Security headers glitch in Nginx: [headers.monster](https://www.headers.monster)

This repository includes a simple [nginx configuration](nginx/nginx.conf) which adds security headers by default.

In the location block [I include an if-statement](https://github.com/tvdhout/headers.monsters/blob/f10931d03dcca7b84de8d3d4f01f1868468749aa/nginx/nginx.conf#L92) which adds additional headers if the request is a GET request. 

As a result, all the previously added headers are removed in the browser, but not in CURL. This results in the website [scoring 100%](https://internet.nl/site/headers.monster/1489677/) on internet.nl, while in reality it does support the security headers.

The results on [securityheaders.com](https://securityheaders.com/?q=headers.monster&followRedirects=on) are correct, because they do not use CURL but some automated browser agent (like selenium)
