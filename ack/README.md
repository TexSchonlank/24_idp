# In short

This program is an implementation of the Ackermann function.
Run `python ack.py m n` to compute `A(m, n)`, where `A` is defined [as on Wikipedia](https://en.wikipedia.org/wiki/Ackermann_function):

```
A(0, n) := n + 1
A(m + 1, 0) := A(m, 1)
A(m + 1, n + 1) := A(m, A(m + 1, n))
```

# Why?

The Ackermann function is a binary function on the natural numbers, i.e. it has signature `ℕ × ℕ → ℕ`.
It is a well-known example of a [(general-)recursive function](https://en.wikipedia.org/wiki/General_recursive_function) that is not [primitive recursive](https://en.wikipedia.org/wiki/Primitive_recursive_function).

This Python program seeks to show that the Ackermann function is indeed recursive.
We choose to think of the class of recursive functions as precisely those functions of signature `ℕᵏ → ℕ` (for some k) that can be implemented in a procedural programming language with variables and arithmetic where the only control structures are while-loops.

We implement the Ackermann function in Python, making only use of those programming features.
We make no recursive calls, even though `A` is defined recursively.
We do, however, allow ourselves to use if statements and a stack with a push and pop operation.
These features can be implemented using only the primitives (while-loops and arithmetic).

This program does not in any way prove that the Ackermann function is not primitive recursive.

# About the program

We supply no proof of the program's correctness.
The reader is assumed to just see that the program's semantics are such that it computes `A`.

The program is not efficient.
On my machine, it computes up to about `A(3, 10)` and `A(4, 0)`.

# Which Ackermann function?

Our definition of `A` is ordinarily called _the Ackermann function_ after Wilhelm Ackermann [ack].
We follow this convention, even though this particular version of A is perhaps more due to Raphael Robinson [rob] or Rózsa Péter [pet].

# References

[ack] W. Ackermann, “Zum Hilbertschen Aufbau der reellen Zahlen,” Math. Ann., vol. 99, no. 1, pp. 118–133, Dec. 1928, doi: 10.1007/BF01459088.

[rob] R. M. Robinson, “Recursion and double recursion,” Bull. Amer. Math. Soc., vol. 54, no. 10, pp. 987–993, 1948, doi: 10.1090/S0002-9904-1948-09121-2.

[pet] R. Péter, “Konstruktion nichtrekursiver Funktionen,” Math. Ann., vol. 111, no. 1, pp. 42–60, Dec. 1935, doi: 10.1007/BF01472200.

