
.. _API-sas-phy-free:

============
sas_phy_free
============

*man sas_phy_free(9)*

*4.6.0-rc1*

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

This function must only be called on a PHY that has not successfully been added using ``sas_phy_add``.
