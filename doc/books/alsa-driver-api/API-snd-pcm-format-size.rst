.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-format-size:

===================
snd_pcm_format_size
===================

*man snd_pcm_format_size(9)*

*4.6.0-rc5*

return the byte size of samples on the given format


Synopsis
========

.. c:function:: ssize_t snd_pcm_format_size( snd_pcm_format_t format, size_t samples )

Arguments
=========

``format``
    the format to check

``samples``
    sampling rate


Return
======

The byte size of the given samples for the format, or a negative error
code if unknown format.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
