.. -*- coding: utf-8; mode: rst -*-

.. _API-idr-replace:

===========
idr_replace
===========

*man idr_replace(9)*

*4.6.0-rc5*

replace pointer for given id


Synopsis
========

.. c:function:: void * idr_replace( struct idr * idp, void * ptr, int id )

Arguments
=========

``idp``
    idr handle

``ptr``
    pointer you want associated with the id

``id``
    lookup key


Description
===========

Replace the pointer registered with an id and return the old value. A
``-ENOENT`` return indicates that ``id`` was not found. A ``-EINVAL``
return indicates that ``id`` was not within valid constraints.

The caller must serialize with writers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
