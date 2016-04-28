.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-phy-free:

============
sas_phy_free
============

*man sas_phy_free(9)*

*4.6.0-rc5*

free a SAS PHY


Synopsis
========

.. c:function:: void sas_phy_free( struct sas_phy * phy )

Arguments
=========

``phy``
    SAS PHY to free


Description
===========

Frees the specified SAS PHY.


Note
====

This function must only be called on a PHY that has not successfully
been added using ``sas_phy_add``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
