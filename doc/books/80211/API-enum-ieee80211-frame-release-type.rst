
.. _API-enum-ieee80211-frame-release-type:

=================================
enum ieee80211_frame_release_type
=================================

*man enum ieee80211_frame_release_type(9)*

*4.6.0-rc1*

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
