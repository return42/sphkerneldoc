
.. _API-rio-enum-peer:

=============
rio_enum_peer
=============

*man rio_enum_peer(9)*

*4.6.0-rc1*

Recursively enumerate a RIO network through a master port


Synopsis
========

.. c:function:: int rio_enum_peer( struct rio_net * net, struct rio_mport * port, u8 hopcount, struct rio_dev * prev, int prev_port )

Arguments
=========

``net``
    RIO network being enumerated

``port``
    Master port to send transactions

``hopcount``
    Number of hops into the network

``prev``
    Previous RIO device connected to the enumerated one

``prev_port``
    Port on previous RIO device


Description
===========

Recursively enumerates a RIO network. Transactions are sent via the master port passed in ``port``.
