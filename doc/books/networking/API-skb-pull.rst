
.. _API-skb-pull:

========
skb_pull
========

*man skb_pull(9)*

*4.6.0-rc1*

remove data from the start of a buffer


Synopsis
========

.. c:function:: unsigned char ⋆ skb_pull( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to use

``len``
    amount of data to remove


Description
===========

This function removes data from the start of a buffer, returning the memory to the headroom. A pointer to the next data in the buffer is returned. Once the data has been pulled
future pushes will overwrite the old data.
