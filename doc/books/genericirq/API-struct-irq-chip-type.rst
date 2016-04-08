
.. _API-struct-irq-chip-type:

====================
struct irq_chip_type
====================

*man struct irq_chip_type(9)*

*4.6.0-rc1*

Generic interrupt chip instance for a flow type


Synopsis
========

.. code-block:: c

    struct irq_chip_type {
      struct irq_chip chip;
      struct irq_chip_regs regs;
      irq_flow_handler_t handler;
      u32 type;
      u32 mask_cache_priv;
      u32 * mask_cache;
    };


Members
=======

chip
    The real interrupt chip which provides the callbacks

regs
    Register offsets for this chip

handler
    Flow handler associated with this chip

type
    Chip can handle these flow types

mask_cache_priv
    Cached mask register private to the chip type

mask_cache
    Pointer to cached mask register


Description
===========

A irq_generic_chip can have several instances of irq_chip_type when it requires different functions and register offsets for different flow types.
