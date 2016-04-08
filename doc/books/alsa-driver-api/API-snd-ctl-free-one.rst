
.. _API-snd-ctl-free-one:

================
snd_ctl_free_one
================

*man snd_ctl_free_one(9)*

*4.6.0-rc1*

release the control instance


Synopsis
========

.. c:function:: void snd_ctl_free_one( struct snd_kcontrol * kcontrol )

Arguments
=========

``kcontrol``
    the control instance


Description
===========

Releases the control instance created via ``snd_ctl_new`` or ``snd_ctl_new1``. Don't call this after the control was added to the card.
