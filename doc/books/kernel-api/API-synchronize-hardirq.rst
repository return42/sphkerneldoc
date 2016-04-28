.. -*- coding: utf-8; mode: rst -*-

.. _API-synchronize-hardirq:

===================
synchronize_hardirq
===================

*man synchronize_hardirq(9)*

*4.6.0-rc5*

wait for pending hard IRQ handlers (on other CPUs)


Synopsis
========

.. c:function:: bool synchronize_hardirq( unsigned int irq )

Arguments
=========

``irq``
    interrupt number to wait for


Description
===========

This function waits for any pending hard IRQ handlers for this interrupt
to complete before returning. If you use this function while holding a
resource the IRQ handler may need you will deadlock. It does not take
associated threaded handlers into account.

Do not use this for shutdown scenarios where you must be sure that all
parts (hardirq and threaded handler) have completed.


Returns
=======

false if a threaded handler is active.

This function may be called - with care - from IRQ context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
