.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-survey-info:

==================
struct survey_info
==================

*man struct survey_info(9)*

*4.6.0-rc5*

channel survey response


Synopsis
========

.. code-block:: c

    struct survey_info {
      struct ieee80211_channel * channel;
      u64 time;
      u64 time_busy;
      u64 time_ext_busy;
      u64 time_rx;
      u64 time_tx;
      u64 time_scan;
      u32 filled;
      s8 noise;
    };


Members
=======

channel
    the channel this survey record reports, may be ``NULL`` for a single
    record to report global statistics

time
    amount of time in ms the radio was turn on (on the channel)

time_busy
    amount of time the primary channel was sensed busy

time_ext_busy
    amount of time the extension channel was sensed busy

time_rx
    amount of time the radio spent receiving data

time_tx
    amount of time the radio spent transmitting data

time_scan
    amount of time the radio spent for scanning

filled
    bitflag of flags from ``enum`` survey_info_flags

noise
    channel noise in dBm. This and all following fields are optional


Description
===========

Used by ``dump_survey`` to report back per-channel survey information.

This structure can later be expanded with things like channel duty cycle
etc.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
