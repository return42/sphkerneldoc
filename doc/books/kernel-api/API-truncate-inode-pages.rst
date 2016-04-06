
.. _API-truncate-inode-pages:

====================
truncate_inode_pages
====================

*man truncate_inode_pages(9)*

*4.6.0-rc1*

truncate ⋆all⋆ the pages from an offset


Synopsis
========

.. c:function:: void truncate_inode_pages( struct address_space * mapping, loff_t lstart )

Arguments
=========

``mapping``
    mapping to truncate

``lstart``
    offset from which to truncate


Description
===========

Called under (and serialised by) inode->i_mutex.


Note
====

When this function returns, there can be a page in the process of deletion (inside ``__delete_from_page_cache``) in the specified range. Thus mapping->nrpages can be non-zero when
this function returns even after truncation of the whole mapping.
