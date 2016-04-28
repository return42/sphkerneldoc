.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-put:

=============
regulator_put
=============

*man regulator_put(9)*

*4.6.0-rc5*

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

drivers must ensure that all regulator_enable calls made on this
regulator source are balanced by regulator_disable calls prior to
calling this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
