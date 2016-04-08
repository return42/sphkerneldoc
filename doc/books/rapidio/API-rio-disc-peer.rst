
.. _API-rio-disc-peer:

=============
rio_disc_peer
=============

*man rio_disc_peer(9)*

*4.6.0-rc1*

Recursively discovers a RIO network through a master port


Synopsis
========

.. c:function:: int rio_disc_peer( struct rio_net * net, struct rio_mport * port, u16 destid, u8 hopcount, struct rio_dev * prev, int prev_port )

Arguments
=========

``net``
    RIO network being discovered

``port``
    Master port to send transactions

``destid``
    Current destination ID in network

``hopcount``
    Number of hops into the network

``prev``
    previous rio_dev

``prev_port``
    previous port number


Description
===========

Recursively discovers a RIO network. Transactions are sent via the master port passed in ``port``.
