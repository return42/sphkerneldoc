.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-sport-is-active:

===================
rio_sport_is_active
===================

*man rio_sport_is_active(9)*

*4.6.0-rc5*

Tests if a switch port has an active connection.


Synopsis
========

.. c:function:: int rio_sport_is_active( struct rio_mport * port, u16 destid, u8 hopcount, int sport )

Arguments
=========

``port``
    Master port to send transaction

``destid``
    Associated destination ID for switch

``hopcount``
    Hopcount to reach switch

``sport``
    Switch port number


Description
===========

Reads the port error status CSR for a particular switch port to
determine if the port has an active link. Returns
``RIO_PORT_N_ERR_STS_PORT_OK`` if the port is active or ``0`` if it is
inactive.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
