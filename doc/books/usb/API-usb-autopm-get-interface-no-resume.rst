
.. _API-usb-autopm-get-interface-no-resume:

==================================
usb_autopm_get_interface_no_resume
==================================

*man usb_autopm_get_interface_no_resume(9)*

*4.6.0-rc1*

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

This routine increments ``intf``'s usage counter but does not carry out an autoresume.

This routine can run in atomic context.
