.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-unregister-hw:

=======================
ieee80211_unregister_hw
=======================

*man ieee80211_unregister_hw(9)*

*4.6.0-rc5*

Unregister a hardware device


Synopsis
========

.. c:function:: void ieee80211_unregister_hw( struct ieee80211_hw * hw )

Arguments
=========

``hw``
    the hardware to unregister


Description
===========

This function instructs mac80211 to free allocated resources and
unregister netdevices from the networking subsystem.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
