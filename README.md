# Security headers bug in Nginx: [headers.monster](https://www.headers.monster)

This repository includes a simple [nginx configuration](nginx/nginx.conf) which adds security headers by default. Website: [headers.monster](https://www.headers.monster)

In the location block [I include an if-statement](https://github.com/tvdhout/headers.monsters/blob/f10931d03dcca7b84de8d3d4f01f1868468749aa/nginx/nginx.conf#L92) which adds an additional header if the request is a GET request. 

All the previously added headers are removed when that if-statement is triggered. 

This can lead to developers thinking they have everything set up correctly, while this is not the case.
