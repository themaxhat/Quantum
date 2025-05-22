from qiskit import QuantumCircuit

# QC(number of qubits, number of classical bits for measurement)
circ = QuantumCircuit(1, 1)
circ.h(0) # add a hadamard gate, 0 represents index of wire to apply the gate to
circ.measure(0, 0) # which index to measure, which classical bit to write to

# circ.draw(output="mpl")

from qiskit import Aer, execute
backend_sim = Aer.get_backend("qasm_simulator") # activate backend object

sim = execute(circ, backend_sim, shots=1024) # shots = number of times to run simulation

sim_result = sim.result()
counts = sim_result.get_counts(circ)
print(counts)