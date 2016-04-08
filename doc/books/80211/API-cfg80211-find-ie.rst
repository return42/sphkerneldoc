
.. _API-cfg80211-find-ie:

================
cfg80211_find_ie
================

*man cfg80211_find_ie(9)*

*4.6.0-rc1*

find information element in data


Synopsis
========

.. c:function:: const u8 ⋆ cfg80211_find_ie( u8 eid, const u8 * ies, int len )

Arguments
=========

``eid``
    element ID

``ies``
    data consisting of IEs

``len``
    length of data


Return
======

``NULL`` if the element ID could not be found or if the element is invalid (claims to be longer than the given data), or a pointer to the first byte of the requested element, that
is the byte containing the element ID.


Note
====

There are no checks on the element length other than having to fit into the given data.
