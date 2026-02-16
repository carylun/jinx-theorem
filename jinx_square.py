import numpy as np
import matplotlib.pyplot as plt
import os
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFT

n_qubits = 20 
N = 2**n_qubits # 1,048,576 points

print(f"--- JINX PROTOCOL: SQUARE SCALE (20 QUBITS) ---")
print(f"Analyzing quadratic structure across {N} integers")

try:
    # 1. Square Field Generation (Sieve replacement)
    def get_squares(n):
        field = np.zeros(n, dtype=np.float64)
        # Mark each position corresponding to a perfect square
        limit = int(np.sqrt(n-1))
        for i in range(1, limit + 1):
            field[i*i] = 1.0
        return field

    print("Mapping perfect squares...")
    data = get_squares(N)
    
    # 2. Normalization and State Preparation
    norm = np.linalg.norm(data)
    state_vector = data / norm
    state_vector = state_vector / np.sqrt(np.sum(np.abs(state_vector)**2))
    del data 

    # 3. Quantum Circuit (Interferometer)
    qc = QuantumCircuit(n_qubits)
    qc.initialize(state_vector, range(n_qubits))
    del state_vector

    # Apply QFT to extract the frequency signature
    qft_block = QFT(num_qubits=n_qubits, do_swaps=False).decompose()
    qc.append(qft_block, range(n_qubits))
    qc.save_statevector()

    # 4. Simulation
    print("Calculating quadratic nitescence interference...")
    backend = AerSimulator()
    qc_t = transpile(qc, backend)
    result = backend.run(qc_t).result()
    sv = result.get_statevector()
    res = np.abs(sv.data)**2
    del sv

    # 5. Visual Rendering (Deep Emerald for squares)
    print("Generating quadratic spectrum...")
    plt.figure(figsize=(24, 12))
    plt.semilogy(np.arange(1, N, 4), res[1:N:4], color='#00ffcc', lw=0.3, alpha=0.8)
    
    plt.title(f"Jinx Signature - Perfect Square Spectrum (20 Qubits)\nStructural Analysis: Xavier J. Regent")
    plt.gca().set_facecolor('#050505')
    
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    save_path = os.path.join(desktop, "JINX_SQUARES_20Q.png")
    
    plt.savefig(save_path, dpi=400)
    print(f"\n--- QUADRATIC SCAN COMPLETE ---")
    print(f"The square spectrum is saved here: {save_path}")

except Exception as e:
    print(f"\nFIELD ERROR: {e}")

print("\n-------------------------------------------")
input("Click to close.")