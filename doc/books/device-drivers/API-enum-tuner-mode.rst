
.. _API-enum-tuner-mode:

===============
enum tuner_mode
===============

*man enum tuner_mode(9)*

*4.6.0-rc1*

Mode of the tuner


Synopsis
========

.. code-block:: c

    enum tuner_mode {
      T_RADIO,
      T_ANALOG_TV
    };


Constants
=========

T_RADIO
    Tuner core will work in radio mode

T_ANALOG_TV
    Tuner core will work in analog TV mode


Description
===========

Older boards only had a single tuner device, but some devices have a separate tuner for radio. In any case, the tuner-core needs to know if the tuner chip(s) will be used in radio
mode or analog TV mode, as, on radio mode, frequencies are specified on a different range than on TV mode. This enum is used by the tuner core in order to work with the proper
tuner range and eventually use a different tuner chip while in radio mode.
