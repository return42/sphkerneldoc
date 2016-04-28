.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-altnum-to-altsetting:

========================
usb_altnum_to_altsetting
========================

*man usb_altnum_to_altsetting(9)*

*4.6.0-rc5*

get the altsetting structure with a given alternate setting number.


Synopsis
========

.. c:function:: struct usb_host_interface * usb_altnum_to_altsetting( const struct usb_interface * intf, unsigned int altnum )

Arguments
=========

``intf``
    the interface containing the altsetting in question

``altnum``
    the desired alternate setting number


Description
===========

This searches the altsetting array of the specified interface for an
entry with the correct bAlternateSetting value.

Note that altsettings need not be stored sequentially by number, so it
would be incorrect to assume that the first altsetting entry in the
array corresponds to altsetting zero. This routine helps device drivers
avoid such mistakes.

Don't call this function unless you are bound to the intf interface or
you have locked the device!


Return
======

A pointer to the entry of the altsetting array of ``intf`` that has
``altnum`` as the alternate setting number. ``NULL`` if not found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
