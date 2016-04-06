
.. _API-idr-replace:

===========
idr_replace
===========

*man idr_replace(9)*

*4.6.0-rc1*

replace pointer for given id


Synopsis
========

.. c:function:: void ⋆ idr_replace( struct idr * idp, void * ptr, int id )

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

Replace the pointer registered with an id and return the old value. A ``-ENOENT`` return indicates that ``id`` was not found. A ``-EINVAL`` return indicates that ``id`` was not
within valid constraints.

The caller must serialize with writers.
