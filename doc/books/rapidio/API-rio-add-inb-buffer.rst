
.. _API-rio-add-inb-buffer:

==================
rio_add_inb_buffer
==================

*man rio_add_inb_buffer(9)*

*4.6.0-rc1*

Add buffer to an inbound mailbox queue


Synopsis
========

.. c:function:: int rio_add_inb_buffer( struct rio_mport * mport, int mbox, void * buffer )

Arguments
=========

``mport``
    Master port containing the inbound mailbox

``mbox``
    The inbound mailbox number

``buffer``
    Pointer to the message buffer


Description
===========

Adds a buffer to an inbound mailbox queue for reception. Returns 0 on success.
