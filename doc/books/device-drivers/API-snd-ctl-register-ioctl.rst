
.. _API-snd-ctl-register-ioctl:

======================
snd_ctl_register_ioctl
======================

*man snd_ctl_register_ioctl(9)*

*4.6.0-rc1*

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
