.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-get-linear-step:

=========================
regulator_get_linear_step
=========================

*man regulator_get_linear_step(9)*

*4.6.0-rc5*

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

Returns the voltage step size between VSEL values for linear regulators,
or return 0 if the regulator isn't a linear regulator.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
