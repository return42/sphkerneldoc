.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-phy-add:

===========
sas_phy_add
===========

*man sas_phy_add(9)*

*4.6.0-rc5*

add a SAS PHY to the device hierarchy


Synopsis
========

.. c:function:: int sas_phy_add( struct sas_phy * phy )

Arguments
=========

``phy``
    The PHY to be added


Description
===========

Publishes a SAS PHY to the rest of the system.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
