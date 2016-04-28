.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-port-id:

===========
hsi_port_id
===========

*man hsi_port_id(9)*

*4.6.0-rc5*

Gets the port number a client is attached to


Synopsis
========

.. c:function:: unsigned int hsi_port_id( struct hsi_client * cl )

Arguments
=========

``cl``
    Pointer to HSI client


Description
===========

Return the port number associated to the client


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
