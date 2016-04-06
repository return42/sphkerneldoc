
.. _API-blk-rq-prep-clone:

=================
blk_rq_prep_clone
=================

*man blk_rq_prep_clone(9)*

*4.6.0-rc1*

Helper function to setup clone request


Synopsis
========

.. c:function:: int blk_rq_prep_clone( struct request * rq, struct request * rq_src, struct bio_set * bs, gfp_t gfp_mask, int (*bio_ctr) struct bio *, struct bio *, void *, void * data )

Arguments
=========

``rq``
    the request to be setup

``rq_src``
    original request to be cloned

``bs``
    bio_set that bios for clone are allocated from

``gfp_mask``
    memory allocation mask for bio

``bio_ctr``
    setup function to be called for each clone bio. Returns ``0`` for success, non ``0`` for failure.

``data``
    private data to be passed to ``bio_ctr``


Description
===========

Clones bios in ``rq_src`` to ``rq``, and copies attributes of ``rq_src`` to ``rq``. The actual data parts of ``rq_src`` (e.g. ->cmd, ->sense) are not copied, and copying such parts
is the caller's responsibility. Also, pages which the original bios are pointing to are not copied and the cloned bios just point same pages. So cloned bios must be completed
before original bios, which means the caller must complete ``rq`` before ``rq_src``.
