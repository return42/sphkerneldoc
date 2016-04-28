.. -*- coding: utf-8; mode: rst -*-

.. _API-handle-percpu-devid-irq:

=======================
handle_percpu_devid_irq
=======================

*man handle_percpu_devid_irq(9)*

*4.6.0-rc5*

Per CPU local irq handler with per cpu dev ids


Synopsis
========

.. c:function:: void handle_percpu_devid_irq( struct irq_desc * desc )

Arguments
=========

``desc``
    the interrupt description structure for this irq


Description
===========

Per CPU interrupts on SMP machines without locking requirements. Same as
``handle_percpu_irq`` above but with the following extras:

action->percpu_dev_id is a pointer to percpu variables which contain
the real device id for the cpu on which this handler is called


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
