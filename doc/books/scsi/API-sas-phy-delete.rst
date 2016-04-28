.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-phy-delete:

==============
sas_phy_delete
==============

*man sas_phy_delete(9)*

*4.6.0-rc5*

remove SAS PHY


Synopsis
========

.. c:function:: void sas_phy_delete( struct sas_phy * phy )

Arguments
=========

``phy``
    SAS PHY to remove


Description
===========

Removes the specified SAS PHY. If the SAS PHY has an associated remote
PHY it is removed before.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
