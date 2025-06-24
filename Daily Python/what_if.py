def combine(f, g):
    return lambda x: f(g(x))
f = lambda x: x ** 2
g = lambda x: x + 2
h = combine(f, g)
print(h(3))  
   # A: 9
   # B: 25
   # C: 16
   # D: 10

# This code defines a function `combine` that takes two functions `f` and `g`
# and returns a new function that applies `g` to its input and then applies `f
#` to the result of `g`. The functions `f` and `g` are defined as follows:
# - `f` squares its input.
# - `g` adds 2 to its input.
# The combined function `h` is then called with the input `3`.
# The output is calculated as follows:
# 1. `g(3)` computes `3 + 2`, which equals `5`.
# 2. `f(g(3))` computes `f(5)`, which
#    squares `5`, resulting in `25`.
# Therefore, the output of `h(3)` is `25`.
    # Output: 25, since h(3) = f(g(3)) = f(5) = 5^2