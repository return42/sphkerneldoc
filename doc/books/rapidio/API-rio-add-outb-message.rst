
.. _API-rio-add-outb-message:

====================
rio_add_outb_message
====================

*man rio_add_outb_message(9)*

*4.6.0-rc1*

Add RIO message to an outbound mailbox queue


Synopsis
========

.. c:function:: int rio_add_outb_message( struct rio_mport * mport, struct rio_dev * rdev, int mbox, void * buffer, size_t len )

Arguments
=========

``mport``
    RIO master port containing the outbound queue

``rdev``
    RIO device the message is be sent to

``mbox``
    The outbound mailbox queue

``buffer``
    Pointer to the message buffer

``len``
    Length of the message buffer


Description
===========

Adds a RIO message buffer to an outbound mailbox queue for transmission. Returns 0 on success.
