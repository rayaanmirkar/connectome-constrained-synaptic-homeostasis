from brian2 import *
import numpy as np
import matplotlib.pyplot as plt
prefs.codegen.target = "numpy"


start_scope()

#Membrane Variables
tau_mem = 20 * ms    # membrane-time constant
v_rest = -70 * mV    # resting potential
v_max = -55 * mV     # threshold
v_reset = -70 * mV   # v after spike/reset

#ATP Variables
tau_atp = 500 * ms   # atp time constant; **how fast atp is replenished**
t_dep = 0.24 * mM     # atp depression; **how much atp is lost when fireing.
max_atp = 1.0 * mM    # max atp/how much is available

#Input Variables/Misc.
I_sensory = 20 *mV    # constant sensory input
n_N = 10              # no. neurons (n_N)

eqs = '''
#leaky-integrate-and-fire equation
dv/dt = (v_rest - v + I_sensory) / tau_mem : volt


#ATP Equation
datp/dt = (max_atp - atp)/ tau_atp : mM

'''

neurons = NeuronGroup(
            n_N, 
            model = eqs, 
            threshold='v > -55*mV', 
            reset='v = -70*mV; atp -= t_dep', 
            method='euler')

S = Synapses(neurons, neurons, on_pre='''




''')

neurons.v = v_rest
neurons.atp = max_atp 

run(1000*ms)

state_monitor = StateMonitor(neurons, 'v', record= 0)
spike_monitor = SpikeMonitor(neurons)
plot(state_monitor.t/ms, state_monitor.v[0])
plt.xlabel('Time (ms)')
plt.ylabel('Values')
plt.legend()
plt.show()


