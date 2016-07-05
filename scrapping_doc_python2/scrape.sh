#bin/bash

#This script uses httrack to scrap any website put in SITE

SITE="https://docs.python.org/2"

httrack -w "${SITE}" -O "./python_doc" -v -s0 \
	-* \
	+${SITE}/*.html \
	+${SITE}/*php \
	+${SITE}*.asp \
	+*.css +*.js +*.jpg +*.jpeg +*.png
