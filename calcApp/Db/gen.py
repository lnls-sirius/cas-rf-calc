#!/usr/bin/env python3
import logging

from string import Template

flow_rate = Template('''
record(ai, "${name}"){
    field(DESC, "${desc}") 
    field(PREC, "${prec}")
    field(EGU,  "${egu}")
}
''')

temp_delta = Template('''
record(calc, "${name}"){
    field(CALC, "")
    field(INPA, "")
    field(INPB, "")
    field(DESC, "${desc}") 
    field(PREC, "${prec}")
    field(EGU,  "${egu}")
}
''')

pwrdiss_n = Template('''
record(calc, "${name}"){
    field(CALC, "1.16*A*B")
    field(INPA, "${t_delta}")   # Disc or cell delta T
    field(INPB, "${flow_rate}")
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
    field(INPB, "${pwr_disc}.VAL[0]")   #  n+1
    field(INPC, "${pwr_cell}.VAL[1]")   #  n
    field(INPD, "${pwr_cell}.VAL[0]")   #  n+1
    field(INPE, "${pwr_cell}.VAL[2]")   #  n-1
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

    db = ''
    db += flow_rate.safe_substitute(defaults, name='flow_rate_1')
    db += temp_delta.safe_substitute(defaults, name='temp_delta_cell_1')
    db += temp_delta.safe_substitute(defaults, name='temp_delta_disc_1')

    db += pwrdiss_n.safe_substitute(defaults, name='pwrdiss_cell_1', flow_rate='flow_rate_1',
        t_delta='temp_delta_cell_1')
    db += pwrdiss_n.safe_substitute(defaults, name='pwrdiss_disc_1', flow_rate='flow_rate_1',
        t_delta='temp_delta_disc_1')

    db += pwr_cell_n.safe_substitute(defaults, name='pwr_cell_1', pwr_cell='pwrdiss_cell_1',
        pwr_disc='pwrdiss_disc_1') 

    with open('Calc.db', 'w+') as _f:
        _f.write(db)
