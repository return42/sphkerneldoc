.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-register-hw:

=====================
ieee80211_register_hw
=====================

*man ieee80211_register_hw(9)*

*4.6.0-rc5*

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

You must call this function before any other functions in mac80211. Note
that before a hardware can be registered, you need to fill the contained
wiphy's information.


Return
======

0 on success. An error code otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
