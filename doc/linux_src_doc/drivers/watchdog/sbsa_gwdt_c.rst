.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/sbsa_gwdt.c

.. _`sbsa_gwdt`:

struct sbsa_gwdt
================

.. c:type:: struct sbsa_gwdt

    Internal representation of the SBSA GWDT

.. _`sbsa_gwdt.definition`:

Definition
----------

.. code-block:: c

    struct sbsa_gwdt {
        struct watchdog_device wdd;
        u32 clk;
        void __iomem *refresh_base;
        void __iomem *control_base;
    }

.. _`sbsa_gwdt.members`:

Members
-------

wdd
    kernel watchdog_device structure

clk
    store the System Counter clock frequency, in Hz.

refresh_base
    Virtual address of the watchdog refresh frame

control_base
    Virtual address of the watchdog control frame

.. This file was automatic generated / don't edit.

