.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-format-physical-width:

=============================
snd_pcm_format_physical_width
=============================

*man snd_pcm_format_physical_width(9)*

*4.6.0-rc5*

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

The physical bit-width of the format, or a negative error code if
unknown format.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
