# snapshotanalyzer2020
aws snapshot analyzer

## About

This project is demoing some boto3 and ec2 commands


## Configuring

shotanalyzer uses a aws cli configuration file 

'aws configure -- profile snapshotanalyzer'

## Running

'pipenv run "python analyzercode/snapshotanalyzer.py <command> <--project=PROJECT"'

*command* is list, start, stop
*project* is optional

