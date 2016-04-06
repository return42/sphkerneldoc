
.. _API-usb-anchor-resume-wakeups:

=========================
usb_anchor_resume_wakeups
=========================

*man usb_anchor_resume_wakeups(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: void usb_anchor_resume_wakeups( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    the anchor you want to resume wakeups on


Description
===========

Allow usb_wait_anchor_empty_timeout waiters to be woken up again, and wake up any current waiters if the anchor is empty.
