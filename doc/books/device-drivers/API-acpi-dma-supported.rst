.. -*- coding: utf-8; mode: rst -*-

.. _API-acpi-dma-supported:

==================
acpi_dma_supported
==================

*man acpi_dma_supported(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
