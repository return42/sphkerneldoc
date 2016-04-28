.. -*- coding: utf-8; mode: rst -*-

.. _API-request-resource-conflict:

=========================
request_resource_conflict
=========================

*man request_resource_conflict(9)*

*4.6.0-rc5*

request and reserve an I/O or memory resource


Synopsis
========

.. c:function:: struct resource * request_resource_conflict( struct resource * root, struct resource * new )

Arguments
=========

``root``
    root resource descriptor

``new``
    resource descriptor desired by caller


Description
===========

Returns 0 for success, conflict resource on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
