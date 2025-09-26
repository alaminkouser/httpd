# httpd

## Why is this Project?

This project uses busybox httpd as server. It is one of the lightest http server
with scripting support. And it can be deployed where busybox runs. It uses very
less resource.

## Requiremnt

- busybox

## How to run

make sure to `chmod 700 ./home/cgi-bin/index.cgi`.

### Development

```sh
busybox httpd -f -p 8080 -h "home" -vvv
```

### Production

```sh
busybox http -f -p 127.0.0.1 -h "home"
```

The Use tools to config https.
