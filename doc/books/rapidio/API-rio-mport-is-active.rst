.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-mport-is-active:

===================
rio_mport_is_active
===================

*man rio_mport_is_active(9)*

*4.6.0-rc5*

Tests if master port link is active


Synopsis
========

.. c:function:: int rio_mport_is_active( struct rio_mport * port )

Arguments
=========

``port``
    Master port to test


Description
===========

Reads the port error status CSR for the master port to determine if the
port has an active link. Returns ``RIO_PORT_N_ERR_STS_PORT_OK`` if the
master port is active or ``0`` if it is inactive.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
