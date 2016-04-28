.. -*- coding: utf-8; mode: rst -*-

.. _API-disable-irq-nosync:

==================
disable_irq_nosync
==================

*man disable_irq_nosync(9)*

*4.6.0-rc5*

disable an irq without waiting


Synopsis
========

.. c:function:: void disable_irq_nosync( unsigned int irq )

Arguments
=========

``irq``
    Interrupt to disable


Description
===========

Disable the selected interrupt line. Disables and Enables are nested.
Unlike ``disable_irq``, this function does not ensure existing instances
of the IRQ handler have completed before returning.

This function may be called from IRQ context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
