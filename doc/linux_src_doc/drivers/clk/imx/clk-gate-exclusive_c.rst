.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/imx/clk-gate-exclusive.c

.. _`clk_gate_exclusive`:

struct clk_gate_exclusive
=========================

.. c:type:: struct clk_gate_exclusive

    i.MX specific gate clock which is mutually exclusive with other gate clocks

.. _`clk_gate_exclusive.definition`:

Definition
----------

.. code-block:: c

    struct clk_gate_exclusive {
        struct clk_gate gate;
        u32 exclusive_mask;
    }

.. _`clk_gate_exclusive.members`:

Members
-------

gate
    the parent class

exclusive_mask
    mask of gate bits which are mutually exclusive to this
    gate clock

.. _`clk_gate_exclusive.description`:

Description
-----------

The imx exclusive gate clock is a subclass of basic clk_gate
with an addtional mask to indicate which other gate bits in the same
register is mutually exclusive to this gate clock.

.. This file was automatic generated / don't edit.

