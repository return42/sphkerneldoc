.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/mxs/clk-frac.c

.. _`clk_frac`:

struct clk_frac
===============

.. c:type:: struct clk_frac

    mxs fractional divider clock

.. _`clk_frac.definition`:

Definition
----------

.. code-block:: c

    struct clk_frac {
        struct clk_hw hw;
        void __iomem *reg;
        u8 shift;
        u8 width;
        u8 busy;
    }

.. _`clk_frac.members`:

Members
-------

hw
    clk_hw for the fractional divider clock

reg
    register address

shift
    the divider bit shift

width
    the divider bit width

busy
    busy bit shift

.. _`clk_frac.description`:

Description
-----------

The clock is an adjustable fractional divider with a busy bit to wait
when the divider is adjusted.

.. This file was automatic generated / don't edit.

