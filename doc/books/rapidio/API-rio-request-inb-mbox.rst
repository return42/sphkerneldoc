.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-request-inb-mbox:

====================
rio_request_inb_mbox
====================

*man rio_request_inb_mbox(9)*

*4.6.0-rc5*

request inbound mailbox service


Synopsis
========

.. c:function:: int rio_request_inb_mbox( struct rio_mport * mport, void * dev_id, int mbox, int entries, void (*minb) struct rio_mport * mport, void *dev_id, int mbox, int slot )

Arguments
=========

``mport``
    RIO master port from which to allocate the mailbox resource

``dev_id``
    Device specific pointer to pass on event

``mbox``
    Mailbox number to claim

``entries``
    Number of entries in inbound mailbox queue

``minb``
    Callback to execute when inbound message is received


Description
===========

Requests ownership of an inbound mailbox resource and binds a callback
function to the resource. Returns ``0`` on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
