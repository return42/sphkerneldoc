
.. _API-ieee80211-frequency-to-channel:

==============================
ieee80211_frequency_to_channel
==============================

*man ieee80211_frequency_to_channel(9)*

*4.6.0-rc1*

convert frequency to channel number


Synopsis
========

.. c:function:: int ieee80211_frequency_to_channel( int freq )

Arguments
=========

``freq``
    center frequency


Return
======

The corresponding channel, or 0 if the conversion failed.
