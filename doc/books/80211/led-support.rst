.. -*- coding: utf-8; mode: rst -*-

.. _led-support:

===========
LED support
===========

Mac80211 supports various ways of blinking LEDs. Wherever possible,
device LEDs should be exposed as LED class devices and hooked up to the
appropriate trigger, which will then be triggered appropriately by
mac80211.


.. toctree::
    :maxdepth: 1

    API-ieee80211-get-tx-led-name
    API-ieee80211-get-rx-led-name
    API-ieee80211-get-assoc-led-name
    API-ieee80211-get-radio-led-name
    API-struct-ieee80211-tpt-blink
    API-enum-ieee80211-tpt-led-trigger-flags
    API-ieee80211-create-tpt-led-trigger




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
