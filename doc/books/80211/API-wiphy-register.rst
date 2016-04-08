
.. _API-wiphy-register:

==============
wiphy_register
==============

*man wiphy_register(9)*

*4.6.0-rc1*

register a wiphy with cfg80211


Synopsis
========

.. c:function:: int wiphy_register( struct wiphy * wiphy )

Arguments
=========

``wiphy``
    The wiphy to register.


Return
======

A non-negative wiphy index or a negative error code.
