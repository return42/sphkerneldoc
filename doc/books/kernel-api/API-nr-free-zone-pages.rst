
.. _API-nr-free-zone-pages:

==================
nr_free_zone_pages
==================

*man nr_free_zone_pages(9)*

*4.6.0-rc1*

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

``nr_free_zone_pages`` counts the number of counts pages which are beyond the high watermark within all zones at or below a given zone index. For each zone, the number of pages is
calculated as: managed_pages - high_pages
