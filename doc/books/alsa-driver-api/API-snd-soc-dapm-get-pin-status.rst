.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-get-pin-status:

===========================
snd_soc_dapm_get_pin_status
===========================

*man snd_soc_dapm_get_pin_status(9)*

*4.6.0-rc5*

get audio pin status


Synopsis
========

.. c:function:: int snd_soc_dapm_get_pin_status( struct snd_soc_dapm_context * dapm, const char * pin )

Arguments
=========

``dapm``
    DAPM context

``pin``
    audio signal pin endpoint (or start point)


Description
===========

Get audio pin status - connected or disconnected.

Returns 1 for connected otherwise 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
