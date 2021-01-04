# Author: Cláudio Ferreira Carneiro
# LNLS - Brazilian Synchrotron Light Source Laboratory

FROM  lnlscon/epics-r3.15.8:v1.2 AS base
LABEL maintainer="Claudio Carneiro <claudio.carneiro@lnls.br>"

# VIM
RUN apt-get -y update && apt-get -y install procps socat vim

# Epics auto addr list
ENV EPICS_CA_AUTO_ADDR_LIST YES

# Base procServ port
ENV EPICS_IOC_CAPUTLOG_INET 0.0.0.0
ENV EPICS_IOC_CAPUTLOG_PORT 7012
ENV EPICS_IOC_LOG_INET 0.0.0.0
ENV EPICS_IOC_LOG_PORT 7011

ENV IOC_PROCSERV_SOCK /opt/RFCalcIOC/sockets/ioc.sock
ENV PCTRL_SOCK /opt/RFCalcIOC/procCtrl/sockets/pCtrl.sock

RUN mkdir -p /opt/RFCalcIOC/autosave

WORKDIR /opt/RFCalcIOC

COPY . /opt/RFCalcIOC

RUN cd /opt/RFCalcIOC/procCtrl && envsubst < configure/RELEASE.tmplt > configure/RELEASE &&\
    cat configure/RELEASE && make distclean && make clean && make -j$(nproc) && mkdir sockets &&\
    \
    cd /opt/RFCalcIOC/ && mkdir sockets && envsubst < configure/RELEASE.tmplt > configure/RELEASE &&\
    make -j$(nproc)

ENV NAME RF-CALC
ENV CMD st.cmd
ENV IOC_PROCSERV_PREFIX PCtrl:${NAME}

ENTRYPOINT [ "/bin/bash", "/opt/RFCalcIOC/entrypoint.sh" ]

