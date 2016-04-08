
.. _API-ieee80211-register-hw:

=====================
ieee80211_register_hw
=====================

*man ieee80211_register_hw(9)*

*4.6.0-rc1*

Register hardware device


Synopsis
========

.. c:function:: int ieee80211_register_hw( struct ieee80211_hw * hw )

Arguments
=========

``hw``
    the device to register as returned by ``ieee80211_alloc_hw``


Description
===========

You must call this function before any other functions in mac80211. Note that before a hardware can be registered, you need to fill the contained wiphy's information.


Return
======

0 on success. An error code otherwise.
