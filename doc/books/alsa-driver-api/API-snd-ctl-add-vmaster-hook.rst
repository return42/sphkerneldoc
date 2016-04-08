
.. _API-snd-ctl-add-vmaster-hook:

========================
snd_ctl_add_vmaster_hook
========================

*man snd_ctl_add_vmaster_hook(9)*

*4.6.0-rc1*

Add a hook to a vmaster control


Synopsis
========

.. c:function:: int snd_ctl_add_vmaster_hook( struct snd_kcontrol * kcontrol, void (*hook) void *private_data, int, void * private_data )

Arguments
=========

``kcontrol``
    vmaster kctl element

``hook``
    the hook function

``private_data``
    the private_data pointer to be saved


Description
===========

Adds the given hook to the vmaster control element so that it's called at each time when the value is changed.


Return
======

Zero.
