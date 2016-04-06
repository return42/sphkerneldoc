
.. _API-blk-rq-unmap-user:

=================
blk_rq_unmap_user
=================

*man blk_rq_unmap_user(9)*

*4.6.0-rc1*

unmap a request with user data


Synopsis
========

.. c:function:: int blk_rq_unmap_user( struct bio * bio )

Arguments
=========

``bio``
    start of bio list


Description
===========

Unmap a rq previously mapped by ``blk_rq_map_user``. The caller must supply the original rq->bio from the ``blk_rq_map_user`` return, since the I/O completion may have changed
rq->bio.
