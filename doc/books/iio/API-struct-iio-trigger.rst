.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-iio-trigger:

==================
struct iio_trigger
==================

*man struct iio_trigger(9)*

*4.6.0-rc5*

industrial I/O trigger device


Synopsis
========

.. code-block:: c

    struct iio_trigger {
      const struct iio_trigger_ops * ops;
      int id;
      const char * name;
      struct device dev;
      struct list_head list;
      struct list_head alloc_list;
      atomic_t use_count;
      struct irq_chip subirq_chip;
      int subirq_base;
      struct iio_subirq subirqs[CONFIG_IIO_CONSUMERS_PER_TRIGGER];
      unsigned long pool[BITS_TO_LONGS(CONFIG_IIO_CONSUMERS_PER_TRIGGER)];
      struct mutex pool_lock;
    };


Members
=======

ops
    [DRIVER] operations structure

id
    [INTERN] unique id number

name
    [DRIVER] unique name

dev
    [DRIVER] associated device (if relevant)

list
    [INTERN] used in maintenance of global trigger list

alloc_list
    [DRIVER] used for driver specific trigger list

use_count
    use count for the trigger

subirq_chip
    [INTERN] associate 'virtual' irq chip.

subirq_base
    [INTERN] base number for irqs provided by trigger.

subirqs[CONFIG_IIO_CONSUMERS_PER_TRIGGER]
    [INTERN] information about the 'child' irqs.

pool[BITS_TO_LONGS(CONFIG_IIO_CONSUMERS_PER_TRIGGER)]
    [INTERN] bitmap of irqs currently in use.

pool_lock
    [INTERN] protection of the irq pool.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
