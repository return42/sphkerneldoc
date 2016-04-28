.. -*- coding: utf-8; mode: rst -*-

.. _smps:

=====================================
Spatial Multiplexing Powersave (SMPS)
=====================================

SMPS (Spatial multiplexing power save) is a mechanism to conserve power
in an 802.11n implementation. For details on the mechanism and
rationale, please refer to 802.11 (as amended by 802.11n-2009) “11.2.3
SM power save”.

The mac80211 implementation is capable of sending action frames to
update the AP about the station's SMPS mode, and will instruct the
driver to enter the specific mode. It will also announce the requested
SMPS mode during the association handshake. Hardware support for this
feature is required, and can be indicated by hardware flags.

The default mode will be “automatic”, which nl80211/cfg80211 defines to
be dynamic SMPS in (regular) powersave, and SMPS turned off otherwise.

To support this feature, the driver must set the appropriate hardware
support flags, and handle the SMPS flag to the ``config`` operation. It
will then with this mechanism be instructed to enter the requested SMPS
mode while associated to an HT AP.


.. toctree::
    :maxdepth: 1

    API-ieee80211-request-smps
    API-enum-ieee80211-smps-mode




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
