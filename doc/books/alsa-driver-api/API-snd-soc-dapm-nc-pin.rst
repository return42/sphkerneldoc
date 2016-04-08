
.. _API-snd-soc-dapm-nc-pin:

===================
snd_soc_dapm_nc_pin
===================

*man snd_soc_dapm_nc_pin(9)*

*4.6.0-rc1*

permanently disable pin.


Synopsis
========

.. c:function:: int snd_soc_dapm_nc_pin( struct snd_soc_dapm_context * dapm, const char * pin )

Arguments
=========

``dapm``
    DAPM context

``pin``
    pin name


Description
===========

Marks the specified pin as being not connected, disabling it along any parent or child widgets. At present this is identical to ``snd_soc_dapm_disable_pin`` but in future it will
be extended to do additional things such as disabling controls which only affect paths through the pin.


NOTE
====

``snd_soc_dapm_sync`` needs to be called after this for DAPM to do any widget power switching.
