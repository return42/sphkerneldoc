
.. _API-rio-enum-complete:

=================
rio_enum_complete
=================

*man rio_enum_complete(9)*

*4.6.0-rc1*

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

Tests the PGCCSR discovered bit for non-zero value (enumeration complete flag). Return ``1`` if enumeration is complete or ``0`` if enumeration is incomplete.
