#!../../bin/linux-x86_64/calc

## You may have to change calc to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/calc.dbd"
calc_registerRecordDeviceDriver pdbbase

asSetFilename("${TOP}/db/Security.as")

## Load record instances
dbLoadRecords("${TOP}/db/Calc.db","user=carneirofc")

set_savefile_path("autosave")

# Consts
#set_pass0_restoreFile("${TOP}/autosave/Calc.sav")
#set_pass1_restoreFile("${TOP}/autosave/Calc.sav")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "10.128.255.4:7011" 2

#create_monitor_set("${TOP}/db/Calc.req", 10)
