.. -*- coding: utf-8; mode: rst -*-

.. _API-wimax-msg-alloc:

===============
wimax_msg_alloc
===============

*man wimax_msg_alloc(9)*

*4.6.0-rc5*

Create a new skb for sending a message to userspace


Synopsis
========

.. c:function:: struct sk_buff * wimax_msg_alloc( struct wimax_dev * wimax_dev, const char * pipe_name, const void * msg, size_t size, gfp_t gfp_flags )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor

``pipe_name``
    "named pipe" the message will be sent to

``msg``
    pointer to the message data to send

``size``
    size of the message to send (in bytes), including the header.

``gfp_flags``
    flags for memory allocation.


Returns
=======

``0`` if ok, negative errno code on error


Description
===========

Allocates an skb that will contain the message to send to user space
over the messaging pipe and initializes it, copying the payload.

Once this call is done, you can deliver it with ``wimax_msg_send``.


IMPORTANT
=========

Don't use ``skb_push``/``skb_pull``/``skb_reserve`` on the skb, as
``wimax_msg_send`` depends on skb->data being placed at the beginning of
the user message.

Unlike other WiMAX stack calls, this call can be used way early, even
before ``wimax_dev_add`` is called, as long as the wimax_dev->net_dev
pointer is set to point to a proper net_dev. This is so that drivers
can use it early in case they need to send stuff around or communicate
with user space.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
