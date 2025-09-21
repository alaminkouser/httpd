# httpd

## Why is this Project?

This project uses busybox httpd as server. It is one of the lightest http server
with scripting support. And it can be deployed where busybox runs. It uses very
less resource.

## Requiremnt

- busybox

## How to run

```sh
busybox httpd -f -p 8080 -h "home"
```
