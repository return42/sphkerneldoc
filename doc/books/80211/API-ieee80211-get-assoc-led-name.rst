
.. _API-ieee80211-get-assoc-led-name:

============================
ieee80211_get_assoc_led_name
============================

*man ieee80211_get_assoc_led_name(9)*

*4.6.0-rc1*

get name of association LED


Synopsis
========

.. c:function:: const char ⋆ ieee80211_get_assoc_led_name( struct ieee80211_hw * hw )

Arguments
=========

``hw``
    the hardware to get the LED trigger name for


Description
===========

mac80211 creates a association LED trigger for each wireless hardware that can be used to drive LEDs if your driver registers a LED device. This function returns the name (or
``NULL`` if not configured for LEDs) of the trigger so you can automatically link the LED device.


Return
======

The name of the LED trigger. ``NULL`` if not configured for LEDs.
