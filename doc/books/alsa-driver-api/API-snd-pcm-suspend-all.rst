.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-suspend-all:

===================
snd_pcm_suspend_all
===================

*man snd_pcm_suspend_all(9)*

*4.6.0-rc5*

trigger SUSPEND to all substreams in the given pcm


Synopsis
========

.. c:function:: int snd_pcm_suspend_all( struct snd_pcm * pcm )

Arguments
=========

``pcm``
    the PCM instance


Description
===========

After this call, all streams are changed to SUSPENDED state.


Return
======

Zero if successful (or ``pcm`` is ``NULL``), or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
