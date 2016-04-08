
.. _API-ieee80211-request-smps:

======================
ieee80211_request_smps
======================

*man ieee80211_request_smps(9)*

*4.6.0-rc1*

request SM PS transition


Synopsis
========

.. c:function:: void ieee80211_request_smps( struct ieee80211_vif * vif, enum ieee80211_smps_mode smps_mode )

Arguments
=========

``vif``
    ``struct ieee80211_vif`` pointer from the add_interface callback.

``smps_mode``
    new SM PS mode


Description
===========

This allows the driver to request an SM PS transition in managed mode. This is useful when the driver has more information than the stack about possible interference, for example
by bluetooth.
