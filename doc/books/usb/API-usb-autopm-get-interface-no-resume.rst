.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-autopm-get-interface-no-resume:

==================================
usb_autopm_get_interface_no_resume
==================================

*man usb_autopm_get_interface_no_resume(9)*

*4.6.0-rc5*

increment a USB interface's PM-usage counter


Synopsis
========

.. c:function:: void usb_autopm_get_interface_no_resume( struct usb_interface * intf )

Arguments
=========

``intf``
    the usb_interface whose counter should be incremented


Description
===========

This routine increments ``intf``'s usage counter but does not carry out
an autoresume.

This routine can run in atomic context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
