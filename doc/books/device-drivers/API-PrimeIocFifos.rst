.. -*- coding: utf-8; mode: rst -*-

.. _API-PrimeIocFifos:

=============
PrimeIocFifos
=============

*man PrimeIocFifos(9)*

*4.6.0-rc5*

Initialize IOC request and reply FIFOs.


Synopsis
========

.. c:function:: int PrimeIocFifos( MPT_ADAPTER * ioc )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure


Description
===========

This routine allocates memory for the MPT reply and request frame pools
(if necessary), and primes the IOC reply FIFO with reply frames.

Returns 0 for success, non-zero for failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
