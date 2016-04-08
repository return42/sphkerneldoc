
.. _API-enum-wiphy-params-flags:

=======================
enum wiphy_params_flags
=======================

*man enum wiphy_params_flags(9)*

*4.6.0-rc1*

set_wiphy_params bitfield values


Synopsis
========

.. code-block:: c

    enum wiphy_params_flags {
      WIPHY_PARAM_RETRY_SHORT,
      WIPHY_PARAM_RETRY_LONG,
      WIPHY_PARAM_FRAG_THRESHOLD,
      WIPHY_PARAM_RTS_THRESHOLD,
      WIPHY_PARAM_COVERAGE_CLASS,
      WIPHY_PARAM_DYN_ACK
    };


Constants
=========

WIPHY_PARAM_RETRY_SHORT
    wiphy->retry_short has changed

WIPHY_PARAM_RETRY_LONG
    wiphy->retry_long has changed

WIPHY_PARAM_FRAG_THRESHOLD
    wiphy->frag_threshold has changed

WIPHY_PARAM_RTS_THRESHOLD
    wiphy->rts_threshold has changed

WIPHY_PARAM_COVERAGE_CLASS
    coverage class changed

WIPHY_PARAM_DYN_ACK
    dynack has been enabled
