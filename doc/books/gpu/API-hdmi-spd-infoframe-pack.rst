
.. _API-hdmi-spd-infoframe-pack:

=======================
hdmi_spd_infoframe_pack
=======================

*man hdmi_spd_infoframe_pack(9)*

*4.6.0-rc1*

write HDMI SPD infoframe to binary buffer


Synopsis
========

.. c:function:: ssize_t hdmi_spd_infoframe_pack( struct hdmi_spd_infoframe * frame, void * buffer, size_t size )

Arguments
=========

``frame``
    HDMI SPD infoframe

``buffer``
    destination buffer

``size``
    size of buffer


Description
===========

Packs the information contained in the ``frame`` structure into a binary representation that can be written into the corresponding controller registers. Also computes the checksum
as required by section 5.3.5 of the HDMI 1.4 specification.

Returns the number of bytes packed into the binary buffer or a negative error code on failure.
