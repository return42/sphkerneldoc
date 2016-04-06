
.. _API-sas-rphy-unlink:

===============
sas_rphy_unlink
===============

*man sas_rphy_unlink(9)*

*4.6.0-rc1*

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
