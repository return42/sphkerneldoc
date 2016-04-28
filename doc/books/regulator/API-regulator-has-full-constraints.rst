.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-has-full-constraints:

==============================
regulator_has_full_constraints
==============================

*man regulator_has_full_constraints(9)*

*4.6.0-rc5*

the system has fully specified constraints


Synopsis
========

.. c:function:: void regulator_has_full_constraints( void )

Arguments
=========

``void``
    no arguments


Description
===========

Calling this function will cause the regulator API to disable all
regulators which have a zero use count and don't have an always_on
constraint in a late_initcall.

The intention is that this will become the default behaviour in a future
kernel release so users are encouraged to use this facility now.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
