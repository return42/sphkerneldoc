.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-percpu-is-enabled:

=====================
irq_percpu_is_enabled
=====================

*man irq_percpu_is_enabled(9)*

*4.6.0-rc5*

Check whether the per cpu irq is enabled


Synopsis
========

.. c:function:: bool irq_percpu_is_enabled( unsigned int irq )

Arguments
=========

``irq``
    Linux irq number to check for


Description
===========

Must be called from a non migratable context. Returns the enable state
of a per cpu interrupt on the current cpu.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
