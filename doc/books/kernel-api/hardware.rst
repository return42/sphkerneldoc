.. -*- coding: utf-8; mode: rst -*-

.. _hardware:

*******************
Hardware Interfaces
*******************


Interrupt Handling
==================


.. kernel-doc:: kernel/irq/manage.c
    :export:

DMA Channels
============


.. kernel-doc:: kernel/dma.c
    :export:

Resources Management
====================


.. kernel-doc:: kernel/resource.c
    :internal:

.. kernel-doc:: kernel/resource.c
    :export:

MTRR Handling
=============


.. kernel-doc:: arch/x86/kernel/cpu/mtrr/main.c
    :export:

PCI Support Library
===================


.. kernel-doc:: drivers/pci/pci.c
    :export:

.. kernel-doc:: drivers/pci/pci-driver.c
    :export:

.. kernel-doc:: drivers/pci/remove.c
    :export:

.. kernel-doc:: drivers/pci/search.c
    :export:

.. kernel-doc:: drivers/pci/msi.c
    :export:

.. kernel-doc:: drivers/pci/bus.c
    :export:

.. kernel-doc:: drivers/pci/access.c
    :export:

.. kernel-doc:: drivers/pci/irq.c
    :export:

.. kernel-doc:: drivers/pci/htirq.c
    :export:

.. kernel-doc:: drivers/pci/probe.c
    :export:

.. kernel-doc:: drivers/pci/slot.c
    :export:

.. kernel-doc:: drivers/pci/rom.c
    :export:

.. kernel-doc:: drivers/pci/iov.c
    :export:

.. kernel-doc:: drivers/pci/pci-sysfs.c
    :internal:

PCI Hotplug Support Library
===========================


.. kernel-doc:: drivers/pci/hotplug/pci_hotplug_core.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
