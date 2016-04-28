.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-tuner-range:

==================
struct tuner_range
==================

*man struct tuner_range(9)*

*4.6.0-rc5*

define the frequencies supported by the tuner


Synopsis
========

.. code-block:: c

    struct tuner_range {
      unsigned short limit;
      unsigned char config;
      unsigned char cb;
    };


Members
=======

limit
    Max frequency supported by that range, in 62.5 kHz (TV) or 62.5 Hz
    (Radio), as defined by V4L2_TUNER_CAP_LOW.

config
    Value of the band switch byte (BB) to setup this mode.

cb
    Value of the CB byte to setup this mode.


Description
===========

Please notice that digital tuners like xc3028/xc4000/xc5000 don't use
those ranges, as they're defined inside the driver. This is used by
analog tuners that are compatible with the “Philips way” to setup the
tuners. On those devices, the tuner set is done via 4 bytes: divider
byte1 (DB1), divider byte 2 (DB2), Control byte (CB) and band switch
byte (BB). Some tuners also have an additional optional Auxiliary byte
(AB).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
