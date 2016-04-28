.. -*- coding: utf-8; mode: rst -*-

.. _API-page-cache-async-readahead:

==========================
page_cache_async_readahead
==========================

*man page_cache_async_readahead(9)*

*4.6.0-rc5*

file readahead for marked pages


Synopsis
========

.. c:function:: void page_cache_async_readahead( struct address_space * mapping, struct file_ra_state * ra, struct file * filp, struct page * page, pgoff_t offset, unsigned long req_size )

Arguments
=========

``mapping``
    address_space which holds the pagecache and I/O vectors

``ra``
    file_ra_state which holds the readahead state

``filp``
    passed on to ->``readpage`` and ->``readpages``

``page``
    the page at ``offset`` which has the PG_readahead flag set

``offset``
    start offset into ``mapping``, in pagecache page-sized units

``req_size``
    hint: total size of the read which the caller is performing in
    pagecache pages


Description
===========

``page_cache_async_readahead`` should be called when a page is used
which has the PG_readahead flag; this is a marker to suggest that the
application has used up enough of the readahead window that we should
start pulling in more pages.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
