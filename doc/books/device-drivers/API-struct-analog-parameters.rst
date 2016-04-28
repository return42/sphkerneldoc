.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-analog-parameters:

========================
struct analog_parameters
========================

*man struct analog_parameters(9)*

*4.6.0-rc5*

Parameters to tune into an analog/radio channel


Synopsis
========

.. code-block:: c

    struct analog_parameters {
      unsigned int frequency;
      unsigned int mode;
      unsigned int audmode;
      u64 std;
    };


Members
=======

frequency
    Frequency used by analog TV tuner (either in 62.5 kHz step, for TV,
    or 62.5 Hz for radio)

mode
    Tuner mode, as defined on enum v4l2_tuner_type

audmode
    Audio mode as defined for the rxsubchans field at videodev2.h, e. g.
    V4L2_TUNER_MODE_*

std
    TV standard bitmap as defined at videodev2.h, e. g. V4L2_STD_*


Description
===========

Hybrid tuners should be supported by both V4L2 and DVB APIs. This struct
contains the data that are used by the V4L2 side. To avoid dependencies
from V4L2 headers, all enums here are declared as integers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
