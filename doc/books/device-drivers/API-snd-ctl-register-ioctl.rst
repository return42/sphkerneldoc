.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-register-ioctl:

======================
snd_ctl_register_ioctl
======================

*man snd_ctl_register_ioctl(9)*

*4.6.0-rc5*

register the device-specific control-ioctls


Synopsis
========

.. c:function:: int snd_ctl_register_ioctl( snd_kctl_ioctl_func_t fcn )

Arguments
=========

``fcn``
    ioctl callback function


Description
===========

called from each device manager like pcm.c, hwdep.c, etc.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
