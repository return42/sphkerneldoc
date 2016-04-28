.. -*- coding: utf-8; mode: rst -*-

.. _API-handle-fasteoi-irq:

==================
handle_fasteoi_irq
==================

*man handle_fasteoi_irq(9)*

*4.6.0-rc5*

irq handler for transparent controllers


Synopsis
========

.. c:function:: void handle_fasteoi_irq( struct irq_desc * desc )

Arguments
=========

``desc``
    the interrupt description structure for this irq


Only a single callback will be issued to the chip
=================================================

an ->``eoi`` call when the interrupt has been serviced. This enables
support for modern forms of interrupt handlers, which handle the flow
details in hardware, transparently.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
