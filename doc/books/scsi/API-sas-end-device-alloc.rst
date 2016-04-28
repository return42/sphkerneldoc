.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-end-device-alloc:

====================
sas_end_device_alloc
====================

*man sas_end_device_alloc(9)*

*4.6.0-rc5*

allocate an rphy for an end device


Synopsis
========

.. c:function:: struct sas_rphy * sas_end_device_alloc( struct sas_port * parent )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
