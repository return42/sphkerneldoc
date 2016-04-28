.. -*- coding: utf-8; mode: rst -*-

.. _API-regulatory-hint:

===============
regulatory_hint
===============

*man regulatory_hint(9)*

*4.6.0-rc5*

driver hint to the wireless core a regulatory domain


Synopsis
========

.. c:function:: int regulatory_hint( struct wiphy * wiphy, const char * alpha2 )

Arguments
=========

``wiphy``
    the wireless device giving the hint (used only for reporting
    conflicts)

``alpha2``
    the ISO/IEC 3166 alpha2 the driver claims its regulatory domain
    should be in. If ``rd`` is set this should be NULL. Note that if you
    set this to NULL you should still set rd->alpha2 to some accepted
    alpha2.


Description
===========

Wireless drivers can use this function to hint to the wireless core what
it believes should be the current regulatory domain by giving it an
ISO/IEC 3166 alpha2 country code it knows its regulatory domain should
be in or by providing a completely build regulatory domain. If the
driver provides an ISO/IEC 3166 alpha2 userspace will be queried for a
regulatory domain structure for the respective country.

The wiphy must have been registered to cfg80211 prior to this call. For
cfg80211 drivers this means you must first use ``wiphy_register``, for
mac80211 drivers you must first use ``ieee80211_register_hw``.

Drivers should check the return value, its possible you can get an
-ENOMEM.


Return
======

0 on success. -ENOMEM.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
