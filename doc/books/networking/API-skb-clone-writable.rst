
.. _API-skb-clone-writable:

==================
skb_clone_writable
==================

*man skb_clone_writable(9)*

*4.6.0-rc1*

is the header of a clone writable


Synopsis
========

.. c:function:: int skb_clone_writable( const struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to check

``len``
    length up to which to write


Description
===========

Returns true if modifying the header part of the cloned buffer does not requires the data to be copied.
