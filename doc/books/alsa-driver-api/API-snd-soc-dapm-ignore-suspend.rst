
.. _API-snd-soc-dapm-ignore-suspend:

===========================
snd_soc_dapm_ignore_suspend
===========================

*man snd_soc_dapm_ignore_suspend(9)*

*4.6.0-rc1*

ignore suspend status for DAPM endpoint


Synopsis
========

.. c:function:: int snd_soc_dapm_ignore_suspend( struct snd_soc_dapm_context * dapm, const char * pin )

Arguments
=========

``dapm``
    DAPM context

``pin``
    audio signal pin endpoint (or start point)


Description
===========

Mark the given endpoint or pin as ignoring suspend. When the system is disabled a path between two endpoints flagged as ignoring suspend will not be disabled. The path must already
be enabled via normal means at suspend time, it will not be turned on if it was not already enabled.
