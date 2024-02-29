#!/bin/bash
# Displays the body of the response
curl -s -o /dev/null -w "%{http_code}" <URL> | grep -q 200 && curl -s <URL>
