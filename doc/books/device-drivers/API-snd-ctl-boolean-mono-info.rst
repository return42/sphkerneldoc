
.. _API-snd-ctl-boolean-mono-info:

=========================
snd_ctl_boolean_mono_info
=========================

*man snd_ctl_boolean_mono_info(9)*

*4.6.0-rc1*

Helper function for a standard boolean info callback with a mono channel


Synopsis
========

.. c:function:: int snd_ctl_boolean_mono_info( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_info * uinfo )

Arguments
=========

``kcontrol``
    the kcontrol instance

``uinfo``
    info to store


Description
===========

This is a function that can be used as info callback for a standard boolean control with a single mono channel.
