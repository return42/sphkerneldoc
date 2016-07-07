.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/hisilicon/clkdivider-hi6220.c

.. _`hi6220_clk_divider`:

struct hi6220_clk_divider
=========================

.. c:type:: struct hi6220_clk_divider

    divider clock for hi6220

.. _`hi6220_clk_divider.definition`:

Definition
----------

.. code-block:: c

    struct hi6220_clk_divider {
        struct clk_hw hw;
        void __iomem *reg;
        u8 shift;
        u8 width;
        u32 mask;
        const struct clk_div_table *table;
        spinlock_t *lock;
    }

.. _`hi6220_clk_divider.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register containing divider

shift
    shift to the divider bit field

width
    width of the divider bit field

mask
    mask for setting divider rate

table
    the div table that the divider supports

lock
    register lock

.. This file was automatic generated / don't edit.

