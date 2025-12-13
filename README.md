# Prime Computer: From Detector to Generator (PA-1)

This repository contains the solution for **Programming Assignment 1 (PA-1)**. The project demonstrates how to transform a primality testing method (Prime Detector) into a formula that computes the $n$-th prime number (Prime Computer).

## 📄 Project Overview

**Key Question:** Can we construct a formula that transforms a prime detector (like Wilson's Theorem) into a prime computer?

This project implements a constructive formula that calculates $p_n$ (the $n$-th prime) using a summation over the prime-counting function $\pi(x)$.

### The Formula
The code implements the following logic to find the $n$-th prime:

$$p_n = 1 + \sum_{i=1}^{M} \left[ \pi(i) < n \right]$$

Where:
- $\pi(i)$ is the number of primes less than or equal to $i$ (calculated using **Wilson's Theorem**).
- $[ \cdot ]$ is the Iverson bracket (or a step function), implemented here using an `arccot` based function.
- $M$ is an upper bound approximation for the $n$-th prime, $M \approx n(\ln n + \ln \ln n)$.

---

## 📂 File Structure

The logic is contained within `pa1.py`. Here is the role of each function:

1.  **`is_prime_wilson(n)`**:
    * **Role**: The "Prime Detector".
    * **Logic**: Uses **Wilson's Theorem**, which states that $n$ is prime if and only if $(n-1)! \equiv -1 \pmod n$.
    
2.  **`count_primes_wilson(x)`**:
    * **Role**: The Prime Counting Function $\pi(x)$.
    * **Logic**: Iterates from 2 to $x$ and sums the result of `is_prime_wilson` to count how many primes exist up to $x$.

3.  **`arccot(x)`** and **`f(x)`**:
    * **Role**: The Step Function.
    * **Logic**: Implements a continuous mathematical switch. `f(x)` returns `1` if the input is positive (indicating we haven't reached the $n$-th prime count yet) and `0` otherwise.

4.  **`nth_prime(n)`**:
    * **Role**: The "Prime Computer" (Main Formula).
    * **Logic**: Sums the results of the step function `f(x)` over a range to mathematically construct the value of the $n$-th prime.

---

## ⚙️ Installation & Usage

### Prerequisites
* Python 3.x
* NumPy (`pip install numpy`)

### Running the Code
1.  Clone the repository.
2.  Run the script:
    ```bash
    python pa1.py
    ```
3.  Enter the value of `n` when prompted. The program will output the $n$-th prime number.

**Example:**
```text
Enter n: 5
The computed value for nth_prime(5) is: 11
