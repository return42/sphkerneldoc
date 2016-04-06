
.. _API-usb-alloc-urb:

=============
usb_alloc_urb
=============

*man usb_alloc_urb(9)*

*4.6.0-rc1*

creates a new urb for a USB driver to use


Synopsis
========

.. c:function:: struct urb ⋆ usb_alloc_urb( int iso_packets, gfp_t mem_flags )

Arguments
=========

``iso_packets``
    number of iso packets for this urb

``mem_flags``
    the type of memory to allocate, see ``kmalloc`` for a list of valid options for this.


Description
===========

Creates an urb for the USB driver to use, initializes a few internal structures, increments the usage counter, and returns a pointer to it.

If the driver want to use this urb for interrupt, control, or bulk endpoints, pass '0' as the number of iso packets.

The driver must call ``usb_free_urb`` when it is finished with the urb.


Return
======

A pointer to the new urb, or ``NULL`` if no memory is available.
