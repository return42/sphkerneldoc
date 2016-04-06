.. -*- coding: utf-8; mode: rst -*-

===============
blk-integrity.c
===============



.. _xref_blk_rq_count_integrity_sg:

blk_rq_count_integrity_sg
=========================

.. c:function:: int blk_rq_count_integrity_sg (struct request_queue * q, struct bio * bio)

    Count number of integrity scatterlist elements

    :param struct request_queue * q:
        request queue

    :param struct bio * bio:
        bio with integrity metadata attached



Description
-----------

Returns the number of elements required in a
scatterlist corresponding to the integrity metadata in a bio.




.. _xref_blk_rq_map_integrity_sg:

blk_rq_map_integrity_sg
=======================

.. c:function:: int blk_rq_map_integrity_sg (struct request_queue * q, struct bio * bio, struct scatterlist * sglist)

    Map integrity metadata into a scatterlist

    :param struct request_queue * q:
        request queue

    :param struct bio * bio:
        bio with integrity metadata attached

    :param struct scatterlist * sglist:
        target scatterlist



Description
-----------

Map the integrity vectors in request into a
scatterlist.  The scatterlist must be big enough to hold all
elements.  I.e. sized using :c:func:`blk_rq_count_integrity_sg`.




.. _xref_blk_integrity_compare:

blk_integrity_compare
=====================

.. c:function:: int blk_integrity_compare (struct gendisk * gd1, struct gendisk * gd2)

    Compare integrity profile of two disks

    :param struct gendisk * gd1:
        Disk to compare

    :param struct gendisk * gd2:
        Disk to compare



Description
-----------

Meta-devices like DM and MD need to verify that all
sub-devices use the same integrity format before advertising to
upper layers that they can send/receive integrity metadata.  This
function can be used to check whether two gendisk devices have
compatible integrity formats.




.. _xref_blk_integrity_register:

blk_integrity_register
======================

.. c:function:: void blk_integrity_register (struct gendisk * disk, struct blk_integrity * template)

    Register a gendisk as being integrity-capable

    :param struct gendisk * disk:
        struct gendisk pointer to make integrity-aware

    :param struct blk_integrity * template:
        block integrity profile to register



Description
-----------

When a device needs to advertise itself as being able to
send/receive integrity metadata it must use this function to register
the capability with the block layer. The template is a blk_integrity
struct with values appropriate for the underlying hardware. See
Documentation/block/data-integrity.txt.




.. _xref_blk_integrity_unregister:

blk_integrity_unregister
========================

.. c:function:: void blk_integrity_unregister (struct gendisk * disk)

    Unregister block integrity profile

    :param struct gendisk * disk:
        disk whose integrity profile to unregister



Description
-----------

This function unregisters the integrity capability from
a block device.


