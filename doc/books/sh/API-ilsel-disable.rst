.. -*- coding: utf-8; mode: rst -*-

.. _API-ilsel-disable:

=============
ilsel_disable
=============

*man ilsel_disable(9)*

*4.6.0-rc5*

Disable an ILSEL set


Synopsis
========

.. c:function:: void ilsel_disable( unsigned int irq )

Arguments
=========

``irq``
    Bit position for ILSEL set value (retval from enable routines)


Description
===========

Disable a previously enabled ILSEL set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
