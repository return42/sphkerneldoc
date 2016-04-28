.. -*- coding: utf-8; mode: rst -*-

.. _API-input-enable-softrepeat:

=======================
input_enable_softrepeat
=======================

*man input_enable_softrepeat(9)*

*4.6.0-rc5*

enable software autorepeat


Synopsis
========

.. c:function:: void input_enable_softrepeat( struct input_dev * dev, int delay, int period )

Arguments
=========

``dev``
    input device

``delay``
    repeat delay

``period``
    repeat period


Description
===========

Enable software autorepeat on the input device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
