
.. _API-sas-end-device-alloc:

====================
sas_end_device_alloc
====================

*man sas_end_device_alloc(9)*

*4.6.0-rc1*

allocate an rphy for an end device


Synopsis
========

.. c:function:: struct sas_rphy ⋆ sas_end_device_alloc( struct sas_port * parent )

Arguments
=========

``parent``
    which port


Description
===========

Allocates an SAS remote PHY structure, connected to ``parent``.


Returns
=======

SAS PHY allocated or ``NULL`` if the allocation failed.
