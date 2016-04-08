
.. _API-ieee80211-create-tpt-led-trigger:

================================
ieee80211_create_tpt_led_trigger
================================

*man ieee80211_create_tpt_led_trigger(9)*

*4.6.0-rc1*

create throughput LED trigger


Synopsis
========

.. c:function:: const char ⋆ ieee80211_create_tpt_led_trigger( struct ieee80211_hw * hw, unsigned int flags, const struct ieee80211_tpt_blink * blink_table, unsigned int blink_table_len )

Arguments
=========

``hw``
    the hardware to create the trigger for

``flags``
    trigger flags, see ``enum`` ieee80211_tpt_led_trigger_flags

``blink_table``
    the blink table -- needs to be ordered by throughput

``blink_table_len``
    size of the blink table


Return
======

``NULL`` (in case of error, or if no LED triggers are configured) or the name of the new trigger.


Note
====

This function must be called before ``ieee80211_register_hw``.
