
.. _API-get-ccwdev-by-busid:

===================
get_ccwdev_by_busid
===================

*man get_ccwdev_by_busid(9)*

*4.6.0-rc1*

obtain device from a bus id


Synopsis
========

.. c:function:: struct ccw_device ⋆ get_ccwdev_by_busid( struct ccw_driver * cdrv, const char * bus_id )

Arguments
=========

``cdrv``
    driver the device is owned by

``bus_id``
    bus id of the device to be searched


Description
===========

This function searches all devices owned by ``cdrv`` for a device with a bus id matching ``bus_id``.


Returns
=======

If a match is found, its reference count of the found device is increased and it is returned; else ``NULL`` is returned.
