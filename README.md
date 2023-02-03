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
