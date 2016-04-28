.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-rphy-add:

============
sas_rphy_add
============

*man sas_rphy_add(9)*

*4.6.0-rc5*

add a SAS remote PHY to the device hierarchy


Synopsis
========

.. c:function:: int sas_rphy_add( struct sas_rphy * rphy )

Arguments
=========

``rphy``
    The remote PHY to be added


Description
===========

Publishes a SAS remote PHY to the rest of the system.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
