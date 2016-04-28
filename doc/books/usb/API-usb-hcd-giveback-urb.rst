.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-hcd-giveback-urb:

====================
usb_hcd_giveback_urb
====================

*man usb_hcd_giveback_urb(9)*

*4.6.0-rc5*

return URB from HCD to device driver


Synopsis
========

.. c:function:: void usb_hcd_giveback_urb( struct usb_hcd * hcd, struct urb * urb, int status )

Arguments
=========

``hcd``
    host controller returning the URB

``urb``
    urb being returned to the USB device driver.

``status``
    completion status code for the URB.


Context
=======

``in_interrupt``


Description
===========

This hands the URB from HCD to its USB device driver, using its
completion function. The HCD has freed all per-urb resources (and is
done using urb->hcpriv). It also released all HCD locks; the device
driver won't cause problems if it frees, modifies, or resubmits this
URB.

If ``urb`` was unlinked, the value of ``status`` will be overridden by
``urb``->unlinked. Erroneous short transfers are detected in case the
HCD hasn't checked for them.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
