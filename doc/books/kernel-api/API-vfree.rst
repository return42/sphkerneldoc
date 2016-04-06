
.. _API-vfree:

=====
vfree
=====

*man vfree(9)*

*4.6.0-rc1*

release memory allocated by ``vmalloc``


Synopsis
========

.. c:function:: void vfree( const void * addr )

Arguments
=========

``addr``
    memory base address


Description
===========

Free the virtually continuous memory area starting at ``addr``, as obtained from ``vmalloc``, ``vmalloc_32`` or ``__vmalloc``. If ``addr`` is NULL, no operation is performed.

Must not be called in NMI context (strictly speaking, only if we don't have CONFIG_ARCH_HAVE_NMI_SAFE_CMPXCHG, but making the calling conventions for ``vfree`` arch-depenedent
would be a really bad idea)


NOTE
====

assumes that the object at ⋆addr has a size >= sizeof(llist_node)
