
.. _API-platform-irq-count:

==================
platform_irq_count
==================

*man platform_irq_count(9)*

*4.6.0-rc1*

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
