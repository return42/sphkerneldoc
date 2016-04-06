
.. _API-hsi-id:

======
hsi_id
======

*man hsi_id(9)*

*4.6.0-rc1*

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
