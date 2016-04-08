
.. _API-dev-alloc-name:

==============
dev_alloc_name
==============

*man dev_alloc_name(9)*

*4.6.0-rc1*

allocate a name for a device


Synopsis
========

.. c:function:: int dev_alloc_name( struct net_device * dev, const char * name )

Arguments
=========

``dev``
    device

``name``
    name format string


Description
===========

Passed a format string - eg “lt\ ``d``” it will try and find a suitable id. It scans list of devices to build up a free map, then chooses the first empty slot. The caller must hold
the dev_base or rtnl lock while allocating the name and adding the device in order to avoid duplicates. Limited to bits_per_byte ⋆ page size devices (ie 32K on most platforms).
Returns the number of the unit assigned or a negative errno code.
