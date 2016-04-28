.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-calc-bus-time:

=================
usb_calc_bus_time
=================

*man usb_calc_bus_time(9)*

*4.6.0-rc5*

approximate periodic transaction time in nanoseconds


Synopsis
========

.. c:function:: long usb_calc_bus_time( int speed, int is_input, int isoc, int bytecount )

Arguments
=========

``speed``
    from dev->speed; USB_SPEED_{LOW,FULL,HIGH}

``is_input``
    true iff the transaction sends data to the host

``isoc``
    true for isochronous transactions, false for interrupt ones

``bytecount``
    how many bytes in the transaction.


Return
======

Approximate bus time in nanoseconds for a periodic transaction.


Note
====

See USB 2.0 spec section 5.11.3; only periodic transfers need to be
scheduled in software, this function is only used for such scheduling.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
