
.. _API-snd-soc-dapm-del-routes:

=======================
snd_soc_dapm_del_routes
=======================

*man snd_soc_dapm_del_routes(9)*

*4.6.0-rc1*

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
