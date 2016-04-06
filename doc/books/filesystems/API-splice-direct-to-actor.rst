
.. _API-splice-direct-to-actor:

======================
splice_direct_to_actor
======================

*man splice_direct_to_actor(9)*

*4.6.0-rc1*

splices data directly between two non-pipes


Synopsis
========

.. c:function:: ssize_t splice_direct_to_actor( struct file * in, struct splice_desc * sd, splice_direct_actor * actor )

Arguments
=========

``in``
    file to splice from

``sd``
    actor information on where to splice to

``actor``
    handles the data splicing


Description
===========

This is a special case helper to splice directly between two points, without requiring an explicit pipe. Internally an allocated pipe is cached in the process, and reused during
the lifetime of that process.
