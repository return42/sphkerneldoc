.. -*- coding: utf-8; mode: rst -*-

.. _intro:

************
Introduction
************

The generic interrupt handling layer is designed to provide a complete
abstraction of interrupt handling for device drivers. It is able to
handle all the different types of interrupt controller hardware. Device
drivers use generic API functions to request, enable, disable and free
interrupts. The drivers do not have to know anything about interrupt
hardware details, so they can be used on different platforms without
code changes.

This documentation is provided to developers who want to implement an
interrupt subsystem based for their architecture, with the help of the
generic IRQ handling layer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
