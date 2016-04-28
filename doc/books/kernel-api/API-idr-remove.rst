.. -*- coding: utf-8; mode: rst -*-

.. _API-idr-remove:

==========
idr_remove
==========

*man idr_remove(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
