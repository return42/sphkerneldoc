.. -*- coding: utf-8; mode: rst -*-

.. _API-page-cache-sync-readahead:

=========================
page_cache_sync_readahead
=========================

*man page_cache_sync_readahead(9)*

*4.6.0-rc5*

generic file readahead


Synopsis
========

.. c:function:: void page_cache_sync_readahead( struct address_space * mapping, struct file_ra_state * ra, struct file * filp, pgoff_t offset, unsigned long req_size )

Arguments
=========

``mapping``
    address_space which holds the pagecache and I/O vectors

``ra``
    file_ra_state which holds the readahead state

``filp``
    passed on to ->``readpage`` and ->``readpages``

``offset``
    start offset into ``mapping``, in pagecache page-sized units

``req_size``
    hint: total size of the read which the caller is performing in
    pagecache pages


Description
===========

``page_cache_sync_readahead`` should be called when a cache miss
happened: it will submit the read. The readahead logic may decide to
piggyback more pages onto the read request if access patterns suggest it
will improve performance.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
