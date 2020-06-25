# snapshotanalyzer2020
aws snapshot analyzer

## About

This project is demoing some boto3 and ec2 commands


## Configuring

shotanalyzer uses a aws cli configuration file 

'aws configure -- profile snapshotanalyzer'

## Running

'pipenv run "python analyzercode/snapshotanalyzer.py <command> <subcommand> <--project=PROJECT"'

*command* is instances snapshots volumes
*subcommand* - depends on command
*project* is optional


