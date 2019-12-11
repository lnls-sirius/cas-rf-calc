#!/usr/bin/env python3

from string import Template

temps = ['SI-02SB:RF-P7Cav:Disc1WT-Mon',
         'SI-02SB:RF-P7Cav:Disc2WT-Mon',
         'SI-02SB:RF-P7Cav:Disc3WT-Mon',
         'SI-02SB:RF-P7Cav:Disc4WT-Mon',
         'SI-02SB:RF-P7Cav:Disc5WT-Mon',
         'SI-02SB:RF-P7Cav:Disc6WT-Mon',
         'SI-02SB:RF-P7Cav:Disc7WT-Mon',
         'SI-02SB:RF-P7Cav:Disc8WT-Mon',
         'SI-02SB:RF-P7Cav:Cylin1WT-Mon',
         'SI-02SB:RF-P7Cav:Cylin2WT-Mon',
         'SI-02SB:RF-P7Cav:Cylin3WT-Mon',
         'SI-02SB:RF-P7Cav:Cylin4WT-Mon',
         'SI-02SB:RF-P7Cav:Cylin5WT-Mon',
         'SI-02SB:RF-P7Cav:Cylin6WT-Mon',
         'SI-02SB:RF-P7Cav:Cylin7WT-Mon']

d_temps = ['SI-02SB:RF-P7Cav:Disc1WdT-Mon',
           'SI-02SB:RF-P7Cav:Disc2WdT-Mon',
           'SI-02SB:RF-P7Cav:Disc3WdT-Mon',
           'SI-02SB:RF-P7Cav:Disc4WdT-Mon',
           'SI-02SB:RF-P7Cav:Disc5WdT-Mon',
           'SI-02SB:RF-P7Cav:Disc6WdT-Mon',
           'SI-02SB:RF-P7Cav:Disc7WdT-Mon',
           'SI-02SB:RF-P7Cav:Disc8WdT-Mon',
           'SI-02SB:RF-P7Cav:Cylin1WdT-Mon',
           'SI-02SB:RF-P7Cav:Cylin2WdT-Mon',
           'SI-02SB:RF-P7Cav:Cylin3WdT-Mon',
           'SI-02SB:RF-P7Cav:Cylin4WdT-Mon',
           'SI-02SB:RF-P7Cav:Cylin5WdT-Mon',
           'SI-02SB:RF-P7Cav:Cylin6WdT-Mon',
           'SI-02SB:RF-P7Cav:Cylin7WdT-Mon']

flow_rates = ['SI-02SB:RF-P7Cav:Disc1FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Disc2FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Disc3FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Disc4FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Disc5FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Disc6FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Disc7FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Disc8FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Cell1FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Cell2FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Cell3FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Cell4FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Cell5FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Cell6FlwRt-Mon',
              'SI-02SB:RF-P7Cav:Cell7FlwRt-Mon']

power_diss_array = ['SI-02SB:RF-P7Cav:PwrDissDisc1-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissDisc2-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissDisc3-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissDisc4-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissDisc5-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissDisc6-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissDisc7-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissDisc8-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissCell1-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissCell2-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissCell3-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissCell4-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissCell5-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissCell6-Mon',
                    'SI-02SB:RF-P7Cav:PwrDissCell7-Mon']

pwr_cell_water = ['SI-02SB:RF-P7Cav:PwrWtCell1-Mon',
                  'SI-02SB:RF-P7Cav:PwrWtCell2-Mon',
                  'SI-02SB:RF-P7Cav:PwrWtCell3-Mon',
                  'SI-02SB:RF-P7Cav:PwrWtCell4-Mon',
                  'SI-02SB:RF-P7Cav:PwrWtCell5-Mon',
                  'SI-02SB:RF-P7Cav:PwrWtCell6-Mon',
                  'SI-02SB:RF-P7Cav:PwrWtCell7-Mon']

cell_voltage_relation = ['SI-02SB:RF-P7Cav:VrCell1-Mon',
                         'SI-02SB:RF-P7Cav:VrCell2-Mon',
                         'SI-02SB:RF-P7Cav:VrCell3-Mon',
                         'SI-02SB:RF-P7Cav:VrCell4-Mon',
                         'SI-02SB:RF-P7Cav:VrCell5-Mon',
                         'SI-02SB:RF-P7Cav:VrCell6-Mon',
                         'SI-02SB:RF-P7Cav:VrCell7-Mon']

trigger_tmpl = Template('''
record(ai, "${name}"){
    field(INP, "${ref} MSS CP")
    field(PREC, "${prec}")
}
''')

flow_rate_tmpl = Template('''
record(ai, "${name}"){
    field(DESC, "${desc}")
    field(PREC, "${prec}")
    field(EGU,  "L/h")
}
''')

temp_delta_tmpl = Template('''
record(calc, "${name}"){
    field(CALC, "B-A")
    field(INPA, "${temp_inp} MSS CP")
    field(INPB, "${temp} MSS")
    field(DESC, "${desc}")
    field(PREC, "${prec}")
    field(EGU,  "C")
}
''')

pwrdiss_n_tmpl = Template('''
record(calc, "${name}"){
    field(CALC, "1.16*A*B/1000")
    field(INPA, "${t_delta} CP")   # Disc or cell delta T
    field(INPB, "${flow_rate} CP")
    field(DESC, "${desc}")
    field(PREC, "${prec}")
    field(EGU,  "kW")
}
''')

total_water_power = Template('''
record(calc, "${name}"){
    field(CALC, "A+B+C+D+E+F+G")
    field(INPA, "${pwr_cell_1} MSS CP")
    field(INPB, "${pwr_cell_2} MSS CP")
    field(INPC, "${pwr_cell_3} MSS CP")
    field(INPD, "${pwr_cell_4} MSS CP")
    field(INPE, "${pwr_cell_5} MSS CP")
    field(INPF, "${pwr_cell_6} MSS CP")
    field(INPG, "${pwr_cell_7} MSS CP")
    field(PREC, "${prec}")
    field(EGU, "${egu}")
}
record(calc, "${name_dbm}"){
    field(CALC, "10*LOG(A*10^6)")
    field(INPA, "${name} CP")
    field(PREC, "${prec}")
    field(EGU, "${egu}")
}
''')

cell_voltage_relation_tmpl = Template('''
record(calc, "${name}"){
    field(CALC, "100*(A/(B/7))^(1/2)")
    field(INPA, "${pwr_cell} MSS CP")
    field(INPB, "${pwr_total} MSS CP")
    field(PREC, "${prec}")
    field(EGU, "${egu}")
}
''')

cell_1_water_power = Template('''
record(calc, "${name}"){
    field(CALC, "A+B+(C/(1+D/B))")
    field(INPA, "${pwr_diss_disc1} MSS CP")
    field(INPB, "${pwr_diss_cell1} MSS CP")
    field(INPC, "${pwr_diss_disc2} MSS CP")
    field(INPD, "${pwr_diss_cell2} MSS CP")
    field(PREC, "${prec}")
    field(EGU, "${egu}")
}
''')

cell_n_water_power = Template('''
record(calc, "${name}"){
    field(CALC, "A/(1+(D/C))+C+B/(1+(E/C))")
    field(INPA, "${pwr_diss_discN} MSS CP")
    field(INPB, "${pwr_diss_discNp1} MSS CP")
    field(INPC, "${pwr_diss_cellN} MSS CP")
    field(INPD, "${pwr_diss_cellNm1} MSS CP")
    field(INPE, "${pwr_diss_cellNp1} MSS CP")
    field(PREC, "${prec}")
    field(EGU, "${egu}")
}
''')
cell_7_water_power = Template('''
record(calc, "${name}"){
    field(CALC, "C + A + (B/(1+D/C))")
    field(INPA, "${pwr_diss_disc8} MSS CP")
    field(INPB, "${pwr_diss_disc7} MSS CP")

    field(INPC, "${pwr_diss_cell7} MSS CP")
    field(INPD, "${pwr_diss_cell6} MSS CP")
    field(PREC, "${prec}")
    field(EGU, "${egu}")
}
''')

if __name__ == '__main__':

    defaults = {'prec': '4', 'desc': '', 'egu': ''}
    water_inp_temp = 'SI-02SB:RF-P7Cav:WInT-Mon'
    water_cell_total_power = 'SI-02SB:RF-P7Cav:PwrWtTotal-Mon'
    water_cell_total_power_dbm = 'SI-02SB:RF-P7Cav:PwrWtTotaldBm-Mon'

    db = ''
    for temp, d_temp, flow_rate, power_diss in zip(temps, d_temps, flow_rates, power_diss_array):
        print(temp, d_temp, flow_rate, power_diss)
        db += flow_rate_tmpl.safe_substitute(defaults, name=flow_rate)
        db += temp_delta_tmpl.safe_substitute(defaults, name=d_temp, temp=temp, temp_inp=water_inp_temp)
        db += pwrdiss_n_tmpl.safe_substitute(defaults, egu='kW', name=power_diss, flow_rate=flow_rate, t_delta=d_temp)

    for i in range(0, 7):
        name = "SI-02SB:RF-P7Cav:PwrWtCell{}-Mon".format(i + 1)
        if i == 0:
            db += cell_1_water_power.safe_substitute(defaults, egu='kW',
                                                     name=name,
                                                     pwr_diss_disc1=power_diss_array[i],
                                                     pwr_diss_disc2=power_diss_array[i + 1],
                                                     pwr_diss_cell1=power_diss_array[i + 8],
                                                     pwr_diss_cell2=power_diss_array[i + 1 + 8])

        elif i == 6:
            db += cell_7_water_power.safe_substitute(defaults, egu='kW',
                                                     name=name,
                                                     pwr_diss_disc7=power_diss_array[i],
                                                     pwr_diss_disc8=power_diss_array[i + 1],
                                                     pwr_diss_cell6=power_diss_array[i - 1 + 8],
                                                     pwr_diss_cell7=power_diss_array[i + 8])
        else:
            db += cell_n_water_power.safe_substitute(defaults, egu='kW',
                                                     name=name,
                                                     pwr_diss_discN=power_diss_array[i],
                                                     pwr_diss_discNp1=power_diss_array[i + 1],
                                                     pwr_diss_cellN=power_diss_array[i + 8],
                                                     pwr_diss_cellNp1=power_diss_array[i + 1 + 8],
                                                     pwr_diss_cellNm1=power_diss_array[i - 1 + 8])

    db += total_water_power.safe_substitute(defaults, egu='kW',
                                            name=water_cell_total_power,
                                            name_dbm=water_cell_total_power_dbm,
                                            pwr_cell_1=pwr_cell_water[0],
                                            pwr_cell_2=pwr_cell_water[1],
                                            pwr_cell_3=pwr_cell_water[2],
                                            pwr_cell_4=pwr_cell_water[3],
                                            pwr_cell_5=pwr_cell_water[4],
                                            pwr_cell_6=pwr_cell_water[5],
                                            pwr_cell_7=pwr_cell_water[6])

    for pwr_cell, cell_voltage in zip(pwr_cell_water, cell_voltage_relation):
        print(pwr_cell, cell_voltage)
        db += cell_voltage_relation_tmpl.safe_substitute(defaults, name=cell_voltage, egu='%',
                                                         pwr_cell=pwr_cell, pwr_total=water_cell_total_power)

    with open('Calc.db', 'w+') as _f:
        _f.write(db)
