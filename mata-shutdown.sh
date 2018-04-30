#!/bin/bash

for i in `ps -ef | grep shutdown | grep python3 | awk '{print $2}'`; do
        kill -9 $i
done