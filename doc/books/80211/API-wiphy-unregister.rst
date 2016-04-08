
.. _API-wiphy-unregister:

================
wiphy_unregister
================

*man wiphy_unregister(9)*

*4.6.0-rc1*

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

After this call, no more requests can be made with this priv pointer, but the call may sleep to wait for an outstanding request that is being handled.
