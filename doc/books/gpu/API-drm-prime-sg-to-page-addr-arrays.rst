.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-prime-sg-to-page-addr-arrays:

================================
drm_prime_sg_to_page_addr_arrays
================================

*man drm_prime_sg_to_page_addr_arrays(9)*

*4.6.0-rc5*

convert an sg table into a page array


Synopsis
========

.. c:function:: int drm_prime_sg_to_page_addr_arrays( struct sg_table * sgt, struct page ** pages, dma_addr_t * addrs, int max_pages )

Arguments
=========

``sgt``
    scatter-gather table to convert

``pages``
    array of page pointers to store the page array in

``addrs``
    optional array to store the dma bus address of each page

``max_pages``
    size of both the passed-in arrays


Description
===========

Exports an sg table into an array of pages and addresses. This is
currently required by the TTM driver in order to do correct fault
handling.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
