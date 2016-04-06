
.. _API-generic-writepages:

==================
generic_writepages
==================

*man generic_writepages(9)*

*4.6.0-rc1*

walk the list of dirty pages of the given address space and ``writepage`` all of them.


Synopsis
========

.. c:function:: int generic_writepages( struct address_space * mapping, struct writeback_control * wbc )

Arguments
=========

``mapping``
    address space structure to write

``wbc``
    subtract the number of written pages from ⋆ ``wbc``->nr_to_write


Description
===========

This is a library function, which implements the ``writepages`` address_space_operation.
