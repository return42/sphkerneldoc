.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-rphy-delete:

===============
sas_rphy_delete
===============

*man sas_rphy_delete(9)*

*4.6.0-rc5*

remove and free SAS remote PHY


Synopsis
========

.. c:function:: void sas_rphy_delete( struct sas_rphy * rphy )

Arguments
=========

``rphy``
    SAS remote PHY to remove and free


Description
===========

Removes the specified SAS remote PHY and frees it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
