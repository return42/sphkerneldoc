.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-event:

=========
hsi_event
=========

*man hsi_event(9)*

*4.6.0-rc5*

Notifies clients about port events


Synopsis
========

.. c:function:: int hsi_event( struct hsi_port * port, unsigned long event )

Arguments
=========

``port``
    Port where the event occurred

``event``
    The event type


Description
===========

Clients should not be concerned about wake line behavior. However, due
to a race condition in HSI HW protocol, clients need to be notified
about wake line changes, so they can implement a workaround for it.


Events
======

HSI_EVENT_START_RX - Incoming wake line high HSI_EVENT_STOP_RX -
Incoming wake line down

Returns -errno on error, or 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
