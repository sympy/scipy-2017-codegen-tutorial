# General notes

Let's make sure that we execute all notebooks for the final tutorial, so that
people can follow along without running the code.

# 30

Probably good to give a quick primer on reaction equations for anyone who
doesn't remember their chemestry.

I usually recommend `sym` as the shorthand for `sympy`. I think `sp` is
generally used for `scipy`.

Write the equation for the law of mass action

If f = ydot, why not just call the variable `ydot`? Then the callback can just
be `f`.

We should have some text explaining what is lambdify, what does it do, how do
you call it. It is just shown here but never explained.

itertools.chain adds unncessary complexity. We should write the lambdify call
so that it matches the input to odeint. I believe `lambdify([c, t, *k], f)`
should work (or `lambdify([c, t] + k, f)` for Python 2). Here `t =
symbols('t')` is unused in `f` but a required argument for the callback.

Can you write some text to explain what the other arguments to odeint are (or
more generally, what the input type it expects is)? I think the key thing to
teach here is how to make `lambdify` give a function of form you are looking for.

You can just write `J = Matrix(f).jacobian`. It is already the right shape.

This is a nice example of how having an analytic Jacobian is better. Could
maybe show `%timeit` to show the performance gain.

# 35

Is this stuff used later? It seems a bit tangential, and doesn't really show
any new stuff for SymPy code generation. I would personally skip it (could
leave it in for anyone interested).

# 37

If numba isn't released by the tutorial I guess we will have to skip this. If
there is a simple SymPy workaround and it is looking like they won't, we can
put one into the SymPy release.

Again, can we avoid using the ODEsys stuff? I think we should keep the
tutorial materials as simple as possible, so that people can easily see what
is going on. The key point here: that we are replacing `f = lambdify(...)`
with `f = jit(lambdify(...))` seems to be buried.

What is `njit`? I thought Numba should just use `jit`.

# 38

Symengine stuff is neat, but I worry about putting it in the tutrial since it
is so new.

# 40

Do you plan to add ufuncify?

# 45

# 50

These examples don't really show anything about modifying the code printers so
support sundials. I don't know if that's something that can be shown here, or
if we need another example. Anyway, code printers stuff still needs to be
shown in the tutorial.
