#!/bin/bash
# Sends a header variable X-School-User-Id with the value 98
curl -sH "X-School-User-Id: 98" "${1}"
