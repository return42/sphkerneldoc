
.. _API-snd-pcm-format-physical-width:

=============================
snd_pcm_format_physical_width
=============================

*man snd_pcm_format_physical_width(9)*

*4.6.0-rc1*

return the physical bit-width of the format


Synopsis
========

.. c:function:: int snd_pcm_format_physical_width( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

The physical bit-width of the format, or a negative error code if unknown format.
