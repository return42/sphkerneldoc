
.. _API-rio-enum-host:

=============
rio_enum_host
=============

*man rio_enum_host(9)*

*4.6.0-rc1*

Set host lock and initialize host destination ID


Synopsis
========

.. c:function:: int rio_enum_host( struct rio_mport * port )

Arguments
=========

``port``
    Master port to issue transaction


Description
===========

Sets the local host master port lock and destination ID register with the host device ID value. The host device ID value is provided by the platform. Returns ``0`` on success or
``-1`` on failure.
