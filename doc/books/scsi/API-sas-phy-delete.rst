
.. _API-sas-phy-delete:

==============
sas_phy_delete
==============

*man sas_phy_delete(9)*

*4.6.0-rc1*

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

Removes the specified SAS PHY. If the SAS PHY has an associated remote PHY it is removed before.
