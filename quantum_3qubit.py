# pip install qiskit matplotlib
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Define a 3-qubit Grover circuit to search for the |101⟩ state
def grover_3_qubit():
    qc = QuantumCircuit(3)
    
    # Step 1: Apply Hadamard to all qubits to create superposition
    qc.h([0, 1, 2])
    
    # Step 2: Oracle - Marks the |101⟩ state
    qc.x(1)  # Flip qubit 1 to make it look like |111>
    qc.ccz(0, 1, 2)  # Multi-controlled Z gate
    qc.x(1)  # Revert qubit 1
    
    # Step 3: Diffuser - Amplifies the probability of the marked state
    qc.h([0, 1, 2])
    qc.x([0, 1, 2])
    qc.h(2)
    qc.ccz(0, 1, 2)
    qc.h(2)
    qc.x([0, 1, 2])
    qc.h([0, 1, 2])
    
    # Step 4: Measurement
    qc.measure_all()
    
    return qc

# Create and simulate the circuit
qc = grover_3_qubit()
simulator = Aer.get_backend('aer_simulator')
qobj = assemble(transpile(qc, simulator))
result = simulator.run(qobj).result()
counts = result.get_counts()

# Display results
qc.draw('mpl')
plt.show()
plot_histogram(counts)
plt.show()
