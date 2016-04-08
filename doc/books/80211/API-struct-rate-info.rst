
.. _API-struct-rate-info:

================
struct rate_info
================

*man struct rate_info(9)*

*4.6.0-rc1*

bitrate information


Synopsis
========

.. code-block:: c

    struct rate_info {
      u8 flags;
      u8 mcs;
      u16 legacy;
      u8 nss;
      u8 bw;
    };


Members
=======

flags
    bitflag of flags from ``enum`` rate_info_flags

mcs
    mcs index if struct describes a 802.11n bitrate

legacy
    bitrate in 100kbit/s for 802.11abg

nss
    number of streams (VHT only)

bw
    bandwidth (from ``enum`` rate_info_bw)


Description
===========

Information about a receiving or transmitting bitrate
