# astrophotography stats (APS)
APS analyses all photos under a given root and creates aggragate information per target.
It's created to summarize a year of astrophotography. 
## usage
`cd` into a separate folder of your liking and:
```
git clone https://github.com/bfv/astrophotography-stats .
pip -r requirements.txt
python main.py
```

## configuration
There is configuration is done in a file called `stats-config.toml` and is possible at two levels: 
- the directory where you're runnin `main.py` from 
- the root you interactively specify

In the first you can set:
```
[files]
defaultdir = 'd:\onedrive\_2023'
excludedirs = [ "various" ]
```
excludes are supposed to be subdir of the root. 

In the root you can specify excludes:
```
[files]
excludedirs = [ "m101_edu", "ngc6888-mosaic", "sn2023ixf" ]
```
Note: in both cases the setting are under te `[files]` section.

## target names
By default the target name is the directory name directly under the root. To override this one can add a `target.info` file in the directory:
```
[target]
name = "M101"
```

## output 
The output is CSV which can be imported in Excel. Everything is written to `stdout` so you may want to copy-paste it into a `csv` file and open that in Excel (or whatever).

# author notes:

## todo
- figure out why target.info in LeoTriplet errors

## disclaimer
This is one of first attempts to produce something in Python so probably not everything is _pythonic_ or consistent.
