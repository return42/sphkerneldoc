
.. _API-enum-survey-info-flags:

======================
enum survey_info_flags
======================

*man enum survey_info_flags(9)*

*4.6.0-rc1*

survey information flags


Synopsis
========

.. code-block:: c

    enum survey_info_flags {
      SURVEY_INFO_NOISE_DBM,
      SURVEY_INFO_IN_USE,
      SURVEY_INFO_TIME,
      SURVEY_INFO_TIME_BUSY,
      SURVEY_INFO_TIME_EXT_BUSY,
      SURVEY_INFO_TIME_RX,
      SURVEY_INFO_TIME_TX,
      SURVEY_INFO_TIME_SCAN
    };


Constants
=========

SURVEY_INFO_NOISE_DBM
    noise (in dBm) was filled in

SURVEY_INFO_IN_USE
    channel is currently being used

SURVEY_INFO_TIME
    active time (in ms) was filled in

SURVEY_INFO_TIME_BUSY
    busy time was filled in

SURVEY_INFO_TIME_EXT_BUSY
    extension channel busy time was filled in

SURVEY_INFO_TIME_RX
    receive time was filled in

SURVEY_INFO_TIME_TX
    transmit time was filled in

SURVEY_INFO_TIME_SCAN
    scan time was filled in


Description
===========

Used by the driver to indicate which info in ``struct survey_info`` it has filled in during the ``get_survey``.
