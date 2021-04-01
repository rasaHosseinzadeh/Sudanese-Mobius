# Sudanese Möbius Strip 

Möbius strip is a manifold that is not orientable and its boundary is a closed curve.
This Python code generates an embedding of Möbius strip
in 3 dimensional space such that its boundary is exactly a circle.

Consider the following construction, we start with the four dimensional space and 
consider the following manifold:
$$
    z = (z_1, z_2) = (\sin(\eta) e^{i\phi}, \cos(\eta) e^{i\phi/2}),
$$
where $\eta \in (0, \pi)$ and $\phi \in (0, 2\pi)$.
Note that $\vert z \vert = 1$ so it lies on $S^3$.
Further, the boundary of the shape is $\vert z_2 \vert = 1$, which is a circle.
We project $S^3$ onto $3$ dimensional Euclidean space,
thus we need to remove a point of $S^3$, but we can not simply remove the
usual $(0,0,0,1)$. Because it lies on the manifold that we want to project.
Therefore, first we rotate $S^3$ with an element of $SO(4)$. The matrix is in the code.
Now that $S^3$ is rotated, we can use the usual stereographic projection
by removing the point $(0,0,0,1)$.

![Sudanese ](Sudanese.png)

If we consider the Möbius strip as a vector bundle over $S^1$,
the interactive plot shows how to
identify each section (that has a constant distance from $S^1$) on the 
Sudanese strip with a corresponding section on a usual embedding, the same
is done for fibers as well (By moving the slider in the bottom of the plot).

The file `sudanese.html` contains the generated plot and `code.py` contains the python
code that generates the plot.
