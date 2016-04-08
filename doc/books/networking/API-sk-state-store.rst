
.. _API-sk-state-store:

==============
sk_state_store
==============

*man sk_state_store(9)*

*4.6.0-rc1*

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

Paired with ``sk_state_load``. Should be used in contexts where state change might impact lockless readers.
