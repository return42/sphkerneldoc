
.. _API-sas-rphy-delete:

===============
sas_rphy_delete
===============

*man sas_rphy_delete(9)*

*4.6.0-rc1*

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
