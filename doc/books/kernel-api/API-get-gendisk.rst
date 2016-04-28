.. -*- coding: utf-8; mode: rst -*-

.. _API-get-gendisk:

===========
get_gendisk
===========

*man get_gendisk(9)*

*4.6.0-rc5*

get partitioning information for a given device


Synopsis
========

.. c:function:: struct gendisk * get_gendisk( dev_t devt, int * partno )

Arguments
=========

``devt``
    device to get partitioning information for

``partno``
    returned partition index


Description
===========

This function gets the structure containing partitioning information for
the given device ``devt``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
