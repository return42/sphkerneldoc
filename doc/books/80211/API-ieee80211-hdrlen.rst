
.. _API-ieee80211-hdrlen:

================
ieee80211_hdrlen
================

*man ieee80211_hdrlen(9)*

*4.6.0-rc1*

get header length in bytes from frame control


Synopsis
========

.. c:function:: unsigned int __attribute_const__ ieee80211_hdrlen( __le16 fc )

Arguments
=========

``fc``
    frame control field in little-endian format


Return
======

The header length in bytes.
