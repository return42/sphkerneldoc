
.. _API-regulator-get-linear-step:

=========================
regulator_get_linear_step
=========================

*man regulator_get_linear_step(9)*

*4.6.0-rc1*

return the voltage step size between VSEL values


Synopsis
========

.. c:function:: unsigned int regulator_get_linear_step( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

Returns the voltage step size between VSEL values for linear regulators, or return 0 if the regulator isn't a linear regulator.
