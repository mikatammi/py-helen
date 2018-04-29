py-helen
========

Script for getting Helen's electricity data using Python

Proof of concept. Might be converted to library later.

Usage
-----

Use web browser of your choice to log in to Helen's Sävel Mobiili and then use developer tools to get Authorization header and Session cookie. Then replace auth and cookie variables in dumper.py script to obtained ones. Get metering point number from first part of the URL (/api/meteringpoints/0/YOUR_METERING_POINT), and replace it as well. You might also want to set your own start and end dates.
