.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-yield-blocking:

======================
parport_yield_blocking
======================

*man parport_yield_blocking(9)*

*4.6.0-rc5*

relinquish a parallel port temporarily


Synopsis
========

.. c:function:: int parport_yield_blocking( struct pardevice * dev )

Arguments
=========

``dev``
    a device on the parallel port


Description
===========

This function relinquishes the port if it would be helpful to other
drivers to do so. Afterwards it tries to reclaim the port using
``parport_claim_or_block``, and the return value is the same as for
``parport_claim_or_block``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
