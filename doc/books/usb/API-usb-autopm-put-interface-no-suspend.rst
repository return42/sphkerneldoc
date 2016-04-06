
.. _API-usb-autopm-put-interface-no-suspend:

===================================
usb_autopm_put_interface_no_suspend
===================================

*man usb_autopm_put_interface_no_suspend(9)*

*4.6.0-rc1*

decrement a USB interface's PM-usage counter


Synopsis
========

.. c:function:: void usb_autopm_put_interface_no_suspend( struct usb_interface * intf )

Arguments
=========

``intf``
    the usb_interface whose counter should be decremented


Description
===========

This routine decrements ``intf``'s usage counter but does not carry out an autosuspend.

This routine can run in atomic context.
