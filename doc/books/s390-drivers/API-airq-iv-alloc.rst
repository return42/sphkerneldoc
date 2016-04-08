
.. _API-airq-iv-alloc:

=============
airq_iv_alloc
=============

*man airq_iv_alloc(9)*

*4.6.0-rc1*

allocate irq bits from an interrupt vector


Synopsis
========

.. c:function:: unsigned long airq_iv_alloc( struct airq_iv * iv, unsigned long num )

Arguments
=========

``iv``
    pointer to an interrupt vector structure

``num``
    number of consecutive irq bits to allocate


Description
===========

Returns the bit number of the first irq in the allocated block of irqs, or -1UL if no bit is available or the AIRQ_IV_ALLOC flag has not been specified
