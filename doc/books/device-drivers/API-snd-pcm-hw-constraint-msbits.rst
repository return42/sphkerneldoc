.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-hw-constraint-msbits:

============================
snd_pcm_hw_constraint_msbits
============================

*man snd_pcm_hw_constraint_msbits(9)*

*4.6.0-rc5*

add a hw constraint msbits rule


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_msbits( struct snd_pcm_runtime * runtime, unsigned int cond, unsigned int width, unsigned int msbits )

Arguments
=========

``runtime``
    PCM runtime instance

``cond``
    condition bits

``width``
    sample bits width

``msbits``
    msbits width


Description
===========

This constraint will set the number of most significant bits (msbits) if
a sample format with the specified width has been select. If width is
set to 0 the msbits will be set for any sample format with a width
larger than the specified msbits.


Return
======

Zero if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
