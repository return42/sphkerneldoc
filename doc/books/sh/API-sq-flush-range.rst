
.. _API-sq-flush-range:

==============
sq_flush_range
==============

*man sq_flush_range(9)*

*4.6.0-rc1*

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

Flushes the store queue cache from ``start`` to ``start`` + ``len`` in a linear fashion.
