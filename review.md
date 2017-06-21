# General notes

Let's make sure that we execute all notebooks for the final tutorial, so that
people can follow along without running the code.

[Björn]: notebooks with output cells saved as artifacts for each commit (see link in README)

# 30

Probably good to give a quick primer on reaction equations for anyone who
doesn't remember their chemestry.

[Björn]: I introduced an introductory notebook (25), no benchmarks there
         and more hands on. Does it help? Or did you have something else
         in mind?

I usually recommend `sym` as the shorthand for `sympy`. I think `sp` is
generally used for `scipy`.

[Björn]: Sure, I've changed this throughout.

Write the equation for the law of mass action

[Björn]: I put it in the introductory notebook (25)

If f = ydot, why not just call the variable `ydot`? Then the callback can just
be `f`.

[Björn]: Agreed, changing.

We should have some text explaining what is lambdify, what does it do, how do
you call it. It is just shown here but never explained.

[Björn]: I now talk some about it in (25)

itertools.chain adds unncessary complexity. We should write the lambdify call
so that it matches the input to odeint. I believe `lambdify([c, t, *k], f)`
should work (or `lambdify([c, t] + k, f)` for Python 2). Here `t =
symbols('t')` is unused in `f` but a required argument for the callback.

[Björn]: You're right. I've started changing the notebooks, it'll look
         much cleaner -- thanks!

Can you write some text to explain what the other arguments to odeint are (or
more generally, what the input type it expects is)? I think the key thing to
teach here is how to make `lambdify` give a function of form you are looking for.

[Björn]: I added a link to the documentation and discussed this some in (25)

You can just write `J = Matrix(f).jacobian`. It is already the right shape.

[Björn]: Perfect, thanks

This is a nice example of how having an analytic Jacobian is better. Could
maybe show `%timeit` to show the performance gain.

[Björn]: Added

# 35

Is this stuff used later? It seems a bit tangential, and doesn't really show
any new stuff for SymPy code generation. I would personally skip it (could
leave it in for anyone interested).

[Björn]: The idea was that I wanted to provide a bigger reaction
         system, while not requiring the participants to write it by
         hand. But it's possible that Robertson's example is enough
         to show what we need. It would indeed reduce the complexity
         so I'll look into that.

# 37

If numba isn't released by the tutorial I guess we will have to skip this. If
there is a simple SymPy workaround and it is looking like they won't, we can
put one into the SymPy release.

[Björn]: Yeah, let's skip it unless there is a new release of numba in time.

Again, can we avoid using the ODEsys stuff? I think we should keep the
tutorial materials as simple as possible, so that people can easily see what
is going on. The key point here: that we are replacing `f = lambdify(...)`
with `f = jit(lambdify(...))` seems to be buried.

[Björn]: I will try to rewrite the notebooks without the
         classes. Should be doable - let me get back on that.


What is `njit`? I thought Numba should just use `jit`.

[Björn]: njit gives an error if python calls were needed. We could use jit.

# 38

Symengine stuff is neat, but I worry about putting it in the tutrial since it
is so new.

[Björn]: It will indeed be very new. We can skip it.

# 40

Do you plan to add ufuncify?

[Björn]: I'm hoping to use it in (60) -- I'll look into it tomorrow.

# 45

# 50

These examples don't really show anything about modifying the code printers so
support sundials. I don't know if that's something that can be shown here, or
if we need another example. Anyway, code printers stuff still needs to be
shown in the tutorial.

[Björn]: I can add custom printing of Indexed outputting
         DENSE_ELEM(i, j)? (I was going with that approach first but
         accessing the column-elements through pointers was
         recommended in the CVode documentation)
