.. -*- coding: utf-8; mode: rst -*-

.. _API-nr-free-zone-pages:

==================
nr_free_zone_pages
==================

*man nr_free_zone_pages(9)*

*4.6.0-rc5*

count number of pages beyond high watermark


Synopsis
========

.. c:function:: unsigned long nr_free_zone_pages( int offset )

Arguments
=========

``offset``
    The zone index of the highest zone


Description
===========

``nr_free_zone_pages`` counts the number of counts pages which are
beyond the high watermark within all zones at or below a given zone
index. For each zone, the number of pages is calculated as:
managed_pages - high_pages


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
