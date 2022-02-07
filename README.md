# Security headers bug in Nginx: [headers.monster](https://www.headers.monster)

This repository includes a simple [nginx configuration](nginx/nginx.conf) which adds security headers by default. Website: [headers.monster](https://www.headers.monster)

In one location block [I include an if-statement](https://github.com/tvdhout/headers.monster/blob/04e31cb75a74832b27ee17fd28dff5455067890f/nginx/nginx.conf#L51) which adds an additional header if the request is a GET request. 

All the previously added headers are removed when that if-statement is triggered. \
See the difference between the response headers of [/](https://headers.monster/) and [/if](https://headers.monster/if)

This can lead to developers thinking they have everything set up correctly, while this is not the case.
