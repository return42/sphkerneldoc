.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-irq-count:

==================
platform_irq_count
==================

*man platform_irq_count(9)*

*4.6.0-rc5*

Count the number of IRQs a platform device uses


Synopsis
========

.. c:function:: int platform_irq_count( struct platform_device * dev )

Arguments
=========

``dev``
    platform device


Return
======

Number of IRQs a platform device uses or EPROBE_DEFER


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
