
.. _API-PrimeIocFifos:

=============
PrimeIocFifos
=============

*man PrimeIocFifos(9)*

*4.6.0-rc1*

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

This routine allocates memory for the MPT reply and request frame pools (if necessary), and primes the IOC reply FIFO with reply frames.

Returns 0 for success, non-zero for failure.
