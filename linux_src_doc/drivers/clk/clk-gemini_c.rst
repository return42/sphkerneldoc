.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-gemini.c

.. _`gemini_gate_data`:

struct gemini_gate_data
=======================

.. c:type:: struct gemini_gate_data

    Gemini gated clocks

.. _`gemini_gate_data.definition`:

Definition
----------

.. code-block:: c

    struct gemini_gate_data {
        u8 bit_idx;
        const char *name;
        const char *parent_name;
        unsigned long flags;
    }

.. _`gemini_gate_data.members`:

Members
-------

bit_idx
    the bit used to gate this clock in the clock register

name
    the clock name

parent_name
    the name of the parent clock

flags
    standard clock framework flags

.. _`clk_gemini_pci`:

struct clk_gemini_pci
=====================

.. c:type:: struct clk_gemini_pci

    Gemini PCI clock

.. _`clk_gemini_pci.definition`:

Definition
----------

.. code-block:: c

    struct clk_gemini_pci {
        struct clk_hw hw;
        struct regmap *map;
        unsigned long rate;
    }

.. _`clk_gemini_pci.members`:

Members
-------

hw
    corresponding clock hardware entry

map
    regmap to access the registers

rate
    current rate

.. _`gemini_reset`:

struct gemini_reset
===================

.. c:type:: struct gemini_reset

    gemini reset controller

.. _`gemini_reset.definition`:

Definition
----------

.. code-block:: c

    struct gemini_reset {
        struct regmap *map;
        struct reset_controller_dev rcdev;
    }

.. _`gemini_reset.members`:

Members
-------

map
    regmap to access the containing system controller

rcdev
    reset controller device

.. This file was automatic generated / don't edit.

