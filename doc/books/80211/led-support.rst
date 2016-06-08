.. -*- coding: utf-8; mode: rst -*-

.. _led-support:

***********
LED support
***********

Mac80211 supports various ways of blinking LEDs. Wherever possible,
device LEDs should be exposed as LED class devices and hooked up to the
appropriate trigger, which will then be triggered appropriately by
mac80211.


.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_get_tx_led_name

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_get_rx_led_name

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_get_assoc_led_name

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_get_radio_led_name

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_tpt_blink

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_tpt_led_trigger_flags

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_create_tpt_led_trigger



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
