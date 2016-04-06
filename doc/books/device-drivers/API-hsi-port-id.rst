
.. _API-hsi-port-id:

===========
hsi_port_id
===========

*man hsi_port_id(9)*

*4.6.0-rc1*

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
