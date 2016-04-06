
.. _API-idr-destroy:

===========
idr_destroy
===========

*man idr_destroy(9)*

*4.6.0-rc1*

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

Free all id mappings and all idp_layers. After this function, ``idp`` is completely unused and can be freed / recycled. The caller is responsible for ensuring that no one else
accesses ``idp`` during or after ``idr_destroy``.

A typical clean-up sequence for objects stored in an idr tree will use ``idr_for_each`` to free all objects, if necessary, then ``idr_destroy`` to free up the id mappings and
cached idr_layers.
