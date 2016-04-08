
.. _API-wimax-msg-data:

==============
wimax_msg_data
==============

*man wimax_msg_data(9)*

*4.6.0-rc1*

Return a pointer to a message's payload


Synopsis
========

.. c:function:: const void ⋆ wimax_msg_data( struct sk_buff * msg )

Arguments
=========

``msg``
    Pointer to a message created with ``wimax_msg_alloc``
