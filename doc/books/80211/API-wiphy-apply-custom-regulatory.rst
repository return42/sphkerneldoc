.. -*- coding: utf-8; mode: rst -*-

.. _API-wiphy-apply-custom-regulatory:

=============================
wiphy_apply_custom_regulatory
=============================

*man wiphy_apply_custom_regulatory(9)*

*4.6.0-rc5*

apply a custom driver regulatory domain


Synopsis
========

.. c:function:: void wiphy_apply_custom_regulatory( struct wiphy * wiphy, const struct ieee80211_regdomain * regd )

Arguments
=========

``wiphy``
    the wireless device we want to process the regulatory domain on

``regd``
    the custom regulatory domain to use for this wiphy


Description
===========

Drivers can sometimes have custom regulatory domains which do not apply
to a specific country. Drivers can use this to apply such custom
regulatory domains. This routine must be called prior to wiphy
registration. The custom regulatory domain will be trusted completely
and as such previous default channel settings will be disregarded. If no
rule is found for a channel on the regulatory domain the channel will be
disabled. Drivers using this for a wiphy should also set the wiphy flag
REGULATORY_CUSTOM_REG or cfg80211 will set it for the wiphy that
called this helper.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
