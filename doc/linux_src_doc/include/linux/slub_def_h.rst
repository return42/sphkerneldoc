.. -*- coding: utf-8; mode: rst -*-

==========
slub_def.h
==========


.. _`virt_to_obj`:

virt_to_obj
===========

.. c:function:: void *virt_to_obj (struct kmem_cache *s, const void *slab_page, const void *x)

    returns address of the beginning of object.

    :param struct kmem_cache \*s:
        object's kmem_cache

    :param const void \*slab_page:
        address of slab page

    :param const void \*x:
        address within object memory range



.. _`virt_to_obj.description`:

Description
-----------

Returns address of the beginning of object

