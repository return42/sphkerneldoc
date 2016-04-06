
.. _API-usb-anchor-suspend-wakeups:

==========================
usb_anchor_suspend_wakeups
==========================

*man usb_anchor_suspend_wakeups(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: void usb_anchor_suspend_wakeups( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    the anchor you want to suspend wakeups on


Description
===========

Call this to stop the last urb being unanchored from waking up any usb_wait_anchor_empty_timeout waiters. This is used in the hcd urb give- back path to delay waking up until
after the completion handler has run.
