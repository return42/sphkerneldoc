.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-ieee80211-band:

===================
enum ieee80211_band
===================

*man enum ieee80211_band(9)*

*4.6.0-rc5*

supported frequency bands


Synopsis
========

.. code-block:: c

    enum ieee80211_band {
      IEEE80211_BAND_2GHZ,
      IEEE80211_BAND_5GHZ,
      IEEE80211_BAND_60GHZ,
      IEEE80211_NUM_BANDS
    };


Constants
=========

IEEE80211_BAND_2GHZ
    2.4GHz ISM band

IEEE80211_BAND_5GHZ
    around 5GHz band (4.9-5.7)

IEEE80211_BAND_60GHZ
    around 60 GHz band (58.32 - 64.80 GHz)

IEEE80211_NUM_BANDS
    number of defined bands


Device registration
===================

The bands are assigned this way because the supported bitrates differ in
these bands.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
