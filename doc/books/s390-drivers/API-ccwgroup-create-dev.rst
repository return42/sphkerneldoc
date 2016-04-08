
.. _API-ccwgroup-create-dev:

===================
ccwgroup_create_dev
===================

*man ccwgroup_create_dev(9)*

*4.6.0-rc1*

create and register a ccw group device


Synopsis
========

.. c:function:: int ccwgroup_create_dev( struct device * parent, struct ccwgroup_driver * gdrv, int num_devices, const char * buf )

Arguments
=========

``parent``
    parent device for the new device

``gdrv``
    driver for the new group device

``num_devices``
    number of slave devices

``buf``
    buffer containing comma separated bus ids of slave devices


Description
===========

Create and register a new ccw group device as a child of ``parent``. Slave devices are obtained from the list of bus ids given in ``buf``.


Returns
=======

``0`` on success and an error code on failure.


Context
=======

non-atomic
