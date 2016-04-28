.. -*- coding: utf-8; mode: rst -*-

.. _API-handle-edge-eoi-irq:

===================
handle_edge_eoi_irq
===================

*man handle_edge_eoi_irq(9)*

*4.6.0-rc5*

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

Similar as the above handle_edge_irq, but using eoi and w/o the
mask/unmask logic.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
