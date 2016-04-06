
.. _API-blk-queue-chunk-sectors:

=======================
blk_queue_chunk_sectors
=======================

*man blk_queue_chunk_sectors(9)*

*4.6.0-rc1*

set size of the chunk for this queue


Synopsis
========

.. c:function:: void blk_queue_chunk_sectors( struct request_queue * q, unsigned int chunk_sectors )

Arguments
=========

``q``
    the request queue for the device

``chunk_sectors``
    chunk sectors in the usual 512b unit


Description
===========

If a driver doesn't want IOs to cross a given chunk size, it can set this limit and prevent merging across chunks. Note that the chunk size must currently be a power-of-2 in
sectors. Also note that the block layer must accept a page worth of data at any offset. So if the crossing of chunks is a hard limitation in the driver, it must still be prepared
to split single page bios.
