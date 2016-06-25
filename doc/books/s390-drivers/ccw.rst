.. -*- coding: utf-8; mode: rst -*-

.. _ccw:

***********
The ccw bus
***********

The ccw bus typically contains the majority of devices available to a
s390 system. Named after the channel command word (ccw), the basic
command structure used to address its devices, the ccw bus contains
so-called channel attached devices. They are addressed via I/O
subchannels, visible on the css bus. A device driver for
channel-attached devices, however, will never interact with the
subchannel directly, but only via the I/O device on the ccw bus, the ccw
device.


.. _channelIO:

I/O functions for channel-attached devices
==========================================

Some hardware structures have been translated into C structures for use
by the common I/O layer and device drivers. For more information on the
hardware structures represented here, please consult the Principles of
Operation.


.. kernel-doc:: arch/s390/include/asm/cio.h
    :man-sect: 9
    :internal:


.. _ccwdev:

ccw devices
===========

Devices that want to initiate channel I/O need to attach to the ccw bus.
Interaction with the driver core is done via the common I/O layer, which
provides the abstractions of ccw devices and ccw device drivers.

The functions that initiate or terminate channel I/O all act upon a ccw
device structure. Device drivers must not bypass those functions or
strange side effects may happen.


.. kernel-doc:: arch/s390/include/asm/ccwdev.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/s390/cio/device.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/s390/cio/device_ops.c
    :man-sect: 9
    :export:


.. _cmf:

The channel-measurement facility
================================

The channel-measurement facility provides a means to collect measurement
data which is made available by the channel subsystem for each channel
attached device.


.. kernel-doc:: arch/s390/include/asm/cmb.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/s390/cio/cmf.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
