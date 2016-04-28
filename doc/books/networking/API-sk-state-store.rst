.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-state-store:

==============
sk_state_store
==============

*man sk_state_store(9)*

*4.6.0-rc5*

update sk->sk_state


Synopsis
========

.. c:function:: void sk_state_store( struct sock * sk, int newstate )

Arguments
=========

``sk``
    socket pointer

``newstate``
    new state


Description
===========

Paired with ``sk_state_load``. Should be used in contexts where state
change might impact lockless readers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
