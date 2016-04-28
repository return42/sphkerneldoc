.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-irqaction:

================
struct irqaction
================

*man struct irqaction(9)*

*4.6.0-rc5*

per interrupt action descriptor


Synopsis
========

.. code-block:: c

    struct irqaction {
      irq_handler_t handler;
      void * dev_id;
      void __percpu * percpu_dev_id;
      struct irqaction * next;
      irq_handler_t thread_fn;
      struct task_struct * thread;
      struct irqaction * secondary;
      unsigned int irq;
      unsigned int flags;
      unsigned long thread_flags;
      unsigned long thread_mask;
      const char * name;
      struct proc_dir_entry * dir;
    };


Members
=======

handler
    interrupt handler function

dev_id
    cookie to identify the device

percpu_dev_id
    cookie to identify the device

next
    pointer to the next irqaction for shared interrupts

thread_fn
    interrupt handler function for threaded interrupts

thread
    thread pointer for threaded interrupts

secondary
    pointer to secondary irqaction (force threading)

irq
    interrupt number

flags
    flags (see IRQF_* above)

thread_flags
    flags related to ``thread``

thread_mask
    bitmask for keeping track of ``thread`` activity

name
    name of the device

dir
    pointer to the proc/irq/NN/name entry


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
