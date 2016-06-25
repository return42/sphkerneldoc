.. -*- coding: utf-8; mode: rst -*-

.. _devdrivers:

*****************************
Device drivers infrastructure
*****************************


The Basic Device Driver-Model Structures
========================================


.. kernel-doc:: include/linux/device.h
    :man-sect: 9
    :internal:


Device Drivers Base
===================


.. kernel-doc:: drivers/base/init.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/base/driver.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/base/core.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/base/syscore.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/base/class.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/base/node.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/base/firmware_class.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/base/transport_class.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/base/dd.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/platform_device.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/base/platform.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/base/bus.c
    :man-sect: 9
    :export:


Buffer Sharing and Synchronization
==================================

The dma-buf subsystem provides the framework for sharing buffers for
hardware (DMA) access across multiple device drivers and subsystems, and
for synchronizing asynchronous hardware access.

This is used, for example, by drm "prime" multi-GPU support, but is of
course not limited to GPU use cases.

The three main components of this are: (1) dma-buf, representing a
sg_table and exposed to userspace as a file descriptor to allow passing
between devices, (2) fence, which provides a mechanism to signal when
one device as finished access, and (3) reservation, which manages the
shared or exclusive fence(s) associated with the buffer.


dma-buf
-------


.. kernel-doc:: drivers/dma-buf/dma-buf.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/dma-buf.h
    :man-sect: 9
    :internal:


reservation
-----------


.. kernel-doc:: drivers/dma-buf/reservation.c
    :man-sect: 9
    :doc: Reservation Object Overview


.. kernel-doc:: drivers/dma-buf/reservation.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/reservation.h
    :man-sect: 9
    :internal:


fence
-----


.. kernel-doc:: drivers/dma-buf/fence.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/fence.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/dma-buf/seqno-fence.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/seqno-fence.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/dma-buf/sync_file.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/sync_file.h
    :man-sect: 9
    :internal:


Device Drivers DMA Management
=============================


.. kernel-doc:: drivers/base/dma-coherent.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/base/dma-mapping.c
    :man-sect: 9
    :export:


Device Drivers Power Management
===============================


.. kernel-doc:: drivers/base/power/main.c
    :man-sect: 9
    :export:


Device Drivers ACPI Support
===========================


.. kernel-doc:: drivers/acpi/scan.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/acpi/scan.c
    :man-sect: 9
    :internal:


Device drivers PnP support
==========================


.. kernel-doc:: drivers/pnp/core.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/pnp/card.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pnp/driver.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/pnp/manager.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/pnp/support.c
    :man-sect: 9
    :export:


Userspace IO devices
====================


.. kernel-doc:: drivers/uio/uio.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/uio_driver.h
    :man-sect: 9
    :internal:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
