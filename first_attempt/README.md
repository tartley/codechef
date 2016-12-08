This dir contains my first attempt at the problem.

At an early stage I became enamoured of a solution that uses a generator to
produce all possible paths, and then run over it:

    max(sum(path) for path in all_paths(case))

This solution works, and it has the heart-warming benefit that it works over
all possible DAGs, not just the triangle. But it turns out to be three times as
much code, and much slower, than other solutions! So in the bin it goes.

