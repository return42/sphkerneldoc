
.. _API-snd-ctl-register-ioctl-compat:

=============================
snd_ctl_register_ioctl_compat
=============================

*man snd_ctl_register_ioctl_compat(9)*

*4.6.0-rc1*

register the device-specific 32bit compat control-ioctls


Synopsis
========

.. c:function:: int snd_ctl_register_ioctl_compat( snd_kctl_ioctl_func_t fcn )

Arguments
=========

``fcn``
    ioctl callback function
