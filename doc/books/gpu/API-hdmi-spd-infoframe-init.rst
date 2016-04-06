
.. _API-hdmi-spd-infoframe-init:

=======================
hdmi_spd_infoframe_init
=======================

*man hdmi_spd_infoframe_init(9)*

*4.6.0-rc1*

initialize an HDMI SPD infoframe


Synopsis
========

.. c:function:: int hdmi_spd_infoframe_init( struct hdmi_spd_infoframe * frame, const char * vendor, const char * product )

Arguments
=========

``frame``
    HDMI SPD infoframe

``vendor``
    vendor string

``product``
    product string


Description
===========

Returns 0 on success or a negative error code on failure.
