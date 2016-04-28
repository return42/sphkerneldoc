.. -*- coding: utf-8; mode: rst -*-

.. _API-wimax-msg-data:

==============
wimax_msg_data
==============

*man wimax_msg_data(9)*

*4.6.0-rc5*

Return a pointer to a message's payload


Synopsis
========

.. c:function:: const void * wimax_msg_data( struct sk_buff * msg )

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
