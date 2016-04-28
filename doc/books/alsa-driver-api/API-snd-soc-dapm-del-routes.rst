.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-del-routes:

=======================
snd_soc_dapm_del_routes
=======================

*man snd_soc_dapm_del_routes(9)*

*4.6.0-rc5*

Remove routes between DAPM widgets


Synopsis
========

.. c:function:: int snd_soc_dapm_del_routes( struct snd_soc_dapm_context * dapm, const struct snd_soc_dapm_route * route, int num )

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

Removes routes from the DAPM context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
