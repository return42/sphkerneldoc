
.. _API-blk-add-trace-bio:

=================
blk_add_trace_bio
=================

*man blk_add_trace_bio(9)*

*4.6.0-rc1*

Add a trace for a bio oriented action


Synopsis
========

.. c:function:: void blk_add_trace_bio( struct request_queue * q, struct bio * bio, u32 what, int error )

Arguments
=========

``q``
    queue the io is for

``bio``
    the source bio

``what``
    the action

``error``
    error, if any


Description
===========

Records an action against a bio. Will log the bio offset + size.
