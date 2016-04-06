
.. _API-acpi-dma-supported:

==================
acpi_dma_supported
==================

*man acpi_dma_supported(9)*

*4.6.0-rc1*

Check DMA support for the specified device.


Synopsis
========

.. c:function:: bool acpi_dma_supported( struct acpi_device * adev )

Arguments
=========

``adev``
    The pointer to acpi device


Description
===========

Return false if DMA is not supported. Otherwise, return true
