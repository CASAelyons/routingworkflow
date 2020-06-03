#!/usr/bin/env bash

dax_name=$(python gen_route_dax.py -d dax_outputs -l "https://emmy8.casa.umass.edu:8091/liveEvents" -o "https://emmy8.casa.umass.edu:8091/alertArchiveStart?&start=2020-04-19T11:34:00-04:00&end=2020-04-19T11:35:00-04:00&hazard=STORM_CASA_10&format=json" -t "https://emmy8.casa.umass.edu:8091/casaAlert/flightPath" -u admin -p shabiz -b 1)

echo $dax_name;
#./plan.sh ${dax_name}

