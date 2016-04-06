
.. _API-snd-ctl-unregister-ioctl:

========================
snd_ctl_unregister_ioctl
========================

*man snd_ctl_unregister_ioctl(9)*

*4.6.0-rc1*

de-register the device-specific control-ioctls


Synopsis
========

.. c:function:: int snd_ctl_unregister_ioctl( snd_kctl_ioctl_func_t fcn )

Arguments
=========

``fcn``
    ioctl callback function to unregister
