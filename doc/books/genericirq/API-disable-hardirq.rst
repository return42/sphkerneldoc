.. -*- coding: utf-8; mode: rst -*-

.. _API-disable-hardirq:

===============
disable_hardirq
===============

*man disable_hardirq(9)*

*4.6.0-rc5*

disables an irq and waits for hardirq completion


Synopsis
========

.. c:function:: bool disable_hardirq( unsigned int irq )

Arguments
=========

``irq``
    Interrupt to disable


Description
===========

Disable the selected interrupt line. Enables and Disables are nested.
This function waits for any pending hard IRQ handlers for this interrupt
to complete before returning. If you use this function while holding a
resource the hard IRQ handler may need you will deadlock.

When used to optimistically disable an interrupt from atomic context the
return value must be checked.


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
