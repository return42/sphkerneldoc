.. -*- coding: utf-8; mode: rst -*-

.. _API-ioremap-nocache:

===============
ioremap_nocache
===============

*man ioremap_nocache(9)*

*4.6.0-rc5*

map bus memory into CPU space


Synopsis
========

.. c:function:: void __iomem * ioremap_nocache( resource_size_t offset, unsigned long size )

Arguments
=========

``offset``
    bus address of the memory

``size``
    size of the resource to map


Description
===========

ioremap performs a platform specific sequence of operations to make bus
memory CPU accessible via the readb/readw/readl/writeb/ writew/writel
functions and the other mmio helpers. The returned address is not
guaranteed to be usable directly as a virtual address.

If the area you are trying to map is a PCI BAR you should have a look at
``pci_iomap``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
