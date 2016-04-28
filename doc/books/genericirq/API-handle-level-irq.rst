.. -*- coding: utf-8; mode: rst -*-

.. _API-handle-level-irq:

================
handle_level_irq
================

*man handle_level_irq(9)*

*4.6.0-rc5*

Level type irq handler


Synopsis
========

.. c:function:: void handle_level_irq( struct irq_desc * desc )

Arguments
=========

``desc``
    the interrupt description structure for this irq


Description
===========

Level type interrupts are active as long as the hardware line has the
active level. This may require to mask the interrupt and unmask it after
the associated handler has acknowledged the device, so the interrupt
line is back to inactive.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
