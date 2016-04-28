.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-rphy-unlink:

===============
sas_rphy_unlink
===============

*man sas_rphy_unlink(9)*

*4.6.0-rc5*

unlink SAS remote PHY


Synopsis
========

.. c:function:: void sas_rphy_unlink( struct sas_rphy * rphy )

Arguments
=========

``rphy``
    SAS remote phy to unlink from its parent port


Description
===========

Removes port reference to an rphy


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
