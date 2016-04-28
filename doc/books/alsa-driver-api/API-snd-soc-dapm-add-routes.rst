.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-add-routes:

=======================
snd_soc_dapm_add_routes
=======================

*man snd_soc_dapm_add_routes(9)*

*4.6.0-rc5*

Add routes between DAPM widgets


Synopsis
========

.. c:function:: int snd_soc_dapm_add_routes( struct snd_soc_dapm_context * dapm, const struct snd_soc_dapm_route * route, int num )

Arguments
=========

``dapm``
    DAPM context

``route``
    audio routes

``num``
    number of routes


Description
===========

Connects 2 dapm widgets together via a named audio path. The sink is the
widget receiving the audio signal, whilst the source is the sender of
the audio signal.

Returns 0 for success else error. On error all resources can be freed
with a call to ``snd_soc_card_free``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
