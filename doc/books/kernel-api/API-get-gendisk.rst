
.. _API-get-gendisk:

===========
get_gendisk
===========

*man get_gendisk(9)*

*4.6.0-rc1*

get partitioning information for a given device


Synopsis
========

.. c:function:: struct gendisk ⋆ get_gendisk( dev_t devt, int * partno )

Arguments
=========

``devt``
    device to get partitioning information for

``partno``
    returned partition index


Description
===========

This function gets the structure containing partitioning information for the given device ``devt``.
