.. -*- coding: utf-8; mode: rst -*-

.. _hardware:

*******************
Hardware Interfaces
*******************


Interrupt Handling
==================


.. kernel-doc:: kernel/irq/manage.c
    :man-sect: 9
    :export:


DMA Channels
============


.. kernel-doc:: kernel/dma.c
    :man-sect: 9
    :export:


Resources Management
====================


.. kernel-doc:: kernel/resource.c
    :man-sect: 9
    :internal:


.. kernel-doc:: kernel/resource.c
    :man-sect: 9
    :export:


MTRR Handling
=============


.. kernel-doc:: arch/x86/kernel/cpu/mtrr/main.c
    :man-sect: 9
    :export:


PCI Support Library
===================


.. kernel-doc:: drivers/pci/pci.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/pci-driver.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/remove.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/search.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/msi.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/bus.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/access.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/irq.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/htirq.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/probe.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/slot.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/rom.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/iov.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pci/pci-sysfs.c
    :man-sect: 9
    :internal:


PCI Hotplug Support Library
===========================


.. kernel-doc:: drivers/pci/hotplug/pci_hotplug_core.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
