
.. _API-snd-pcm-format-width:

====================
snd_pcm_format_width
====================

*man snd_pcm_format_width(9)*

*4.6.0-rc1*

return the bit-width of the format


Synopsis
========

.. c:function:: int snd_pcm_format_width( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

The bit-width of the format, or a negative error code if unknown format.
