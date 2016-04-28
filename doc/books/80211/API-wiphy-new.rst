.. -*- coding: utf-8; mode: rst -*-

.. _API-wiphy-new:

=========
wiphy_new
=========

*man wiphy_new(9)*

*4.6.0-rc5*

create a new wiphy for use with cfg80211


Synopsis
========

.. c:function:: struct wiphy * wiphy_new( const struct cfg80211_ops * ops, int sizeof_priv )

Arguments
=========

``ops``
    The configuration operations for this device

``sizeof_priv``
    The size of the private area to allocate


Description
===========

Create a new wiphy and associate the given operations with it.
``sizeof_priv`` bytes are allocated for private use.


Return
======

A pointer to the new wiphy. This pointer must be assigned to each
netdev's ieee80211_ptr for proper operation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
