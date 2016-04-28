.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-ts-filter-type:

===================
enum ts_filter_type
===================

*man enum ts_filter_type(9)*

*4.6.0-rc5*

filter type bitmap for dmx_ts_feed. ``set``


Synopsis
========

.. code-block:: c

    enum ts_filter_type {
      TS_PACKET,
      TS_PAYLOAD_ONLY,
      TS_DECODER,
      TS_DEMUX
    };


Constants
=========

TS_PACKET
    Send TS packets (188 bytes) to callback (default).

TS_PAYLOAD_ONLY
    In case TS_PACKET is set, only send the TS payload (<=184 bytes per
    packet) to callback

TS_DECODER
    Send stream to built-in decoder (if present).

TS_DEMUX
    In case TS_PACKET is set, send the TS to the demux device, not to
    the dvr device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
