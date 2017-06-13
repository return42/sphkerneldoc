.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/renesas/clk-mstp.c

.. _`mstp_clock_group`:

struct mstp_clock_group
=======================

.. c:type:: struct mstp_clock_group

    MSTP gating clocks group

.. _`mstp_clock_group.definition`:

Definition
----------

.. code-block:: c

    struct mstp_clock_group {
        struct clk_onecell_data data;
        void __iomem *smstpcr;
        void __iomem *mstpsr;
        spinlock_t lock;
        bool width_8bit;
    }

.. _`mstp_clock_group.members`:

Members
-------

data
    clocks in this group

smstpcr
    module stop control register

mstpsr
    module stop status register (optional)

lock
    protects writes to SMSTPCR

width_8bit
    registers are 8-bit, not 32-bit

.. _`mstp_clock`:

struct mstp_clock
=================

.. c:type:: struct mstp_clock

    MSTP gating clock

.. _`mstp_clock.definition`:

Definition
----------

.. code-block:: c

    struct mstp_clock {
        struct clk_hw hw;
        u32 bit_index;
        struct mstp_clock_group *group;
    }

.. _`mstp_clock.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

bit_index
    control bit index

group
    MSTP clocks group

.. This file was automatic generated / don't edit.

