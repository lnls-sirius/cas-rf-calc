#!/usr/bin/env python3
import logging

from string import Template
trigger = Template('''
record(ai, "${name}"){
    field(INP, "${ref} MSS CP")
    field(PREC, "${prec}")
}
''')
flow_rate = Template('''
record(ai, "${name}"){
    field(DESC, "${desc}") 
    field(PREC, "${prec}")
    field(EGU,  "${egu}")
}
''')

temp_delta = Template('''
record(ai, "${name}_buffer"){
    field(INP, "${temp} MSS")
    field(SCAN, "Passive")
    field(PREC, "${prec}")
}
record(calc, "${name}"){
    field(CALC, "B-A")
    field(INPA, "${name}_buffer MSS NPP")
    field(INPB, "${name}_buffer MSS PP")
    field(INPC, "${trigger} CP")
    field(DESC, "${desc}") 
    field(PREC, "${prec}")
    field(EGU,  "${egu}")
}
''')

pwrdiss_n = Template('''
record(calc, "${name}"){
    field(CALC, "1.16*A*B")
    field(INPA, "${t_delta} CP")   # Disc or cell delta T
    field(INPB, "${flow_rate} CP")
    field(DESC, "${desc}") 
    field(PREC, "${prec}")
    field(EGU,  "${egu}")
}
record(compress, "${name}_array"){
    field(INP,  "${name} CP")
    field(NSAM, "3")
    field(ALG,  "Circular Buffer")
    field(DESC, "${desc} (array)") 
    field(PREC, "${prec}")
    field(EGU,  "${egu}")
}
''')

pwr_cell_n = Template('''
record(calc, "${name}"){
    field(CALC, "(A/(1+E/C)+C+(B/(1+D/C)))")
    field(INPA, "${pwr_disc}.VAL[1]")   #  n
    field(INPB, "${pwr_disc}.VAL[2]")   #  n+1
    field(INPC, "${pwr_cell}.VAL[1]")   #  n
    field(INPD, "${pwr_cell}.VAL[2]")   #  n+1
    field(INPE, "${pwr_cell}.VAL[0]")   #  n-1
    field(DESC, "${desc}") 
    field(PREC, "${prec}")
    field(EGU,  "${egu}")
}
''')

vrel_celln = Template('''
record(calc,  "${name}"){
    field(CALC, "SQR(A/(B/7))")
    field(INPA, "${prw_cell_n}")
    field(INPB, "${prw_cell_total}")
    field(DESC, "${desc}") 
    field(PREC, "${prec}")
    field(EGU,  "${egu}")
}
''')

if __name__ == '__main__':
    defaults = {'prec':'4', 'desc':'', 'egu':''}
    trigger_name = 'RF_CALC_IOC_TRIGGER_'
    trigger_ref_name = "SI-02SB:RF-P7Cav:WInT-Mon"


    db = ''
    flow_rate_name = 'SI-02SB:RF-P7Cav:Disc1FlwRt-Mon'
    temp_delta_name = 'SI-02SB:RF-P7Cav:Disc1WdT-Mon'
    temp_name = 'SI-02SB:RF-P7Cav:Cylin1WT-Mon'
    pwr_diss_name = 'SI-02SB:RF-P7Cav:PwrDissDisc1-Mon'
    db += trigger.safe_substitute(defaults, name=trigger_name, ref=trigger_ref_name)
    db += flow_rate.safe_substitute(defaults, name=flow_rate_name)
    db += temp_delta.safe_substitute(defaults, name=temp_delta_name, temp=temp_name, trigger=trigger_name)
    db += pwrdiss_n.safe_substitute(defaults, name=pwr_diss_name, flow_rate=flow_rate_name,t_delta=temp_delta_name)
    #    t_delta='temp_delta_cell_1')
    #db += pwrdiss_n.safe_substitute(defaults, name='pwrdiss_disc_1', flow_rate='flow_rate_1',
    #    t_delta='temp_delta_disc_1')

    #db += pwr_cell_n.safe_substitute(defaults, name='pwr_cell_1', pwr_cell='pwrdiss_cell_1',
    #    pwr_disc='pwrdiss_disc_1')

    with open('Calc.db', 'w+') as _f:
        _f.write(db)
