
.. _API-d-lookup:

========
d_lookup
========

*man d_lookup(9)*

*4.6.0-rc1*

search for a dentry


Synopsis
========

.. c:function:: struct dentry ⋆ d_lookup( const struct dentry * parent, const struct qstr * name )

Arguments
=========

``parent``
    parent dentry

``name``
    qstr of name we wish to find


Returns
=======

dentry, or NULL

d_lookup searches the children of the parent dentry for the name in question. If the dentry is found its reference count is incremented and the dentry is returned. The caller must
use dput to free the entry when it has finished using it. ``NULL`` is returned if the dentry does not exist.
