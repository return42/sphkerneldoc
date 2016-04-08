
.. _API-struct-cfg80211-pmksa:

=====================
struct cfg80211_pmksa
=====================

*man struct cfg80211_pmksa(9)*

*4.6.0-rc1*

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

This structure is passed to the set/\ ``del_pmksa`` method for PMKSA caching.
