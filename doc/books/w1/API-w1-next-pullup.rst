.. -*- coding: utf-8; mode: rst -*-

.. _API-w1-next-pullup:

==============
w1_next_pullup
==============

*man w1_next_pullup(9)*

*4.6.0-rc5*

register for a strong pullup


Synopsis
========

.. c:function:: void w1_next_pullup( struct w1_master * dev, int delay )

Arguments
=========

``dev``
    the master device

``delay``
    time in milliseconds


Description
===========

Put out a strong pull-up of the specified duration after the next write
operation. Not all hardware supports strong pullups. Hardware that
doesn't support strong pullups will sleep for the given time after the
write operation without a strong pullup. This is a one shot request for
the next write, specifying zero will clear a previous request. The w1
master lock must be held.


Return
======

0=success, anything else=error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
