import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import os
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFT

n_qubits = 20 
N = 2**n_qubits # 1,048,576 points

print(f"--- JINX PROTOCOL: 20 QUBITS SCALE ---")
print(f"Target: {N} integers | ~82,000 prime numbers")
print("Warning: Your PC may appear 'frozen' for 1 to 5 minutes. This is normal.")

try:
    # 1. Massive Sieve
    def get_primes(n):
        p = np.ones(n, dtype=bool)
        p[:2] = False
        for i in range(2, int(n**0.5)+1):
            if p[i]: p[i*i::i] = False
        return p.astype(np.float64)

    print("Generating one-million point sieve...")
    data = get_primes(N)
    
    # 2. Precision Normalization
    norm = np.linalg.norm(data)
    state_vector = data / norm
    state_vector = state_vector / np.sqrt(np.sum(np.abs(state_vector)**2))
    del data # Immediate memory release to make room for the simulator

    # 3. Quantum Circuit
    qc = QuantumCircuit(n_qubits)
    qc.initialize(state_vector, range(n_qubits))
    del state_vector

    # QFT without swaps to save computational resources
    qft_block = QFT(num_qubits=n_qubits, do_swaps=False).decompose()
    qc.append(qft_block, range(n_qubits))
    qc.save_statevector()

    # 4. Simulation (The moment of truth)
    print("Calculating quantum interferences (Hard drive access)...")
    backend = AerSimulator()
    qc_t = transpile(qc, backend)
    result = backend.run(qc_t).result()
    sv = result.get_statevector()
    res = np.abs(sv.data)**2
    del sv

    # 5. "Deep Purple" Rendering
    print("Generating ultra-high resolution image...")
    plt.figure(figsize=(24, 12))
    # Displaying every other point to avoid saturating GPU memory
    plt.loglog(np.arange(1, N//2, 2), res[1:N//2:2], color='#6600ff', lw=0.2, alpha=0.7)
    
    plt.title(f"Jinx Signature - Millionaire Scan (20 Qubits)\nExperimental Validation: Xavier J. Regent")
    plt.gca().set_facecolor('#020202')
    
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    save_path = os.path.join(desktop, "JINX_ULTRA_20Q.png")
    
    plt.savefig(save_path, dpi=400)
    print(f"\n--- HISTORIC VICTORY ---")
    print(f"The 1-million point image is located here: {save_path}")

except Exception as e:
    print(f"\nLIMIT REACHED: {e}")

print("\n-------------------------------------------")
input("Computation finished. Press Enter to release your PC resources.")