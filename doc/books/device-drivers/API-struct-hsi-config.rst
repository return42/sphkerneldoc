.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-hsi-config:

=================
struct hsi_config
=================

*man struct hsi_config(9)*

*4.6.0-rc5*

Configuration for RX/TX HSI modules


Synopsis
========

.. code-block:: c

    struct hsi_config {
      unsigned int mode;
      struct hsi_channel * channels;
      unsigned int num_channels;
      unsigned int num_hw_channels;
      unsigned int speed;
      union {unnamed_union};
    };


Members
=======

mode
    Bit transmission mode (STREAM or FRAME)

channels
    Channel resources used by the client

num_channels
    Number of channel resources

num_hw_channels
    Number of channels the transceiver is configured for [1..16]

speed
    Max bit transmission speed (Kbit/s)

{unnamed_union}
    anonymous


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
