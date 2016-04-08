
.. _API-handle-fasteoi-irq:

==================
handle_fasteoi_irq
==================

*man handle_fasteoi_irq(9)*

*4.6.0-rc1*

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

an ->``eoi`` call when the interrupt has been serviced. This enables support for modern forms of interrupt handlers, which handle the flow details in hardware, transparently.
