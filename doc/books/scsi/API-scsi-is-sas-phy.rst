.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-is-sas-phy:

===============
scsi_is_sas_phy
===============

*man scsi_is_sas_phy(9)*

*4.6.0-rc5*

check if a struct device represents a SAS PHY


Synopsis
========

.. c:function:: int scsi_is_sas_phy( const struct device * dev )

Arguments
=========

``dev``
    device to check


Returns
=======

``1`` if the device represents a SAS PHY, ``0`` else


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
