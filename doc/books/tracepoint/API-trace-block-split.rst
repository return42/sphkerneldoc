
.. _API-trace-block-split:

=================
trace_block_split
=================

*man trace_block_split(9)*

*4.6.0-rc1*

split a single bio struct into two bio structs


Synopsis
========

.. c:function:: void trace_block_split( struct request_queue * q, struct bio * bio, unsigned int new_sector )

Arguments
=========

``q``
    queue containing the bio

``bio``
    block operation being split

``new_sector``
    The starting sector for the new bio


Description
===========

The bio request ``bio`` in request queue ``q`` needs to be split into two bio requests. The newly created ``bio`` request starts at ``new_sector``. This split may be required due
to hardware limitation such as operation crossing device boundaries in a RAID system.
