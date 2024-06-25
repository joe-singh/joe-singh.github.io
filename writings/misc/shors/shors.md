# Shor's Algorithm


Suppose we want to factor $N$ into its prime 
factors. The inefficient classical way to do this
is a brute force approach that is exponential.
The most efficient classical algorithm for factoring
numbers is the [general number field sieve](https://en.wikipedia.org/wiki/General_number_field_sieve) that
takes sub-exponential time. Shor's Algorithm is a quantum algorithm that
can do this $\mathcal{O}\left(\left(\log N\right)^3\right)$ where 
N is the size of the integer.

## Shor's Algorithm Classical Part
Shor's algorithm is essentially a classical algorithm which 
requires a quantum approach for one step. In this section
we outline the classical approach.

For this discussion, we will make extensive use of 
Euclid's [greatest common divisor (gcd) algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm). 
This is efficient and has a logarithmic complexity. 

Suppose we want to factor $N$. Let's start with a guess $a$.
First let's compute $d = \gcd(a,N)$. If $d \neq 1$ we are done
because we guessed luckily and found a divisor $d$ of $N$. 
You can find the other one by doing $\frac{N}{d}$.

Instead assume that $d = 1$, i.e. $a$ and $N$ are coprime
integers. This means that $a$ is an element of the 
multiplicative group of integers modulo $N$, i.e. 
$a\in \left(\mathbb{Z}/N\mathbb{Z}\right)^{\times}$.
