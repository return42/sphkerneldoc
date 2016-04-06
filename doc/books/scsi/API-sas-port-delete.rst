
.. _API-sas-port-delete:

===============
sas_port_delete
===============

*man sas_port_delete(9)*

*4.6.0-rc1*

remove SAS PORT


Synopsis
========

.. c:function:: void sas_port_delete( struct sas_port * port )

Arguments
=========

``port``
    SAS PORT to remove


Description
===========

Removes the specified SAS PORT. If the SAS PORT has an associated phys, unlink them from the port as well.
