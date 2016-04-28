.. -*- coding: utf-8; mode: rst -*-

.. _API-hdmi-audio-infoframe-pack:

=========================
hdmi_audio_infoframe_pack
=========================

*man hdmi_audio_infoframe_pack(9)*

*4.6.0-rc5*

write HDMI audio infoframe to binary buffer


Synopsis
========

.. c:function:: ssize_t hdmi_audio_infoframe_pack( struct hdmi_audio_infoframe * frame, void * buffer, size_t size )

Arguments
=========

``frame``
    HDMI audio infoframe

``buffer``
    destination buffer

``size``
    size of buffer


Description
===========

Packs the information contained in the ``frame`` structure into a binary
representation that can be written into the corresponding controller
registers. Also computes the checksum as required by section 5.3.5 of
the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative
error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
