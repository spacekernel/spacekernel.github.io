#  -*- coding: utf-8 -*-
r"""

.. _tutorials-coords-ellipsoid:

===================
Reference Ellipsoid
===================



Parametrization Theory (Optional)
---------------------------------


Consider the domain :math:`D = \left(-\pi,\pi\right]\times\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]`

In this sense, let :math:`\PosSph \in \Real^{3\times1}` be the position of a sphere surface, then. 





.. math::
    \Pos\pare{\lambda, \beta}
    =
    \Pos_{\mathrm{surf}}\pare{\lambda, \beta}
    +
    h \hat{\boldsymbol{n}}\pare{\lambda, \beta}


.. image:: /_static/tikzpic/ellipsoid.svg
   :align: center
   :width: 300px


"""

from matplotlib import pyplot


figure, axes = pyplot.subplots()

pyplot.show()
