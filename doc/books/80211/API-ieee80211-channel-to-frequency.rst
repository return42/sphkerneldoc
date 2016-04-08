
.. _API-ieee80211-channel-to-frequency:

==============================
ieee80211_channel_to_frequency
==============================

*man ieee80211_channel_to_frequency(9)*

*4.6.0-rc1*

convert channel number to frequency


Synopsis
========

.. c:function:: int ieee80211_channel_to_frequency( int chan, enum ieee80211_band band )

Arguments
=========

``chan``
    channel number

``band``
    band, necessary due to channel number overlap


Return
======

The corresponding frequency (in MHz), or 0 if the conversion failed.
