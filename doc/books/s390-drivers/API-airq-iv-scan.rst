
.. _API-airq-iv-scan:

============
airq_iv_scan
============

*man airq_iv_scan(9)*

*4.6.0-rc1*

scan interrupt vector for non-zero bits


Synopsis
========

.. c:function:: unsigned long airq_iv_scan( struct airq_iv * iv, unsigned long start, unsigned long end )

Arguments
=========

``iv``
    pointer to interrupt vector structure

``start``
    bit number to start the search

``end``
    bit number to end the search


Description
===========

Returns the bit number of the next non-zero interrupt bit, or -1UL if the scan completed without finding any more any non-zero bits.
