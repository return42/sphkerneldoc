.. -*- coding: utf-8; mode: rst -*-

.. _API-request-resource:

================
request_resource
================

*man request_resource(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
