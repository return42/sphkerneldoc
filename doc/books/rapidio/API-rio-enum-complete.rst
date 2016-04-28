.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-enum-complete:

=================
rio_enum_complete
=================

*man rio_enum_complete(9)*

*4.6.0-rc5*

Tests if enumeration of a network is complete


Synopsis
========

.. c:function:: int rio_enum_complete( struct rio_mport * port )

Arguments
=========

``port``
    Master port to send transaction


Description
===========

Tests the PGCCSR discovered bit for non-zero value (enumeration complete
flag). Return ``1`` if enumeration is complete or ``0`` if enumeration
is incomplete.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
