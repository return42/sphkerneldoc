.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-page-frag:

============
sk_page_frag
============

*man sk_page_frag(9)*

*4.6.0-rc5*

return an appropriate page_frag


Synopsis
========

.. c:function:: struct page_frag * sk_page_frag( struct sock * sk )

Arguments
=========

``sk``
    socket


Description
===========

If socket allocation mode allows current thread to sleep, it means its
safe to use the per task page_frag instead of the per socket one.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
