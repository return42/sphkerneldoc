.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-rphy-free:

=============
sas_rphy_free
=============

*man sas_rphy_free(9)*

*4.6.0-rc5*

free a SAS remote PHY


Synopsis
========

.. c:function:: void sas_rphy_free( struct sas_rphy * rphy )

Arguments
=========

``rphy``
    SAS remote PHY to free


Description
===========

Frees the specified SAS remote PHY.


Note
====

This function must only be called on a remote PHY that has not
successfully been added using ``sas_rphy_add`` (or has been
``sas_rphy_remove``'d)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
