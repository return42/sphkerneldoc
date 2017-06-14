.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/bcm/clk-bcm2835.c

.. _`bcm2835-cprman--clock-manager-for-the--audio--domain-`:

BCM2835 CPRMAN (clock manager for the "audio" domain)
=====================================================

The clock tree on the 2835 has several levels.  There's a root
oscillator running at 19.2Mhz.  After the oscillator there are 5
PLLs, roughly divided as "camera", "ARM", "core", "DSI displays",
and "HDMI displays".  Those 5 PLLs each can divide their output to
produce up to 4 channels.  Finally, there is the level of clocks to
be consumed by other hardware components (like "H264" or "HDMI
state machine"), which divide off of some subset of the PLL
channels.

All of the clocks in the tree are exposed in the DT, because the DT
may want to make assignments of the final layer of clocks to the
PLL channels, and some components of the hardware will actually
skip layers of the tree (for example, the pixel clock comes
directly from the PLLH PIX channel without using a CM\_\*CTL clock
generator).

.. This file was automatic generated / don't edit.

