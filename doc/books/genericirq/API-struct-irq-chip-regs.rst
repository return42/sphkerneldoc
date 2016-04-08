
.. _API-struct-irq-chip-regs:

====================
struct irq_chip_regs
====================

*man struct irq_chip_regs(9)*

*4.6.0-rc1*

register offsets for struct irq_gci


Synopsis
========

.. code-block:: c

    struct irq_chip_regs {
      unsigned long enable;
      unsigned long disable;
      unsigned long mask;
      unsigned long ack;
      unsigned long eoi;
      unsigned long type;
      unsigned long polarity;
    };


Members
=======

enable
    Enable register offset to reg_base

disable
    Disable register offset to reg_base

mask
    Mask register offset to reg_base

ack
    Ack register offset to reg_base

eoi
    Eoi register offset to reg_base

type
    Type configuration register offset to reg_base

polarity
    Polarity configuration register offset to reg_base
