.. -*- coding: utf-8; mode: rst -*-

.. _usbcore:

=============
USB Core APIs
=============

There are two basic I/O models in the USB API. The most elemental one is
asynchronous: drivers submit requests in the form of an URB, and the
URB's completion callback handle the next step. All USB transfer types
support that model, although there are special cases for control URBs
(which always have setup and status stages, but may not have a data
stage) and isochronous URBs (which allow large packets and include
per-packet fault reports). Built on top of that is synchronous API
support, where a driver calls a routine that allocates one or more URBs,
submits them, and waits until they complete. There are synchronous
wrappers for single-buffer control and bulk transfers (which are awkward
to use in some driver disconnect scenarios), and for scatterlist based
streaming i/o (bulk or interrupt).

USB drivers need to provide buffers that can be used for DMA, although
they don't necessarily need to provide the DMA mapping themselves. There
are APIs to use used when allocating DMA buffers, which can prevent use
of bounce buffers on some systems. In some cases, drivers may be able to
rely on 64bit DMA to eliminate another kind of bounce buffer.


.. kernel-doc:: drivers/usb/core/urb.c
    :export:

.. kernel-doc:: drivers/usb/core/message.c
    :export:

.. kernel-doc:: drivers/usb/core/file.c
    :export:

.. kernel-doc:: drivers/usb/core/driver.c
    :export:

.. kernel-doc:: drivers/usb/core/usb.c
    :export:

.. kernel-doc:: drivers/usb/core/hub.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
