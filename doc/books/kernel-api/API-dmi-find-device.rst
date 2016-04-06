
.. _API-dmi-find-device:

===============
dmi_find_device
===============

*man dmi_find_device(9)*

*4.6.0-rc1*

find onboard device by type/name


Synopsis
========

.. c:function:: const struct dmi_device ⋆ dmi_find_device( int type, const char * name, const struct dmi_device * from )

Arguments
=========

``type``
    device type or ``DMI_DEV_TYPE_ANY`` to match all device types

``name``
    device name string or ``NULL`` to match all

``from``
    previous device found in search, or ``NULL`` for new search.


Description
===========

Iterates through the list of known onboard devices. If a device is found with a matching ``type`` and ``name``, a pointer to its device structure is returned. Otherwise, ``NULL``
is returned. A new search is initiated by passing ``NULL`` as the ``from`` argument. If ``from`` is not ``NULL``, searches continue from next device.
