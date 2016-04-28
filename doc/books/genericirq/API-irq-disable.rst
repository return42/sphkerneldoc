.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-disable:

===========
irq_disable
===========

*man irq_disable(9)*

*4.6.0-rc5*

Mark interrupt disabled


Synopsis
========

.. c:function:: void irq_disable( struct irq_desc * desc )

Arguments
=========

``desc``
    irq descriptor which should be disabled


Description
===========

If the chip does not implement the irq_disable callback, we use a lazy
disable approach. That means we mark the interrupt disabled, but leave
the hardware unmasked. That's an optimization because we avoid the
hardware access for the common case where no interrupt happens after we
marked it disabled. If an interrupt happens, then the interrupt flow
handler masks the line at the hardware level and marks it pending.

If the interrupt chip does not implement the irq_disable callback, a
driver can disable the lazy approach for a particular irq line by
calling 'irq_set_status_flags(irq, IRQ_DISABLE_UNLAZY)'. This can
be used for devices which cannot disable the interrupt at the device
level under certain circumstances and have to use disable_irq[_nosync]
instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
