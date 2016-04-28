.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-weak-routes:

========================
snd_soc_dapm_weak_routes
========================

*man snd_soc_dapm_weak_routes(9)*

*4.6.0-rc5*

Mark routes between DAPM widgets as weak


Synopsis
========

.. c:function:: int snd_soc_dapm_weak_routes( struct snd_soc_dapm_context * dapm, const struct snd_soc_dapm_route * route, int num )

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

Mark existing routes matching those specified in the passed array as
being weak, meaning that they are ignored for the purpose of power
decisions. The main intended use case is for sidetone paths which couple
audio between other independent paths if they are both active in order
to make the combination work better at the user level but which aren't
intended to be “used”.

Note that CODEC drivers should not use this as sidetone type paths can
frequently also be used as bypass paths.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
