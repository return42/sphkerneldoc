.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-ieee80211-tpt-led-trigger-flags:

====================================
enum ieee80211_tpt_led_trigger_flags
====================================

*man enum ieee80211_tpt_led_trigger_flags(9)*

*4.6.0-rc5*

throughput trigger flags


Synopsis
========

.. code-block:: c

    enum ieee80211_tpt_led_trigger_flags {
      IEEE80211_TPT_LEDTRIG_FL_RADIO,
      IEEE80211_TPT_LEDTRIG_FL_WORK,
      IEEE80211_TPT_LEDTRIG_FL_CONNECTED
    };


Constants
=========

IEEE80211_TPT_LEDTRIG_FL_RADIO
    enable blinking with radio

IEEE80211_TPT_LEDTRIG_FL_WORK
    enable blinking when working

IEEE80211_TPT_LEDTRIG_FL_CONNECTED
    enable blinking when at least one interface is connected in some
    way, including being an AP


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
