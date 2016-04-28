.. -*- coding: utf-8; mode: rst -*-

.. _API-handle-percpu-irq:

=================
handle_percpu_irq
=================

*man handle_percpu_irq(9)*

*4.6.0-rc5*

Per CPU local irq handler


Synopsis
========

.. c:function:: void handle_percpu_irq( struct irq_desc * desc )

Arguments
=========

``desc``
    the interrupt description structure for this irq


Description
===========

Per CPU interrupts on SMP machines without locking requirements


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
