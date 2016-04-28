.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-dvb-tuner-info:

=====================
struct dvb_tuner_info
=====================

*man struct dvb_tuner_info(9)*

*4.6.0-rc5*

Frontend name and min/max ranges/bandwidths


Synopsis
========

.. code-block:: c

    struct dvb_tuner_info {
      char name[128];
      u32 frequency_min;
      u32 frequency_max;
      u32 frequency_step;
      u32 bandwidth_min;
      u32 bandwidth_max;
      u32 bandwidth_step;
    };


Members
=======

name[128]
    name of the Frontend

frequency_min
    minimal frequency supported

frequency_max
    maximum frequency supported

frequency_step
    frequency step

bandwidth_min
    minimal frontend bandwidth supported

bandwidth_max
    maximum frontend bandwidth supported

bandwidth_step
    frontend bandwidth step


NOTE
====

frequency parameters are in Hz, for terrestrial/cable or kHz for
satellite.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
