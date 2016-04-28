.. -*- coding: utf-8; mode: rst -*-

.. _API-dmam-declare-coherent-memory:

============================
dmam_declare_coherent_memory
============================

*man dmam_declare_coherent_memory(9)*

*4.6.0-rc5*

Managed ``dma_declare_coherent_memory``


Synopsis
========

.. c:function:: int dmam_declare_coherent_memory( struct device * dev, phys_addr_t phys_addr, dma_addr_t device_addr, size_t size, int flags )

Arguments
=========

``dev``
    Device to declare coherent memory for

``phys_addr``
    Physical address of coherent memory to be declared

``device_addr``
    Device address of coherent memory to be declared

``size``
    Size of coherent memory to be declared

``flags``
    Flags


Description
===========

Managed ``dma_declare_coherent_memory``.


RETURNS
=======

0 on success, -errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
