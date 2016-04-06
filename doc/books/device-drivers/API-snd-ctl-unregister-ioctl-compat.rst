
.. _API-snd-ctl-unregister-ioctl-compat:

===============================
snd_ctl_unregister_ioctl_compat
===============================

*man snd_ctl_unregister_ioctl_compat(9)*

*4.6.0-rc1*

de-register the device-specific compat 32bit control-ioctls


Synopsis
========

.. c:function:: int snd_ctl_unregister_ioctl_compat( snd_kctl_ioctl_func_t fcn )

Arguments
=========

``fcn``
    ioctl callback function to unregister
