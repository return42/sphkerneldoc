.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-append-datato-frags:

=======================
skb_append_datato_frags
=======================

*man skb_append_datato_frags(9)*

*4.6.0-rc5*

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

This procedure append the user data in the fragment part of the skb if
any page alloc fails user this procedure returns -ENOMEM


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
