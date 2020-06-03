#!/bin/sh
pushd /home/ldm/routingworkflow
python gen_route_dax.py -d dax_outputs -l "https://casa-denton3.noaa.unt.edu:8091/liveEvents" -o "https://casa-denton3.noaa.unt.edu:8091/alertArchiveStart?&start=`date -d "-6minutes" +%Y-%m-%dT%H:%M:00Z`&end=`date -d "-5minutes" +%Y-%m-%dT%H:%M:00Z`&format=json" -t "https://casa-denton3.noaa.unt.edu:8091/casaAlert/flightPath" -u admin -p shabiz -b 1
popd
