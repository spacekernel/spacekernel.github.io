#  -*- coding: utf-8 -*-
r"""
.. _tutorials-satellite-propagation:

=====================
Satellite Propagation
=====================

It is often the case that an antenna has been tested at a frequency and samples
of its fields are collected in several different directions. In this context,
this tutorial will help you on how to handle this kind of data and use AFTK
tools to visualise it.

Theory (Optional)
-----------------


Consider the domain :math:`D = \left(-\pi,\pi\right]\times\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]`

.. math::
    \StateDot\pare{\Time}
    =
    \boldsymbol{\Psi}\pare{\vphantom{\frac{}{}}\Time, \State\pare{\Time}}
    +
    \bmrm{b}
    \dot{\bmrm{v}}
    \pare{\Time}




"""

from matplotlib import pyplot


figure, axes = pyplot.subplots()

pyplot.show()

