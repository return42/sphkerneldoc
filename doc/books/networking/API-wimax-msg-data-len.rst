.. -*- coding: utf-8; mode: rst -*-

.. _API-wimax-msg-data-len:

==================
wimax_msg_data_len
==================

*man wimax_msg_data_len(9)*

*4.6.0-rc5*

Return a pointer and size of a message's payload


Synopsis
========

.. c:function:: const void * wimax_msg_data_len( struct sk_buff * msg, size_t * size )

Arguments
=========

``msg``
    Pointer to a message created with ``wimax_msg_alloc``

``size``
    Pointer to where to store the message's size


Description
===========

Returns the pointer to the message data.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
