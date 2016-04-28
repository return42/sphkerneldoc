.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-monitor-flags:

==================
enum monitor_flags
==================

*man enum monitor_flags(9)*

*4.6.0-rc5*

monitor flags


Synopsis
========

.. code-block:: c

    enum monitor_flags {
      MONITOR_FLAG_FCSFAIL,
      MONITOR_FLAG_PLCPFAIL,
      MONITOR_FLAG_CONTROL,
      MONITOR_FLAG_OTHER_BSS,
      MONITOR_FLAG_COOK_FRAMES,
      MONITOR_FLAG_ACTIVE
    };


Constants
=========

MONITOR_FLAG_FCSFAIL
    pass frames with bad FCS

MONITOR_FLAG_PLCPFAIL
    pass frames with bad PLCP

MONITOR_FLAG_CONTROL
    pass control frames

MONITOR_FLAG_OTHER_BSS
    disable BSSID filtering

MONITOR_FLAG_COOK_FRAMES
    report frames after processing

MONITOR_FLAG_ACTIVE
    active monitor, ACKs frames on its MAC address


Description
===========

Monitor interface configuration flags. Note that these must be the bits
according to the nl80211 flags.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
