.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-spear-spics.c

.. _`spear_spics`:

struct spear_spics
==================

.. c:type:: struct spear_spics

    represents spi chip select control

.. _`spear_spics.definition`:

Definition
----------

.. code-block:: c

    struct spear_spics {
        void __iomem *base;
        u32 perip_cfg;
        u32 sw_enable_bit;
        u32 cs_value_bit;
        u32 cs_enable_mask;
        u32 cs_enable_shift;
        unsigned long use_count;
        int last_off;
        struct gpio_chip chip;
    }

.. _`spear_spics.members`:

Members
-------

base
    base address

perip_cfg
    configuration register

sw_enable_bit
    bit to enable s/w control over chipselects

cs_value_bit
    bit to program high or low chipselect

cs_enable_mask
    mask to select bits required to select chipselect

cs_enable_shift
    bit pos of cs_enable_mask

use_count
    use count of a spi controller cs lines

last_off
    stores last offset caller of \ :c:func:`set_value`\ 

chip
    gpio_chip abstraction

.. This file was automatic generated / don't edit.

