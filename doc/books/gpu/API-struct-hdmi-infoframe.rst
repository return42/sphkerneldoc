
.. _API-struct-hdmi-infoframe:

====================
union hdmi_infoframe
====================

*man union hdmi_infoframe(9)*

*4.6.0-rc1*

overall union of all abstract infoframe representations


Synopsis
========

.. code-block:: c

    union hdmi_infoframe {
      struct hdmi_any_infoframe any;
      struct hdmi_avi_infoframe avi;
      struct hdmi_spd_infoframe spd;
      union hdmi_vendor_any_infoframe vendor;
      struct hdmi_audio_infoframe audio;
    };


Members
=======

any
    generic infoframe

avi
    avi infoframe

spd
    spd infoframe

vendor
    union of all vendor infoframes

audio
    audio infoframe


Description
===========

This is used by the generic pack function. This works since all infoframes have the same header which also indicates which type of infoframe should be packed.
