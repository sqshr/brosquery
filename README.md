# brosquery
This is very early days, designed to take osquery output from systems, and perform a "build review". This approach is designed to be minimally invasive to the system being reviewed, with no/minimal logic being performed there.

## To recover data for brosquery:

* Get osqueryi onto the system in question (I'm not your mother)

### Linux
```
./osqueryi .tables| while read ttable; do echo $ttable && ./osqueryi --json ".all `echo $ttable| cut -c 4-`" > ./br_output/`echo $ttable| cut -c 4-`.json ;done
```
### Windows
```
foreach($line in .\osqueryi.exe .tables) { $ttable = $line.split("=> "); if( -not ( $ttable -match 'ec2_.*' ) ){ .\osqueryi --json ".all $ttable[5]" > C:\BR\$ttable.json } }
```

## What Can It Do?
At present brosquery can:

* identify users' group memberships
* WONKY- identify out of date software
* Identify unquoted service paths
* Report on Windows security center/product status
* Flag high system uptimes
* List the listening processes on a system, with their command
* Identify potential "lateral movement" by looking for open sockets in local subnets
* Checks the DNS cache for known malware domains (pulled form github)

All of the above needs testing and refinement- I have only tested against Windows output at present.
