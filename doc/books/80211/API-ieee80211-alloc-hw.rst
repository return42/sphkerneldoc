.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-alloc-hw:

==================
ieee80211_alloc_hw
==================

*man ieee80211_alloc_hw(9)*

*4.6.0-rc5*

Allocate a new hardware device


Synopsis
========

.. c:function:: struct ieee80211_hw * ieee80211_alloc_hw( size_t priv_data_len, const struct ieee80211_ops * ops )

Arguments
=========

``priv_data_len``
    length of private data

``ops``
    callbacks for this device


Description
===========

This must be called once for each hardware device. The returned pointer
must be used to refer to this device when calling other functions.
mac80211 allocates a private data area for the driver pointed to by
``priv`` in ``struct ieee80211_hw``, the size of this area is given as
``priv_data_len``.


Return
======

A pointer to the new hardware device, or ``NULL`` on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
