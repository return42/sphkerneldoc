.. -*- coding: utf-8; mode: rst -*-

###################################
Writing s390 channel device drivers
###################################

:author:    Huck Cornelia
:address:   cornelia.huck@de.ibm.com

**Copyright** 2007 : IBM Corp.

This documentation is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

For more details see the file COPYING in the source distribution of
Linux.


.. _intro:

************
Introduction
************

This document describes the interfaces available for device drivers that
drive s390 based channel attached I/O devices. This includes interfaces
for interaction with the hardware and interfaces for interacting with
the common driver core. Those interfaces are provided by the s390 common
I/O layer.

The document assumes a familarity with the technical terms associated
with the s390 channel I/O architecture. For a description of this
architecture, please refer to the "z/Architecture: Principles of
Operation", IBM publication no. SA22-7832.

While most I/O devices on a s390 system are typically driven through the
channel I/O mechanism described here, there are various other methods
(like the diag interface). These are out of the scope of this document.

Some additional information can also be found in the kernel source under
Documentation/s390/driver-model.txt.


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


.. _ccwgroup:

****************
The ccwgroup bus
****************

The ccwgroup bus only contains artificial devices, created by the user.
Many networking devices (e.g. qeth) are in fact composed of several ccw
devices (like read, write and data channel for qeth). The ccwgroup bus
provides a mechanism to create a meta-device which contains those ccw
devices as slave devices and can be associated with the netdevice.


.. _ccwgroupdevices:

ccw group devices
=================


.. kernel-doc:: arch/s390/include/asm/ccwgroup.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/s390/cio/ccwgroup.c
    :man-sect: 9
    :export:


.. _genericinterfaces:

******************
Generic interfaces
******************

Some interfaces are available to other drivers that do not necessarily
have anything to do with the busses described above, but still are
indirectly using basic infrastructure in the common I/O layer. One
example is the support for adapter interrupts.


.. kernel-doc:: drivers/s390/cio/airq.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------


.. only:: html

  Retrieval
  =========

  * :ref:`genindex`

.. todolist::

