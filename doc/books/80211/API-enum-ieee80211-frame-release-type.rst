.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-ieee80211-frame-release-type:

=================================
enum ieee80211_frame_release_type
=================================

*man enum ieee80211_frame_release_type(9)*

*4.6.0-rc5*

frame release reason


Synopsis
========

.. code-block:: c

    enum ieee80211_frame_release_type {
      IEEE80211_FRAME_RELEASE_PSPOLL,
      IEEE80211_FRAME_RELEASE_UAPSD
    };


Constants
=========

IEEE80211_FRAME_RELEASE_PSPOLL
    frame released for PS-Poll

IEEE80211_FRAME_RELEASE_UAPSD
    frame(s) released due to frame received on trigger-enabled AC


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
