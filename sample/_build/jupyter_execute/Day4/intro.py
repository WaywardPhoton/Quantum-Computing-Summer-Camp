## Quantum Algorithms

Today we're going to be exploring how we can actually *do* tihngs with quantum computers! So far we've learned about entanglement, superposition, and quantum gates. Now we're going to put all these concepts together and learn about quantum algorithms.

A typical quantum algorithm consists of:

- The problem we want to solve,

- A classical algorithm that can describe the working of the quantum circuit,

- The quantum circuit that uses quantum gates to manipulate qubits,

- And the output (in classical 0 or 1) to the problem. 

Quantum computers are then programmed to run these quantum circuits. They can be constructed out of any quantum technology that allows for defining qubit elements, and can implement single- and multi-qubit operations. Some of these quantum technologies include quantum things we have already looked at, such as superconducting materials, photons, or trapped (and very cold) atoms.  
Currently, quantum computers based on superconducting circuits, trapped-ions, semiconducting quantum-dots, photons, and neutral atoms, are actively being developed, and many are accessible to users over the internet. 

IBM has a cloud-accessible quantum computer with 53 qubits. The circuits on the computer are programmed using the Qiskit SDK. Qiskit provides a platform in which you can use a computer language (in this case, Python) to interact with the quantum computer, map the circuit instructions onto the existing hardware, and simulate the effect of the circuit in real time. 
<br>
<br>


![](images/IBM.png)

*The IBM Quantum Computer*


```{toctree}
:hidden:
:titlesonly:


SuperpositionAgain
pickle
exploring
ProjectIdeas
Project
```
