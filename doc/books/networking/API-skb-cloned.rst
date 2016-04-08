
.. _API-skb-cloned:

==========
skb_cloned
==========

*man skb_cloned(9)*

*4.6.0-rc1*

is the buffer a clone


Synopsis
========

.. c:function:: int skb_cloned( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Returns true if the buffer was generated with ``skb_clone`` and is one of multiple shared copies of the buffer. Cloned buffers are shared data so must not be written to under
normal circumstances.
