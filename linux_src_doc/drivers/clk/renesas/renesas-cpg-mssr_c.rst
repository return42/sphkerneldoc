.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/renesas/renesas-cpg-mssr.c

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
        u32 index;
        struct cpg_mssr_priv *priv;
    }

.. _`mstp_clock.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

index
    MSTP clock number

priv
    CPG/MSSR private data

.. This file was automatic generated / don't edit.

