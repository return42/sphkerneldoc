
.. _API-sas-rphy-add:

============
sas_rphy_add
============

*man sas_rphy_add(9)*

*4.6.0-rc1*

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
