
.. _API-media-device-cleanup:

====================
media_device_cleanup
====================

*man media_device_cleanup(9)*

*4.6.0-rc1*

Cleanups a media device element


Synopsis
========

.. c:function:: void media_device_cleanup( struct media_device * mdev )

Arguments
=========

``mdev``
    pointer to struct ``media_device``


Description
===========

This function that will destroy the graph_mutex that is initialized in ``media_device_init``.
