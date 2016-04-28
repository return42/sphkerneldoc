.. -*- coding: utf-8; mode: rst -*-

.. _API-hdmi-infoframe-unpack:

=====================
hdmi_infoframe_unpack
=====================

*man hdmi_infoframe_unpack(9)*

*4.6.0-rc5*

unpack binary buffer to a HDMI infoframe


Synopsis
========

.. c:function:: int hdmi_infoframe_unpack( union hdmi_infoframe * frame, void * buffer )

Arguments
=========

``frame``
    HDMI infoframe

``buffer``
    source buffer


Description
===========

Unpacks the information contained in binary buffer ``buffer`` into a
structured ``frame`` of a HDMI infoframe. Also verifies the checksum as
required by section 5.3.5 of the HDMI 1.4 specification.

Returns 0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
