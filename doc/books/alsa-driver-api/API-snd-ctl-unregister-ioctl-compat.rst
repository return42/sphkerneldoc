.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-unregister-ioctl-compat:

===============================
snd_ctl_unregister_ioctl_compat
===============================

*man snd_ctl_unregister_ioctl_compat(9)*

*4.6.0-rc5*

de-register the device-specific compat 32bit control-ioctls


Synopsis
========

.. c:function:: int snd_ctl_unregister_ioctl_compat( snd_kctl_ioctl_func_t fcn )

Arguments
=========

``fcn``
    ioctl callback function to unregister


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
