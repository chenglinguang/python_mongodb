#!/usr/bin/env python3

#-*-encoding:utf-8-*-


"""An example of how to connect to MongoDB"""
import sys

import pymongo
from pymongo.errors import ConnectionFailure

def main():
    """Connect to MongoDB"""
    try:
        client=pymongo.MongoClient(host="localhost",port=27017)
        print("Connected successfully")
    except ConnectionFailure as e:
        sys.stderr.write("Could now connect to MongoDB: %s" % e)
        sys.exit(1)
	#
    dbh = client.test
    for item in dbh.c1.find():
        print(item)

if __name__=="__main__":
    main()


