
.. _API-acpi-get-dma-attr:

=================
acpi_get_dma_attr
=================

*man acpi_get_dma_attr(9)*

*4.6.0-rc1*

Check the supported DMA attr for the specified device.


Synopsis
========

.. c:function:: enum dev_dma_attr acpi_get_dma_attr( struct acpi_device * adev )

Arguments
=========

``adev``
    The pointer to acpi device


Description
===========

Return enum dev_dma_attr.
