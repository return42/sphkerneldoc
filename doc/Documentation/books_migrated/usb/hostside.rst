.. -*- coding: utf-8; mode: rst -*-

.. _hostside:

*******************************
Host-Side Data Types and Macros
*******************************

The host side API exposes several layers to drivers, some of which are
more necessary than others. These support lifecycle models for host side
drivers and devices, and support passing buffers through usbcore to some
HCD that performs the I/O for the device driver.


.. kernel-doc:: include/linux/usb.h
    :man-sect: 9
    :internal:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
