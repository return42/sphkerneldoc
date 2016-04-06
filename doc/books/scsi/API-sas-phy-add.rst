
.. _API-sas-phy-add:

===========
sas_phy_add
===========

*man sas_phy_add(9)*

*4.6.0-rc1*

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
