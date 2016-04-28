.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-iface-limit:

============================
struct ieee80211_iface_limit
============================

*man struct ieee80211_iface_limit(9)*

*4.6.0-rc5*

limit on certain interface types


Synopsis
========

.. code-block:: c

    struct ieee80211_iface_limit {
      u16 max;
      u16 types;
    };


Members
=======

max
    maximum number of interfaces of these types

types
    interface types (bits)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
