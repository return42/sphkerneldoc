
.. _API-regulator-put:

=============
regulator_put
=============

*man regulator_put(9)*

*4.6.0-rc1*

"free" the regulator source


Synopsis
========

.. c:function:: void regulator_put( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Note
====

drivers must ensure that all regulator_enable calls made on this regulator source are balanced by regulator_disable calls prior to calling this function.
