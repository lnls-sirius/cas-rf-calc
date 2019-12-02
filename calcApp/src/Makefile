TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = calc
# calc.dbd will be created and installed
DBD += calc.dbd

# calc.dbd will be made up from these files:
calc_DBD += base.dbd
calc_DBD += calcSupport.dbd
calc_DBD += asSupport.dbd
calc_DBD += asyn.dbd


# Include dbd files from all support applications:
#calc_DBD += xxx.dbd

calc_LIBS += calc
calc_LIBS += autosave
calc_LIBS += asyn

# calc_registerRecordDeviceDriver.cpp derives from calc.dbd
calc_SRCS += calc_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
calc_SRCS_DEFAULT += calcMain.cpp
calc_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#calc_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
calc_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

