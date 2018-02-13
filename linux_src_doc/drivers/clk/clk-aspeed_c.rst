.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-aspeed.c

.. _`aspeed_gate_data`:

struct aspeed_gate_data
=======================

.. c:type:: struct aspeed_gate_data

    Aspeed gated clocks

.. _`aspeed_gate_data.definition`:

Definition
----------

.. code-block:: c

    struct aspeed_gate_data {
        u8 clock_idx;
        s8 reset_idx;
        const char *name;
        const char *parent_name;
        unsigned long flags;
    }

.. _`aspeed_gate_data.members`:

Members
-------

clock_idx
    bit used to gate this clock in the clock register

reset_idx
    bit used to reset this IP in the reset register. -1 if no
    reset is required when enabling the clock

name
    the clock name

parent_name
    the name of the parent clock

flags
    standard clock framework flags

.. _`aspeed_clk_gate`:

struct aspeed_clk_gate
======================

.. c:type:: struct aspeed_clk_gate

    Aspeed specific clk_gate structure

.. _`aspeed_clk_gate.definition`:

Definition
----------

.. code-block:: c

    struct aspeed_clk_gate {
        struct clk_hw hw;
        struct regmap *map;
        u8 clock_idx;
        s8 reset_idx;
        u8 flags;
        spinlock_t *lock;
    }

.. _`aspeed_clk_gate.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

map
    *undescribed*

clock_idx
    bit used to gate this clock in the clock register

reset_idx
    bit used to reset this IP in the reset register. -1 if no
    reset is required when enabling the clock

flags
    hardware-specific flags

lock
    register lock

.. _`aspeed_clk_gate.description`:

Description
-----------

Some of the clocks in the Aspeed SoC must be put in reset before enabling.
This modified version of clk_gate allows an optional reset bit to be
specified.

.. _`aspeed_reset`:

struct aspeed_reset
===================

.. c:type:: struct aspeed_reset

    Aspeed reset controller

.. _`aspeed_reset.definition`:

Definition
----------

.. code-block:: c

    struct aspeed_reset {
        struct regmap *map;
        struct reset_controller_dev rcdev;
    }

.. _`aspeed_reset.members`:

Members
-------

map
    regmap to access the containing system controller

rcdev
    reset controller device

.. This file was automatic generated / don't edit.

