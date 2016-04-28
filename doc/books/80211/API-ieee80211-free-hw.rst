.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-free-hw:

=================
ieee80211_free_hw
=================

*man ieee80211_free_hw(9)*

*4.6.0-rc5*

free hardware descriptor


Synopsis
========

.. c:function:: void ieee80211_free_hw( struct ieee80211_hw * hw )

Arguments
=========

``hw``
    the hardware to free


Description
===========

This function frees everything that was allocated, including the private
data for the driver. You must call ``ieee80211_unregister_hw`` before
calling this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
