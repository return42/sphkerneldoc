
.. _API-snd-ctl-replace:

===============
snd_ctl_replace
===============

*man snd_ctl_replace(9)*

*4.6.0-rc1*

replace the control instance of the card


Synopsis
========

.. c:function:: int snd_ctl_replace( struct snd_card * card, struct snd_kcontrol * kcontrol, bool add_on_replace )

Arguments
=========

``card``
    the card instance

``kcontrol``
    the control instance to replace

``add_on_replace``
    add the control if not already added


Description
===========

Replaces the given control. If the given control does not exist and the add_on_replace flag is set, the control is added. If the control exists, it is destroyed first.

It frees automatically the control which cannot be added or replaced.


Return
======

Zero if successful, or a negative error code on failure.
