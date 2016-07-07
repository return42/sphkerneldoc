.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/imx/clk-fixup-div.c

.. _`clk_fixup_div`:

struct clk_fixup_div
====================

.. c:type:: struct clk_fixup_div

    imx integer fixup divider clock

.. _`clk_fixup_div.definition`:

Definition
----------

.. code-block:: c

    struct clk_fixup_div {
        struct clk_divider divider;
        const struct clk_ops *ops;
        void (* fixup) (u32 *val);
    }

.. _`clk_fixup_div.members`:

Members
-------

divider
    the parent class

ops
    pointer to clk_ops of parent class

fixup
    a hook to fixup the write value

.. _`clk_fixup_div.description`:

Description
-----------

The imx fixup divider clock is a subclass of basic clk_divider
with an addtional fixup hook.

.. This file was automatic generated / don't edit.

