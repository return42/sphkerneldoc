.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-port-delete:

===============
sas_port_delete
===============

*man sas_port_delete(9)*

*4.6.0-rc5*

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

Removes the specified SAS PORT. If the SAS PORT has an associated phys,
unlink them from the port as well.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
