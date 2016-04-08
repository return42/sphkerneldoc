
.. _API-struct-irq-data:

===============
struct irq_data
===============

*man struct irq_data(9)*

*4.6.0-rc1*

per irq chip data passed down to chip functions


Synopsis
========

.. code-block:: c

    struct irq_data {
      u32 mask;
      unsigned int irq;
      unsigned long hwirq;
      struct irq_common_data * common;
      struct irq_chip * chip;
      struct irq_domain * domain;
    #ifdef CONFIG_IRQ_DOMAIN_HIERARCHY
      struct irq_data * parent_data;
    #endif
      void * chip_data;
    };


Members
=======

mask
    precomputed bitmask for accessing the chip registers

irq
    interrupt number

hwirq
    hardware interrupt number, local to the interrupt domain

common
    point to data shared by all irqchips

chip
    low level interrupt hardware access

domain
    Interrupt translation domain; responsible for mapping between hwirq number and linux irq number.

parent_data
    pointer to parent struct irq_data to support hierarchy irq_domain

chip_data
    platform-specific per-chip private data for the chip methods, to allow shared chip implementations
