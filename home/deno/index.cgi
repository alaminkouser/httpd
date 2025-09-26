#!/usr/bin/env -S deno --allow-net

console.log("Content-Type: text/html\n")

fetch("https://example.com/").then((response) => {
  return response.text();
}).then((text) => {
  console.log(text);
})
