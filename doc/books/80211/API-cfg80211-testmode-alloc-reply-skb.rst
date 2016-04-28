.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-testmode-alloc-reply-skb:

=================================
cfg80211_testmode_alloc_reply_skb
=================================

*man cfg80211_testmode_alloc_reply_skb(9)*

*4.6.0-rc5*

allocate testmode reply


Synopsis
========

.. c:function:: struct sk_buff * cfg80211_testmode_alloc_reply_skb( struct wiphy * wiphy, int approxlen )

Arguments
=========

``wiphy``
    the wiphy

``approxlen``
    an upper bound of the length of the data that will be put into the
    skb


Description
===========

This function allocates and pre-fills an skb for a reply to the testmode
command. Since it is intended for a reply, calling it outside of the
``testmode_cmd`` operation is invalid.

The returned skb is pre-filled with the wiphy index and set up in a way
that any data that is put into the skb (with ``skb_put``, ``nla_put`` or
similar) will end up being within the ``NL80211_ATTR_TESTDATA``
attribute, so all that needs to be done with the skb is adding data for
the corresponding userspace tool which can then read that data out of
the testdata attribute. You must not modify the skb in any other way.

When done, call ``cfg80211_testmode_reply`` with the skb and return its
error code as the result of the ``testmode_cmd`` operation.


Return
======

An allocated and pre-filled skb. ``NULL`` if any errors happen.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
