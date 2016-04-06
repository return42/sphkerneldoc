
.. _API-nr-free-pagecache-pages:

=======================
nr_free_pagecache_pages
=======================

*man nr_free_pagecache_pages(9)*

*4.6.0-rc1*

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

``nr_free_pagecache_pages`` counts the number of pages which are beyond the high watermark within all zones.
