.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-format-linear:

=====================
snd_pcm_format_linear
=====================

*man snd_pcm_format_linear(9)*

*4.6.0-rc5*

Check the PCM format is linear


Synopsis
========

.. c:function:: int snd_pcm_format_linear( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

1 if the given PCM format is linear, 0 if not.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
