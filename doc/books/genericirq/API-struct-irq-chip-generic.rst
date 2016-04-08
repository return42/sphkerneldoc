
.. _API-struct-irq-chip-generic:

=======================
struct irq_chip_generic
=======================

*man struct irq_chip_generic(9)*

*4.6.0-rc1*

Generic irq chip data structure


Synopsis
========

.. code-block:: c

    struct irq_chip_generic {
      raw_spinlock_t lock;
      void __iomem * reg_base;
      u32 (* reg_readl) (void __iomem *addr);
      void (* reg_writel) (u32 val, void __iomem *addr);
      void (* suspend) (struct irq_chip_generic *gc);
      void (* resume) (struct irq_chip_generic *gc);
      unsigned int irq_base;
      unsigned int irq_cnt;
      u32 mask_cache;
      u32 type_cache;
      u32 polarity_cache;
      u32 wake_enabled;
      u32 wake_active;
      unsigned int num_ct;
      void * private;
      unsigned long installed;
      unsigned long unused;
      struct irq_domain * domain;
      struct list_head list;
      struct irq_chip_type chip_types[0];
    };


Members
=======

lock
    Lock to protect register and cache data access

reg_base
    Register base address (virtual)

reg_readl
    Alternate I/O accessor (defaults to readl if NULL)

reg_writel
    Alternate I/O accessor (defaults to writel if NULL)

suspend
    Function called from core code on suspend once per chip; can be useful instead of irq_chip::suspend to handle chip details even when no interrupts are in use

resume
    Function called from core code on resume once per chip;

irq_base
    Interrupt base nr for this chip

irq_cnt
    Number of interrupts handled by this chip

mask_cache
    Cached mask register shared between all chip types

type_cache
    Cached type register

polarity_cache
    Cached polarity register

wake_enabled
    Interrupt can wakeup from suspend

wake_active
    Interrupt is marked as an wakeup from suspend source

num_ct
    Number of available irq_chip_type instances (usually 1)

private
    Private data for non generic chip callbacks

installed
    bitfield to denote installed interrupts

unused
    bitfield to denote unused interrupts

domain
    irq domain pointer

list
    List head for keeping track of instances

chip_types[0]
    Array of interrupt irq_chip_types


can be useful instead of irq_chip
=================================

:suspend to handle chip details even when no interrupts are in use


Description
===========

Note, that irq_chip_generic can have multiple irq_chip_type implementations which can be associated to a particular irq line of an irq_chip_generic instance. That allows to
share and protect state in an irq_chip_generic instance when we need to implement different flow mechanisms (level/edge) for it.
