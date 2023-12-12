#!/bin/bash
# displays the body of the response
if [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" == '200' ]; then
  curl -sL "$1"
fi
