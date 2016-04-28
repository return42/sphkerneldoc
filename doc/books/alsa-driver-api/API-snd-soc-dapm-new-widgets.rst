.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-new-widgets:

========================
snd_soc_dapm_new_widgets
========================

*man snd_soc_dapm_new_widgets(9)*

*4.6.0-rc5*

add new dapm widgets


Synopsis
========

.. c:function:: int snd_soc_dapm_new_widgets( struct snd_soc_card * card )

Arguments
=========

``card``
    card to be checked for new dapm widgets


Description
===========

Checks the codec for any new dapm widgets and creates them if found.

Returns 0 for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
