
.. _API-request-resource-conflict:

=========================
request_resource_conflict
=========================

*man request_resource_conflict(9)*

*4.6.0-rc1*

request and reserve an I/O or memory resource


Synopsis
========

.. c:function:: struct resource ⋆ request_resource_conflict( struct resource * root, struct resource * new )

Arguments
=========

``root``
    root resource descriptor

``new``
    resource descriptor desired by caller


Description
===========

Returns 0 for success, conflict resource on error.
