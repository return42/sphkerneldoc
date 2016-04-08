
.. _API-rio-request-inb-mbox:

====================
rio_request_inb_mbox
====================

*man rio_request_inb_mbox(9)*

*4.6.0-rc1*

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

Requests ownership of an inbound mailbox resource and binds a callback function to the resource. Returns ``0`` on success.
