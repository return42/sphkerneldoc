.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/mxs/clk-div.c

.. _`clk_div`:

struct clk_div
==============

.. c:type:: struct clk_div

    mxs integer divider clock

.. _`clk_div.definition`:

Definition
----------

.. code-block:: c

    struct clk_div {
        struct clk_divider divider;
        const struct clk_ops *ops;
        void __iomem *reg;
        u8 busy;
    }

.. _`clk_div.members`:

Members
-------

divider
    the parent class

ops
    pointer to clk_ops of parent class

reg
    register address

busy
    busy bit shift

.. _`clk_div.description`:

Description
-----------

The mxs divider clock is a subclass of basic clk_divider with an
addtional busy bit.

.. This file was automatic generated / don't edit.

