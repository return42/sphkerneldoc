
.. _API-blk-add-trace-bio-remap:

=======================
blk_add_trace_bio_remap
=======================

*man blk_add_trace_bio_remap(9)*

*4.6.0-rc1*

Add a trace for a bio-remap operation


Synopsis
========

.. c:function:: void blk_add_trace_bio_remap( void * ignore, struct request_queue * q, struct bio * bio, dev_t dev, sector_t from )

Arguments
=========

``ignore``
    trace callback data parameter (not used)

``q``
    queue the io is for

``bio``
    the source bio

``dev``
    target device

``from``
    source sector


Description
===========

Device mapper or raid target sometimes need to split a bio because it spans a stripe (or similar). Add a trace for that action.
