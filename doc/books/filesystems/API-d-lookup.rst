.. -*- coding: utf-8; mode: rst -*-

.. _API-d-lookup:

========
d_lookup
========

*man d_lookup(9)*

*4.6.0-rc5*

search for a dentry


Synopsis
========

.. c:function:: struct dentry * d_lookup( const struct dentry * parent, const struct qstr * name )

Arguments
=========

``parent``
    parent dentry

``name``
    qstr of name we wish to find


Returns
=======

dentry, or NULL

d_lookup searches the children of the parent dentry for the name in
question. If the dentry is found its reference count is incremented and
the dentry is returned. The caller must use dput to free the entry when
it has finished using it. ``NULL`` is returned if the dentry does not
exist.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
