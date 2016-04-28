.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-prime-pages-to-sg:

=====================
drm_prime_pages_to_sg
=====================

*man drm_prime_pages_to_sg(9)*

*4.6.0-rc5*

converts a page array into an sg list


Synopsis
========

.. c:function:: struct sg_table * drm_prime_pages_to_sg( struct page ** pages, unsigned int nr_pages )

Arguments
=========

``pages``
    pointer to the array of page pointers to convert

``nr_pages``
    length of the page vector


Description
===========

This helper creates an sg table object from a set of pages the driver is
responsible for mapping the pages into the importers address space for
use with dma_buf itself.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
