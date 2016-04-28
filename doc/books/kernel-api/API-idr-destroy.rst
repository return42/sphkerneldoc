.. -*- coding: utf-8; mode: rst -*-

.. _API-idr-destroy:

===========
idr_destroy
===========

*man idr_destroy(9)*

*4.6.0-rc5*

release all cached layers within an idr tree


Synopsis
========

.. c:function:: void idr_destroy( struct idr * idp )

Arguments
=========

``idp``
    idr handle


Description
===========

Free all id mappings and all idp_layers. After this function, ``idp``
is completely unused and can be freed / recycled. The caller is
responsible for ensuring that no one else accesses ``idp`` during or
after ``idr_destroy``.

A typical clean-up sequence for objects stored in an idr tree will use
``idr_for_each`` to free all objects, if necessary, then ``idr_destroy``
to free up the id mappings and cached idr_layers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
