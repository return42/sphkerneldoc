
.. _API-disk-part-iter-exit:

===================
disk_part_iter_exit
===================

*man disk_part_iter_exit(9)*

*4.6.0-rc1*

finish up partition iteration


Synopsis
========

.. c:function:: void disk_part_iter_exit( struct disk_part_iter * piter )

Arguments
=========

``piter``
    iter of interest


Description
===========

Called when iteration is over. Cleans up ``piter``.


CONTEXT
=======

Don't care.
