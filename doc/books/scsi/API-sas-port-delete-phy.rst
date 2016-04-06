
.. _API-sas-port-delete-phy:

===================
sas_port_delete_phy
===================

*man sas_port_delete_phy(9)*

*4.6.0-rc1*

remove a phy from a port or wide port


Synopsis
========

.. c:function:: void sas_port_delete_phy( struct sas_port * port, struct sas_phy * phy )

Arguments
=========

``port``
    port to remove the phy from

``phy``
    phy to remove


Description
===========

This operation is used for tearing down ports again. It must be done to every port or wide port before calling sas_port_delete.
