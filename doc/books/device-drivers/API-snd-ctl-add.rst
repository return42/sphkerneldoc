
.. _API-snd-ctl-add:

===========
snd_ctl_add
===========

*man snd_ctl_add(9)*

*4.6.0-rc1*

add the control instance to the card


Synopsis
========

.. c:function:: int snd_ctl_add( struct snd_card * card, struct snd_kcontrol * kcontrol )

Arguments
=========

``card``
    the card instance

``kcontrol``
    the control instance to add


Description
===========

Adds the control instance created via ``snd_ctl_new`` or ``snd_ctl_new1`` to the given card. Assigns also an unique numid used for fast search.

It frees automatically the control which cannot be added.


Return
======

Zero if successful, or a negative error code on failure.
