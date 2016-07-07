.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-u300.c

.. _`clk_syscon`:

struct clk_syscon
=================

.. c:type:: struct clk_syscon

    U300 syscon clock

.. _`clk_syscon.definition`:

Definition
----------

.. code-block:: c

    struct clk_syscon {
        struct clk_hw hw;
        bool hw_ctrld;
        bool reset;
        void __iomem *res_reg;
        u8 res_bit;
        void __iomem *en_reg;
        u8 en_bit;
        u16 clk_val;
    }

.. _`clk_syscon.members`:

Members
-------

hw
    corresponding clock hardware entry

hw_ctrld
    whether this clock is hardware controlled (for refcount etc)
    and does not need any magic pokes to be enabled/disabled

reset
    state holder, whether this block's reset line is asserted or not

res_reg
    reset line enable/disable flag register

res_bit
    bit for resetting or taking this consumer out of reset

en_reg
    clock line enable/disable flag register

en_bit
    bit for enabling/disabling this consumer clock line

clk_val
    magic value to poke in the register to enable/disable
    this one clock

.. _`u300_clock`:

struct u300_clock
=================

.. c:type:: struct u300_clock

    defines the bits and pieces for a certain clock

.. _`u300_clock.definition`:

Definition
----------

.. code-block:: c

    struct u300_clock {
        u8 type;
        u8 id;
        bool hw_ctrld;
        u16 clk_val;
    }

.. _`u300_clock.members`:

Members
-------

type
    the clock type, slow fast or rest

id
    the bit in the slow/fast/rest register for this clock

hw_ctrld
    whether the clock is hardware controlled

clk_val
    a value to poke in the one-write enable/disable registers

.. _`clk_mclk`:

struct clk_mclk
===============

.. c:type:: struct clk_mclk

    U300 MCLK clock (MMC/SD clock)

.. _`clk_mclk.definition`:

Definition
----------

.. code-block:: c

    struct clk_mclk {
        struct clk_hw hw;
        bool is_mspro;
    }

.. _`clk_mclk.members`:

Members
-------

hw
    corresponding clock hardware entry

is_mspro
    if this is the memory stick clock rather than MMC/SD

.. This file was automatic generated / don't edit.

