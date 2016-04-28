.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-clk-get:

============
devm_clk_get
============

*man devm_clk_get(9)*

*4.6.0-rc5*

lookup and obtain a managed reference to a clock producer.


Synopsis
========

.. c:function:: struct clk * devm_clk_get( struct device * dev, const char * id )

Arguments
=========

``dev``
    device for clock “consumer”

``id``
    clock consumer ID


Description
===========

Returns a struct clk corresponding to the clock producer, or valid
``IS_ERR`` condition containing errno. The implementation uses ``dev``
and ``id`` to determine the clock consumer, and thereby the clock
producer. (IOW, ``id`` may be identical strings, but clk_get may return
different clock producers depending on ``dev``.)

Drivers must assume that the clock source is not enabled.

devm_clk_get should not be called from within interrupt context.

The clock will automatically be freed when the device is unbound from
the bus.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
