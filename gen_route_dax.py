#!/usr/bin/env python

import sys
import os
import pwd
import time
import requests
import json, geojson, time, socket, subprocess, pytz, certifi, urllib3
from Pegasus.DAX3 import *
from datetime import datetime
from argparse import ArgumentParser

CASA_AUTH = ("admin","shabiz")

class routingWorkflow(object):
    #def __init__(self, outdir, queryURL, usrname, password):
    def __init__(self, outdir, featurename):
        self.outdir = outdir
        self.featurename = featurename
        #self.queryURL = queryURL
        #self.usrname = usrname
        #self.password = password

    def generate_dax(self):
        
        ts = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
        dax = ADAG("casa_routing_wf-%s" % ts)
        dax.metadata("name", "CASA Routing")
        print ("casa_routing_wf-%s" % ts)
        #print ("endpoint %s" % ep)
        
        routing_configfile = File("route_plan.cfg")
        routing_job = Job("route_plan")
        routing_job.addArguments("-c", routing_configfile);
        routing_job.addArguments("-n", self.featurename);
        routing_job.uses(routing_configfile, link=Link.INPUT)

        # Write the DAX file
        daxfile = os.path.join(self.outdir, dax.name+".dax")
        dax.writeXMLFile(daxfile)
        print daxfile

    def generate_workflow(self):
        # Generate dax
        self.generate_dax()

if __name__ == '__main__':
    parser = ArgumentParser(description="Flight Path Routing Workflow")
    parser.add_argument("-f", "--flights", metavar="FLIGHT_QUERY_URL", type=str, help="URL to query flights", required=True)
    #parser.add_argument("-u", "--usrname", metavar="USR", type=str, help="username for query authentication", required=True)
    #parser.add_argument("-p", "--password", metavar="PASS", type=str, help="password for query authentication", required=True)
    parser.add_argument("-o", "--outdir", metavar="OUTPUT_LOCATION", type=str, help="DAX Directory", required=True)
    args = parser.parse_args()
    outdir = os.path.abspath(args.outdir)

    if not os.path.isdir(args.outdir):
        os.makedirs(outdir)
    url = args.flights
    
    response = requests.get(url, auth=CASA_AUTH, verify=True)
    if response.status_code == 200:
        liveEvents = geojson.loads(response.content)
    
    for feature in liveEvents['features']:
        #all flights will be linestrings and vice versa for now... eventually read a flight property
        if feature['geometry']['type'] == 'LineString':
            featurename = feature['properties']['eventName']
            print featurename
            workflow = routingWorkflow(outdir,featurename)
            workflow.generate_workflow()

