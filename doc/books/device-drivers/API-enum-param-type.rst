
.. _API-enum-param-type:

===============
enum param_type
===============

*man enum param_type(9)*

*4.6.0-rc1*

type of the tuner pameters


Synopsis
========

.. code-block:: c

    enum param_type {
      TUNER_PARAM_TYPE_RADIO,
      TUNER_PARAM_TYPE_PAL,
      TUNER_PARAM_TYPE_SECAM,
      TUNER_PARAM_TYPE_NTSC,
      TUNER_PARAM_TYPE_DIGITAL
    };


Constants
=========

TUNER_PARAM_TYPE_RADIO
    Tuner params are for FM and/or AM radio

TUNER_PARAM_TYPE_PAL
    Tuner params are for PAL color TV standard

TUNER_PARAM_TYPE_SECAM
    Tuner params are for SECAM color TV standard

TUNER_PARAM_TYPE_NTSC
    Tuner params are for NTSC color TV standard

TUNER_PARAM_TYPE_DIGITAL
    Tuner params are for digital TV
