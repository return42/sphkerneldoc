
.. _API-request-resource:

================
request_resource
================

*man request_resource(9)*

*4.6.0-rc1*

request and reserve an I/O or memory resource


Synopsis
========

.. c:function:: int request_resource( struct resource * root, struct resource * new )

Arguments
=========

``root``
    root resource descriptor

``new``
    resource descriptor desired by caller


Description
===========

Returns 0 for success, negative error code on error.
