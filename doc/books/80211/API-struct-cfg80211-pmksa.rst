.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-cfg80211-pmksa:

=====================
struct cfg80211_pmksa
=====================

*man struct cfg80211_pmksa(9)*

*4.6.0-rc5*

PMK Security Association


Synopsis
========

.. code-block:: c

    struct cfg80211_pmksa {
      const u8 * bssid;
      const u8 * pmkid;
    };


Members
=======

bssid
    The AP's BSSID.

pmkid
    The PMK material itself.


Description
===========

This structure is passed to the set/\ ``del_pmksa`` method for PMKSA
caching.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
