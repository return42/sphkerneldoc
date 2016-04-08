
.. _API-wimax-msg-len:

=============
wimax_msg_len
=============

*man wimax_msg_len(9)*

*4.6.0-rc1*

Return a message's payload length


Synopsis
========

.. c:function:: ssize_t wimax_msg_len( struct sk_buff * msg )

Arguments
=========

``msg``
    Pointer to a message created with ``wimax_msg_alloc``
