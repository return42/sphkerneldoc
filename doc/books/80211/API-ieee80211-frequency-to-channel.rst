.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-frequency-to-channel:

==============================
ieee80211_frequency_to_channel
==============================

*man ieee80211_frequency_to_channel(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
