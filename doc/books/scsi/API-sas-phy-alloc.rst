.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-phy-alloc:

=============
sas_phy_alloc
=============

*man sas_phy_alloc(9)*

*4.6.0-rc5*

allocates and initialize a SAS PHY structure


Synopsis
========

.. c:function:: struct sas_phy * sas_phy_alloc( struct device * parent, int number )

Arguments
=========

``parent``
    Parent device

``number``
    Phy index


Description
===========

Allocates an SAS PHY structure. It will be added in the device tree
below the device specified by ``parent``, which has to be either a
Scsi_Host or sas_rphy.


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
