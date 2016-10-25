.. -*- coding: utf-8; mode: rst -*-

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




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
