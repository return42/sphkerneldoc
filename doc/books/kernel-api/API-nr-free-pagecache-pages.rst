.. -*- coding: utf-8; mode: rst -*-

.. _API-nr-free-pagecache-pages:

=======================
nr_free_pagecache_pages
=======================

*man nr_free_pagecache_pages(9)*

*4.6.0-rc5*

count number of pages beyond high watermark


Synopsis
========

.. c:function:: unsigned long nr_free_pagecache_pages( void )

Arguments
=========

``void``
    no arguments


Description
===========

``nr_free_pagecache_pages`` counts the number of pages which are beyond
the high watermark within all zones.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
