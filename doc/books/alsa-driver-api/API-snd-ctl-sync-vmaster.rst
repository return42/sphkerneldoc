.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-sync-vmaster:

====================
snd_ctl_sync_vmaster
====================

*man snd_ctl_sync_vmaster(9)*

*4.6.0-rc5*

Sync the vmaster slaves and hook


Synopsis
========

.. c:function:: void snd_ctl_sync_vmaster( struct snd_kcontrol * kcontrol, bool hook_only )

Arguments
=========

``kcontrol``
    vmaster kctl element

``hook_only``
    sync only the hook


Description
===========

Forcibly call the put callback of each slave and call the hook function
to synchronize with the current value of the given vmaster element. NOP
when NULL is passed to ``kcontrol``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
