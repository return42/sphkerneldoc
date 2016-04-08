
.. _API-ilsel-disable:

=============
ilsel_disable
=============

*man ilsel_disable(9)*

*4.6.0-rc1*

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
