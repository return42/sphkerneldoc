.. -*- coding: utf-8; mode: rst -*-

.. _API---request-region:

================
__request_region
================

*man __request_region(9)*

*4.6.0-rc5*

create a new busy resource region


Synopsis
========

.. c:function:: struct resource * __request_region( struct resource * parent, resource_size_t start, resource_size_t n, const char * name, int flags )

Arguments
=========

``parent``
    parent resource descriptor

``start``
    resource start address

``n``
    resource region size

``name``
    reserving caller's ID string

``flags``
    IO resource flags


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
