.. -*- coding: utf-8; mode: rst -*-

.. _API-handle-edge-irq:

===============
handle_edge_irq
===============

*man handle_edge_irq(9)*

*4.6.0-rc5*

edge type IRQ handler


Synopsis
========

.. c:function:: void handle_edge_irq( struct irq_desc * desc )

Arguments
=========

``desc``
    the interrupt description structure for this irq


Description
===========

Interrupt occures on the falling and/or rising edge of a hardware
signal. The occurrence is latched into the irq controller hardware and
must be acked in order to be reenabled. After the ack another interrupt
can happen on the same source even before the first one is handled by
the associated event handler. If this happens it might be necessary to
disable (mask) the interrupt depending on the controller hardware. This
requires to reenable the interrupt inside of the loop which handles the
interrupts which have arrived while the handler was running. If all
pending interrupts are handled, the loop is left.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
