.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-get-phys-port-name:

======================
dev_get_phys_port_name
======================

*man dev_get_phys_port_name(9)*

*4.6.0-rc5*

Get device physical port name


Synopsis
========

.. c:function:: int dev_get_phys_port_name( struct net_device * dev, char * name, size_t len )

Arguments
=========

``dev``
    device

``name``
    port name

``len``
    limit of bytes to copy to name


Description
===========

Get device physical port name


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
