.. -*- coding: utf-8; mode: rst -*-

.. _API-d-alloc:

=======
d_alloc
=======

*man d_alloc(9)*

*4.6.0-rc5*

allocate a dcache entry


Synopsis
========

.. c:function:: struct dentry * d_alloc( struct dentry * parent, const struct qstr * name )

Arguments
=========

``parent``
    parent of entry to allocate

``name``
    qstr of the name


Description
===========

Allocates a dentry. It returns ``NULL`` if there is insufficient memory
available. On a success the dentry is returned. The name passed in is
copied and the copy passed in may be reused after this call.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
