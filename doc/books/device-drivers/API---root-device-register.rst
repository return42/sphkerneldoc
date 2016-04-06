
.. _API---root-device-register:

======================
__root_device_register
======================

*man __root_device_register(9)*

*4.6.0-rc1*

allocate and register a root device


Synopsis
========

.. c:function:: struct device ⋆ __root_device_register( const char * name, struct module * owner )

Arguments
=========

``name``
    root device name

``owner``
    owner module of the root device, usually THIS_MODULE


Description
===========

This function allocates a root device and registers it using ``device_register``. In order to free the returned device, use ``root_device_unregister``.

Root devices are dummy devices which allow other devices to be grouped under /sys/devices. Use this function to allocate a root device and then use it as the parent of any device
which should appear under /sys/devices/{name}

The /sys/devices/{name} directory will also contain a 'module' symlink which points to the ``owner`` directory in sysfs.

Returns ``struct device`` pointer on success, or ``ERR_PTR`` on error.


Note
====

You probably want to use ``root_device_register``.
