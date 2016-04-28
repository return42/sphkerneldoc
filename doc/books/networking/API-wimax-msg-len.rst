.. -*- coding: utf-8; mode: rst -*-

.. _API-wimax-msg-len:

=============
wimax_msg_len
=============

*man wimax_msg_len(9)*

*4.6.0-rc5*

Return a message's payload length


Synopsis
========

.. c:function:: ssize_t wimax_msg_len( struct sk_buff * msg )

Arguments
=========

``msg``
    Pointer to a message created with ``wimax_msg_alloc``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
