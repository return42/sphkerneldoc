
.. _API-idr-remove:

==========
idr_remove
==========

*man idr_remove(9)*

*4.6.0-rc1*

remove the given id and free its slot


Synopsis
========

.. c:function:: void idr_remove( struct idr * idp, int id )

Arguments
=========

``idp``
    idr handle

``id``
    unique key
