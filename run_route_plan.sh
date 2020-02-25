#!/usr/bin/env bash

dax_name=$(python gen_route_dax.py -d dax_outputs -l "https://emmy8.casa.umass.edu:8091/liveEvents" -o "https://hazard.hpcc.umass.edu:8091/alertArchiveOverlap?start=2020-02-04T05:55:00Z&end=2020-02-04T06:00:00Z&hazard=STORM_CASA_5&format=json" -t "https://emmy8.casa.umass.edu:8091/casaAlert/flightPath" -u admin -p shabiz)

echo $dax_name;
#./plan.sh ${dax_name}

