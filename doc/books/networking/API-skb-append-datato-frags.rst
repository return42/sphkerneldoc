
.. _API-skb-append-datato-frags:

=======================
skb_append_datato_frags
=======================

*man skb_append_datato_frags(9)*

*4.6.0-rc1*

append the user data to a skb


Synopsis
========

.. c:function:: int skb_append_datato_frags( struct sock * sk, struct sk_buff * skb, int (*getfrag) void *from, char *to, int offset, int len, int odd, struct sk_buff *skb, void * from, int length )

Arguments
=========

``sk``
    sock structure

``skb``
    skb structure to be appended with user data.

``getfrag``
    call back function to be used for getting the user data

``from``
    pointer to user message iov

``length``
    length of the iov message


Description
===========

This procedure append the user data in the fragment part of the skb if any page alloc fails user this procedure returns -ENOMEM
