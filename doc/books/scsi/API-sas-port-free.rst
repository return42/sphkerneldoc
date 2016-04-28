.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-port-free:

=============
sas_port_free
=============

*man sas_port_free(9)*

*4.6.0-rc5*

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

This function must only be called on a PORT that has not successfully
been added using ``sas_port_add``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
