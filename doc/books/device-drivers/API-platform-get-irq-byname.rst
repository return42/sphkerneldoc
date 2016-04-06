
.. _API-platform-get-irq-byname:

=======================
platform_get_irq_byname
=======================

*man platform_get_irq_byname(9)*

*4.6.0-rc1*

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
