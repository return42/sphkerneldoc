.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/imx/clk-fixup-mux.c

.. _`clk_fixup_mux`:

struct clk_fixup_mux
====================

.. c:type:: struct clk_fixup_mux

    imx integer fixup multiplexer clock

.. _`clk_fixup_mux.definition`:

Definition
----------

.. code-block:: c

    struct clk_fixup_mux {
        struct clk_mux mux;
        const struct clk_ops *ops;
        void (* fixup) (u32 *val);
    }

.. _`clk_fixup_mux.members`:

Members
-------

mux
    the parent class

ops
    pointer to clk_ops of parent class

fixup
    a hook to fixup the write value

.. _`clk_fixup_mux.description`:

Description
-----------

The imx fixup multiplexer clock is a subclass of basic clk_mux
with an addtional fixup hook.

.. This file was automatic generated / don't edit.

