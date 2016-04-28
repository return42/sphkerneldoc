.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-wait-peripheral:

=======================
parport_wait_peripheral
=======================

*man parport_wait_peripheral(9)*

*4.6.0-rc5*

wait for status lines to change in 35ms


Synopsis
========

.. c:function:: int parport_wait_peripheral( struct parport * port, unsigned char mask, unsigned char result )

Arguments
=========

``port``
    port to watch

``mask``
    status lines to watch

``result``
    desired values of chosen status lines


Description
===========

This function waits until the masked status lines have the desired
values, or until 35ms have elapsed (see IEEE 1284-1994 page 24 to 25 for
why this value in particular is hardcoded). The ``mask`` and ``result``
parameters are bitmasks, with the bits defined by the constants in
parport.h: ``PARPORT_STATUS_BUSY``, and so on.

The port is polled quickly to start off with, in anticipation of a fast
response from the peripheral. This fast polling time is configurable
(using /proc), and defaults to 500usec. If the timeout for this port
(see ``parport_set_timeout``) is zero, the fast polling time is 35ms,
and this function does not call ``schedule``.

If the timeout for this port is non-zero, after the fast polling fails
it uses ``parport_wait_event`` to wait for up to 10ms, waking up if an
interrupt occurs.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
