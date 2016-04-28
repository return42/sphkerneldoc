.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-rq-count-integrity-sg:

=========================
blk_rq_count_integrity_sg
=========================

*man blk_rq_count_integrity_sg(9)*

*4.6.0-rc5*

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

Returns the number of elements required in a scatterlist corresponding
to the integrity metadata in a bio.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
