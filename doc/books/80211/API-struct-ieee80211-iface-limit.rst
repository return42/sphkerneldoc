
.. _API-struct-ieee80211-iface-limit:

============================
struct ieee80211_iface_limit
============================

*man struct ieee80211_iface_limit(9)*

*4.6.0-rc1*

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
