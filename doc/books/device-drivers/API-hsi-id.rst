.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-id:

======
hsi_id
======

*man hsi_id(9)*

*4.6.0-rc5*

Get HSI controller ID associated to a client


Synopsis
========

.. c:function:: unsigned int hsi_id( struct hsi_client * cl )

Arguments
=========

``cl``
    Pointer to a HSI client


Description
===========

Return the controller id where the client is attached to


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
