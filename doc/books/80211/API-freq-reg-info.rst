
.. _API-freq-reg-info:

=============
freq_reg_info
=============

*man freq_reg_info(9)*

*4.6.0-rc1*

get regulatory information for the given frequency


Synopsis
========

.. c:function:: const struct ieee80211_reg_rule ⋆ freq_reg_info( struct wiphy * wiphy, u32 center_freq )

Arguments
=========

``wiphy``
    the wiphy for which we want to process this rule for

``center_freq``
    Frequency in KHz for which we want regulatory information for


Description
===========

Use this function to get the regulatory rule for a specific frequency on a given wireless device. If the device has a specific regulatory domain it wants to follow we respect that
unless a country IE has been received and processed already.


Return
======

A valid pointer, or, when an error occurs, for example if no rule can be found, the return value is encoded using ``ERR_PTR``. Use ``IS_ERR`` to check and ``PTR_ERR`` to obtain the
numeric return value. The numeric return value will be -ERANGE if we determine the given center_freq does not even have a regulatory rule for a frequency range in the
center_freq's band. See ``freq_in_rule_band`` for our current definition of a band -- this is purely subjective and right now it's 802.11 specific.
