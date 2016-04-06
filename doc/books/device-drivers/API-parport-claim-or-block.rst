
.. _API-parport-claim-or-block:

======================
parport_claim_or_block
======================

*man parport_claim_or_block(9)*

*4.6.0-rc1*

claim access to a parallel port device


Synopsis
========

.. c:function:: int parport_claim_or_block( struct pardevice * dev )

Arguments
=========

``dev``
    pointer to structure representing a device on the port


Description
===========

This behaves like ``parport_claim``, but will block if necessary to wait for the port to be free. A return value of 1 indicates that it slept; 0 means that it succeeded without
needing to sleep. A negative error code indicates failure.
