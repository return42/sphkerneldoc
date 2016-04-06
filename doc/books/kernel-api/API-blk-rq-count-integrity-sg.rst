
.. _API-blk-rq-count-integrity-sg:

=========================
blk_rq_count_integrity_sg
=========================

*man blk_rq_count_integrity_sg(9)*

*4.6.0-rc1*

Count number of integrity scatterlist elements


Synopsis
========

.. c:function:: int blk_rq_count_integrity_sg( struct request_queue * q, struct bio * bio )

Arguments
=========

``q``
    request queue

``bio``
    bio with integrity metadata attached


Description
===========

Returns the number of elements required in a scatterlist corresponding to the integrity metadata in a bio.
