.. -*- coding: utf-8; mode: rst -*-

.. _API-wiphy-unregister:

================
wiphy_unregister
================

*man wiphy_unregister(9)*

*4.6.0-rc5*

deregister a wiphy from cfg80211


Synopsis
========

.. c:function:: void wiphy_unregister( struct wiphy * wiphy )

Arguments
=========

``wiphy``
    The wiphy to unregister.


Description
===========

After this call, no more requests can be made with this priv pointer,
but the call may sleep to wait for an outstanding request that is being
handled.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
