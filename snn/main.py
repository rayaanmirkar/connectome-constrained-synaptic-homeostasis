from brian2 import *
import numpy as np
prefs.codegen.target = "numpy"


start_scope()

tau_mem = 20*ms
v_rest = 0
v_max = 1
v_reset = 0
tau_atp = 2000*ms
t_dep = 0.15p
max_atp = 1.0
I_sensory = 0.5 

n_N = 10

eqs = '''
dv/dt = (v_rest - v + I_sensory) / tau_mem : 1 (unless refractory)
datp/dt = (max_atp - atp)/ tau_atp : 1
'''
#on_pre = 

G = NeuronGroup(n_N, model = eqs, threshold='v> v_max', reset='v = 0*mV', method='euler')




###
#print('Before v = %s' % G.v[0])
#run(100*ms)
#print('After v = %s' % G.v[0])
###