
.. _API-media-device-get-devres:

=======================
media_device_get_devres
=======================

*man media_device_get_devres(9)*

*4.6.0-rc1*

get media device as device resource creates if one doesn't exist


Synopsis
========

.. c:function:: struct media_device ⋆ media_device_get_devres( struct device * dev )

Arguments
=========

``dev``
    pointer to struct ``device``.


Description
===========

Sometimes, the media controller ``media_device`` needs to be shared by more than one driver. This function adds support for that, by dynamically allocating the ``media_device`` and
allowing it to be obtained from the struct ``device`` associated with the common device where all sub-device components belong. So, for example, on an USB device with multiple
interfaces, each interface may be handled by a separate per-interface drivers. While each interface have its own ``device``, they all share a common ``device`` associated with the
hole USB device.
