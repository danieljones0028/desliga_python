#!/bin/bash

for i in `ps -ef | grep decisao | grep python3 | awk '{print $2}'`; do
        kill -9 $i
done