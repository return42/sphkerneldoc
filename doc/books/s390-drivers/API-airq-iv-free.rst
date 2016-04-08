
.. _API-airq-iv-free:

============
airq_iv_free
============

*man airq_iv_free(9)*

*4.6.0-rc1*

free irq bits of an interrupt vector


Synopsis
========

.. c:function:: void airq_iv_free( struct airq_iv * iv, unsigned long bit, unsigned long num )

Arguments
=========

``iv``
    pointer to interrupt vector structure

``bit``
    number of the first irq bit to free

``num``
    number of consecutive irq bits to free
