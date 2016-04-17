.. -*- coding: utf-8; mode: rst -*-

=========
ioremap.c
=========


.. _`ioremap_nocache`:

ioremap_nocache
===============

.. c:function:: void __iomem *ioremap_nocache (unsigned long phys_addr, unsigned long size)

    map bus memory into CPU space

    :param unsigned long phys_addr:

        *undescribed*

    :param unsigned long size:
        size of the resource to map



.. _`ioremap_nocache.description`:

Description
-----------

Must be freed with iounmap.

