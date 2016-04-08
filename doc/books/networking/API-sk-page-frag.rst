
.. _API-sk-page-frag:

============
sk_page_frag
============

*man sk_page_frag(9)*

*4.6.0-rc1*

return an appropriate page_frag


Synopsis
========

.. c:function:: struct page_frag ⋆ sk_page_frag( struct sock * sk )

Arguments
=========

``sk``
    socket


Description
===========

If socket allocation mode allows current thread to sleep, it means its safe to use the per task page_frag instead of the per socket one.
