.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-port-add-phy:

================
sas_port_add_phy
================

*man sas_port_add_phy(9)*

*4.6.0-rc5*

add another phy to a port to form a wide port


Synopsis
========

.. c:function:: void sas_port_add_phy( struct sas_port * port, struct sas_phy * phy )

Arguments
=========

``port``
    port to add the phy to

``phy``
    phy to add


Description
===========

When a port is initially created, it is empty (has no phys). All ports
must have at least one phy to operated, and all wide ports must have at
least two. The current code makes no difference between ports and wide
ports, but the only object that can be connected to a remote device is a
port, so ports must be formed on all devices with phys if they're
connected to anything.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
