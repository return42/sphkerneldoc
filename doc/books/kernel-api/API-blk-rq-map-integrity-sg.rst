
.. _API-blk-rq-map-integrity-sg:

=======================
blk_rq_map_integrity_sg
=======================

*man blk_rq_map_integrity_sg(9)*

*4.6.0-rc1*

Map integrity metadata into a scatterlist


Synopsis
========

.. c:function:: int blk_rq_map_integrity_sg( struct request_queue * q, struct bio * bio, struct scatterlist * sglist )

Arguments
=========

``q``
    request queue

``bio``
    bio with integrity metadata attached

``sglist``
    target scatterlist


Description
===========

Map the integrity vectors in request into a scatterlist. The scatterlist must be big enough to hold all elements. I.e. sized using ``blk_rq_count_integrity_sg``.
