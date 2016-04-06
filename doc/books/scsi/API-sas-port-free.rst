
.. _API-sas-port-free:

=============
sas_port_free
=============

*man sas_port_free(9)*

*4.6.0-rc1*

free a SAS PORT


Synopsis
========

.. c:function:: void sas_port_free( struct sas_port * port )

Arguments
=========

``port``
    SAS PORT to free


Description
===========

Frees the specified SAS PORT.


Note
====

This function must only be called on a PORT that has not successfully been added using ``sas_port_add``.
