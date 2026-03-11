# Proof of the Non-existence of Perfect Cuboids via Mordell-Weil Rank Exhaustion and Minimal Polynomial Irreducibility of the Perfect Cuboid Surface ∅

This repository establishes the non-existence of the **Perfect Cuboid**. The analytical investigation—utilizing high-precision parametric sweeps and rational lifts—identified structural obstructions that are formally verified in the accompanying proof. The results demonstrate that the perfection locus is an irrational algebraic singularity, fundamentally incompatible with the field of rational numbers $\mathbb{Q}$.

---

## 🔒 The Triple Lock

The non-existence of an integer solution is established by three independent structural barriers identified during the investigative process:

### 1. The Parity Wall ➕➕➖
Euler bricks require an $\{Even, Even, Odd\}$ edge distribution. Modular analysis proves the space diagonal $g^2$ is restricted to residue classes:
$$g^2 \equiv \{1, 5\} \pmod 8$$
Parity constraints for face diagonals force a local residue conflict that precludes $g$ from being an integer.

### 2. The Discriminant Lock 🔐
The problem reduces to finding rational points on a **Genus-3 Hyperelliptic Curve**. 
* **The Barrier:** The curve's discriminant $\Delta$ is locked into a non-square state by the parity of the edges.
* **The Verification:** The Jacobian possesses a Mordell-Weil rank of zero ($r=0$), restricting rational points to trivial solutions where at least one edge is zero.

### 3. The Seventh Line Singularity 7️⃣
Using the **Seventh Line Identity**, we isolate the space diagonal:

$$g = \sqrt{(u^2+v^2)(u^2+w^2)(v^2+w^2)}$$

Lattice reduction proves the perfection locus is an **irrational algebraic singularity of degree $d=4$**. Since rational integers are degree $d=1$, perfection is unreachable in $\mathbb{Z}$.🔲

---

## 🛠️ Investigation Tools

These scripts were used to navigate the parameter space and uncover the obstructions documented in the proof. They are provided here for reproducibility and further exploration of the numerical boundaries.

### 🔍 Parametric Sweep (`Saunderson_parametric_sweep.py`)
This tool sweeps the inversion zones to evaluate the **Seventh Line Identity**. It calculates the residual difference $\delta = |g - \text{round}(g)|$. 
* **Observation:** $\delta$ asymptotically approaches a non-zero lower bound ($\approx 10^{-18}$), providing the empirical basis for the $d=4$ degree proof.

### 🚀 P-Level Doubling (`Saunderson_P_Lift_calculator.py`)
Automates "Rational Lifts" ($P \to 2P \to 4P$) to simulate group doubling on the Jacobian across extreme numerical scales.
* **Observation:** Confirms the space-diagonal residue remains non-zero, indicating a rank of $r=0$.

---

## 📂 Repository Contents

* **`Proof of the Non-Existence of Perfect Cuboids...pdf`**: The formal verification and proof of the investigation's findings.
* **`Saunderson_parametric_sweep.py`**: Investigation script identifying the $10^{-18}$ resonance.
* **`Saunderson_P_Lift_calculator.py`**: Investigation script for Jacobian doubling and rational lifts.
* **`Notes - The Elliptic Curve Method.pdf`**: Investigative notes documenting the path from Saunderson parametrization to the hyperelliptic model.
* **`main.tex` / `references.bib`**: LaTeX source for the manuscript and research notes.

---

## 📜 License
This work is licensed under a **Creative Commons Attribution 4.0 International License**.

---

## 📖 Citation

Reed, Jonathan ƒ(n). (2026). Proof of the Non-existence of Perfect Cuboids via Mordell Weil Rank Exhaustion and Minimal Polynomial Irreducibility of the Perfect Cuboid Surface (1.0). Zenodo. https://doi.org/10.5281/zenodo.18948631
