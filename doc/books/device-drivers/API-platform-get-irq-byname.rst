.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-get-irq-byname:

=======================
platform_get_irq_byname
=======================

*man platform_get_irq_byname(9)*

*4.6.0-rc5*

get an IRQ for a device by name


Synopsis
========

.. c:function:: int platform_get_irq_byname( struct platform_device * dev, const char * name )

Arguments
=========

``dev``
    platform device

``name``
    IRQ name


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
