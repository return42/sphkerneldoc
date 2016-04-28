.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-rate-info-flags:

====================
enum rate_info_flags
====================

*man enum rate_info_flags(9)*

*4.6.0-rc5*

bitrate info flags


Synopsis
========

.. code-block:: c

    enum rate_info_flags {
      RATE_INFO_FLAGS_MCS,
      RATE_INFO_FLAGS_VHT_MCS,
      RATE_INFO_FLAGS_SHORT_GI,
      RATE_INFO_FLAGS_60G
    };


Constants
=========

RATE_INFO_FLAGS_MCS
    mcs field filled with HT MCS

RATE_INFO_FLAGS_VHT_MCS
    mcs field filled with VHT MCS

RATE_INFO_FLAGS_SHORT_GI
    400ns guard interval

RATE_INFO_FLAGS_60G
    60GHz MCS


Description
===========

Used by the driver to indicate the specific rate transmission type for
802.11n transmissions.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
