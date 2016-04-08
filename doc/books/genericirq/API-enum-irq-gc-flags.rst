
.. _API-enum-irq-gc-flags:

=================
enum irq_gc_flags
=================

*man enum irq_gc_flags(9)*

*4.6.0-rc1*

Initialization flags for generic irq chips


Synopsis
========

.. code-block:: c

    enum irq_gc_flags {
      IRQ_GC_INIT_MASK_CACHE,
      IRQ_GC_INIT_NESTED_LOCK,
      IRQ_GC_MASK_CACHE_PER_TYPE,
      IRQ_GC_NO_MASK,
      IRQ_GC_BE_IO
    };


Constants
=========

IRQ_GC_INIT_MASK_CACHE
    Initialize the mask_cache by reading mask reg

IRQ_GC_INIT_NESTED_LOCK
    Set the lock class of the irqs to nested for irq chips which need to call ``irq_set_wake`` on the parent irq. Usually GPIO implementations

IRQ_GC_MASK_CACHE_PER_TYPE
    Mask cache is chip type private

IRQ_GC_NO_MASK
    Do not calculate irq_data->mask

IRQ_GC_BE_IO
    Use big-endian register accesses (default: LE)
