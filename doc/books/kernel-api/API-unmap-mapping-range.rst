
.. _API-unmap-mapping-range:

===================
unmap_mapping_range
===================

*man unmap_mapping_range(9)*

*4.6.0-rc1*

unmap the portion of all mmaps in the specified address_space corresponding to the specified page range in the underlying file.


Synopsis
========

.. c:function:: void unmap_mapping_range( struct address_space * mapping, loff_t const holebegin, loff_t const holelen, int even_cows )

Arguments
=========

``mapping``
    the address space containing mmaps to be unmapped.

``holebegin``
    byte in first page to unmap, relative to the start of the underlying file. This will be rounded down to a PAGE_SIZE boundary. Note that this is different from
    ``truncate_pagecache``, which must keep the partial page. In contrast, we must get rid of partial pages.

``holelen``
    size of prospective hole in bytes. This will be rounded up to a PAGE_SIZE boundary. A holelen of zero truncates to the end of the file.

``even_cows``
    1 when truncating a file, unmap even private COWed pages; but 0 when invalidating pagecache, don't throw away private data.
