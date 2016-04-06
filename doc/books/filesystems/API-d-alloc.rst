
.. _API-d-alloc:

=======
d_alloc
=======

*man d_alloc(9)*

*4.6.0-rc1*

allocate a dcache entry


Synopsis
========

.. c:function:: struct dentry ⋆ d_alloc( struct dentry * parent, const struct qstr * name )

Arguments
=========

``parent``
    parent of entry to allocate

``name``
    qstr of the name


Description
===========

Allocates a dentry. It returns ``NULL`` if there is insufficient memory available. On a success the dentry is returned. The name passed in is copied and the copy passed in may be
reused after this call.
