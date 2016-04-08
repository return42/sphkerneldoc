
.. _API-handle-edge-eoi-irq:

===================
handle_edge_eoi_irq
===================

*man handle_edge_eoi_irq(9)*

*4.6.0-rc1*

edge eoi type IRQ handler


Synopsis
========

.. c:function:: void handle_edge_eoi_irq( struct irq_desc * desc )

Arguments
=========

``desc``
    the interrupt description structure for this irq


Description
===========

Similar as the above handle_edge_irq, but using eoi and w/o the mask/unmask logic.
