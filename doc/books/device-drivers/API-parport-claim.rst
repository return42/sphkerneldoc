.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-claim:

=============
parport_claim
=============

*man parport_claim(9)*

*4.6.0-rc5*

claim access to a parallel port device


Synopsis
========

.. c:function:: int parport_claim( struct pardevice * dev )

Arguments
=========

``dev``
    pointer to structure representing a device on the port


Description
===========

This function will not block and so can be used from interrupt context.
If ``parport_claim`` succeeds in claiming access to the port it returns
zero and the port is available to use. It may fail (returning non-zero)
if the port is in use by another driver and that driver is not willing
to relinquish control of the port.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
