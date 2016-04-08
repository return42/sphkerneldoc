
.. _API-snd-soc-dapm-new-widgets:

========================
snd_soc_dapm_new_widgets
========================

*man snd_soc_dapm_new_widgets(9)*

*4.6.0-rc1*

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
