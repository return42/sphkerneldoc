.. -*- coding: utf-8; mode: rst -*-

.. _API-sq-flush-range:

==============
sq_flush_range
==============

*man sq_flush_range(9)*

*4.6.0-rc5*

Flush (prefetch) a specific SQ range


Synopsis
========

.. c:function:: void sq_flush_range( unsigned long start, unsigned int len )

Arguments
=========

``start``
    the store queue address to start flushing from

``len``
    the length to flush


Description
===========

Flushes the store queue cache from ``start`` to ``start`` + ``len`` in a
linear fashion.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
