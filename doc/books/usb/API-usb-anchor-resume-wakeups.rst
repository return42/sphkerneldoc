.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-anchor-resume-wakeups:

=========================
usb_anchor_resume_wakeups
=========================

*man usb_anchor_resume_wakeups(9)*

*4.6.0-rc5*


Synopsis
========

.. c:function:: void usb_anchor_resume_wakeups( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    the anchor you want to resume wakeups on


Description
===========

Allow usb_wait_anchor_empty_timeout waiters to be woken up again,
and wake up any current waiters if the anchor is empty.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
