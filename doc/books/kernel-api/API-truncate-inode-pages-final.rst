
.. _API-truncate-inode-pages-final:

==========================
truncate_inode_pages_final
==========================

*man truncate_inode_pages_final(9)*

*4.6.0-rc1*

truncate ⋆all⋆ pages before inode dies


Synopsis
========

.. c:function:: void truncate_inode_pages_final( struct address_space * mapping )

Arguments
=========

``mapping``
    mapping to truncate


Description
===========

Called under (and serialized by) inode->i_mutex.

Filesystems have to use this in the .evict_inode path to inform the VM that this is the final truncate and the inode is going away.
