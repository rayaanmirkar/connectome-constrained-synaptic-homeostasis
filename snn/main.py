from brian2 import *
import numpy as np
prefs.codegen.target = "numpy"


start_scope()

tau_mem = 20*ms # membrane-time constant
v_rest = 0 # resting potential
v_max =  # threshold
v_reset = 0 # v after spike/reset
tau_atp = 2000*ms #atp time constant; **how fast atp is replenished**
t_dep = 0.15 # atp depression; **how much atp is lost when fireing.
max_atp = 1.0 # max atp/how much is available
I_sensory = 0.5 # constant sensory input
n_N = 10 # no. neurons (n_N)

eqs = '''
dv/dt = (v_rest - v + I_sensory) / tau_mem : 1 (unless refractory)
datp/dt = (max_atp - atp)/ tau_atp : 1
tau: second
tau_atp = second
atp_rest
'''


#on_pre = 

neurons = NeuronGroup(n_N, model = eqs, threshold='v> v_max', reset='v = 0*mV', method='euler')
neurons.ATP = 1.0   



###
#print('Before v = %s' % G.v[0])
#run(100*ms)
#print('After v = %s' % G.v[0])
###