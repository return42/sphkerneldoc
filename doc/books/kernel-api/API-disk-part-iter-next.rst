
.. _API-disk-part-iter-next:

===================
disk_part_iter_next
===================

*man disk_part_iter_next(9)*

*4.6.0-rc1*

proceed iterator to the next partition and return it


Synopsis
========

.. c:function:: struct hd_struct ⋆ disk_part_iter_next( struct disk_part_iter * piter )

Arguments
=========

``piter``
    iterator of interest


Description
===========

Proceed ``piter`` to the next partition and return it.


CONTEXT
=======

Don't care.
