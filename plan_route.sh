#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 DAXFILE"
    exit 1
fi

DAXFILE=$1
DIR=/home/ldm/routingworkflow

# This command tells Pegasus to plan the workflow contained in 
# dax file passed as an argument. The planned workflow will be stored
# in the "submit" directory. The execution # site is "".
# --input-dir tells Pegasus where to find workflow input files.
# --output-dir tells Pegasus where to place workflow output files.
pegasus-plan --conf $DIR/pegasus.properties.nfs \
    --dax $DAXFILE \
    --dir $DIR/submit \
    --input-dir $DIR/input \
    --sites condorpool_nfs \
    --output-site local \
    --cleanup leaf \
    --force \
    --submit
    #--cluster horizontal \
    #--cluster label \
