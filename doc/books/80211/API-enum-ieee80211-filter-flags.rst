
.. _API-enum-ieee80211-filter-flags:

===========================
enum ieee80211_filter_flags
===========================

*man enum ieee80211_filter_flags(9)*

*4.6.0-rc1*

hardware filter flags


Synopsis
========

.. code-block:: c

    enum ieee80211_filter_flags {
      FIF_ALLMULTI,
      FIF_FCSFAIL,
      FIF_PLCPFAIL,
      FIF_BCN_PRBRESP_PROMISC,
      FIF_CONTROL,
      FIF_OTHER_BSS,
      FIF_PSPOLL,
      FIF_PROBE_REQ
    };


Constants
=========

FIF_ALLMULTI
    pass all multicast frames, this is used if requested by the user or if the hardware is not capable of filtering by multicast address.

FIF_FCSFAIL
    pass frames with failed FCS (but you need to set the ``RX_FLAG_FAILED_FCS_CRC`` for them)

FIF_PLCPFAIL
    pass frames with failed PLCP CRC (but you need to set the ``RX_FLAG_FAILED_PLCP_CRC`` for them

FIF_BCN_PRBRESP_PROMISC
    This flag is set during scanning to indicate to the hardware that it should not filter beacons or probe responses by BSSID. Filtering them can greatly reduce the amount of
    processing mac80211 needs to do and the amount of CPU wakeups, so you should honour this flag if possible.

FIF_CONTROL
    pass control frames (except for PS Poll) addressed to this station

FIF_OTHER_BSS
    pass frames destined to other BSSes

FIF_PSPOLL
    pass PS Poll frames

FIF_PROBE_REQ
    pass probe request frames


HW queue control
================

These flags determine what the filter in hardware should be programmed to let through and what should not be passed to the stack. It is always safe to pass more frames than
requested, but this has negative impact on power consumption.
