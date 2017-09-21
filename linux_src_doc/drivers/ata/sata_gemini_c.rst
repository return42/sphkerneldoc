.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/sata_gemini.c

.. _`sata_gemini`:

struct sata_gemini
==================

.. c:type:: struct sata_gemini

    a state container for a Gemini SATA bridge

.. _`sata_gemini.definition`:

Definition
----------

.. code-block:: c

    struct sata_gemini {
        struct device *dev;
        void __iomem *base;
        enum gemini_muxmode muxmode;
        bool ide_pins;
        bool sata_bridge;
        struct reset_control *sata0_reset;
        struct reset_control *sata1_reset;
        struct clk *sata0_pclk;
        struct clk *sata1_pclk;
    }

.. _`sata_gemini.members`:

Members
-------

dev
    the containing device

base
    remapped I/O memory base

muxmode
    the current muxing mode

ide_pins
    if the device is using the plain IDE interface pins

sata_bridge
    if the device enables the SATA bridge

sata0_reset
    SATA0 reset handler

sata1_reset
    SATA1 reset handler

sata0_pclk
    SATA0 PCLK handler

sata1_pclk
    SATA1 PCLK handler

.. This file was automatic generated / don't edit.

