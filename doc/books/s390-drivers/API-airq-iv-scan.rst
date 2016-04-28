.. -*- coding: utf-8; mode: rst -*-

.. _API-airq-iv-scan:

============
airq_iv_scan
============

*man airq_iv_scan(9)*

*4.6.0-rc5*

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

Returns the bit number of the next non-zero interrupt bit, or -1UL if
the scan completed without finding any more any non-zero bits.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
