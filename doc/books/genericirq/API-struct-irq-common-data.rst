.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-irq-common-data:

======================
struct irq_common_data
======================

*man struct irq_common_data(9)*

*4.6.0-rc5*

per irq data shared by all irqchips


Synopsis
========

.. code-block:: c

    struct irq_common_data {
      unsigned int __private state_use_accessors;
    #ifdef CONFIG_NUMA
      unsigned int node;
    #endif
      void * handler_data;
      struct msi_desc * msi_desc;
      cpumask_var_t affinity;
    #ifdef CONFIG_GENERIC_IRQ_IPI
      unsigned int ipi_offset;
    #endif
    };


Members
=======

state_use_accessors
    status information for irq chip functions. Use accessor functions to
    deal with it

node
    node index useful for balancing

handler_data
    per-IRQ data for the irq_chip methods

msi_desc
    MSI descriptor

affinity
    IRQ affinity on SMP. If this is an IPI related irq, then this is the
    mask of the CPUs to which an IPI can be sent.

ipi_offset
    Offset of first IPI target cpu in ``affinity``. Optional.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
