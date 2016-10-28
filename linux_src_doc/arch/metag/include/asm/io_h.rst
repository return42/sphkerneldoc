.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/include/asm/io.h

.. _`ioremap`:

ioremap
=======

.. c:function::  ioremap( offset,  size)

    map bus memory into CPU space

    :param  offset:
        bus address of the memory

    :param  size:
        size of the resource to map

.. _`ioremap.description`:

Description
-----------

ioremap performs a platform specific sequence of operations to
make bus memory CPU accessible via the readb/readw/readl/writeb/
writew/writel functions and the other mmio helpers. The returned
address is not guaranteed to be usable directly as a virtual
address.

.. This file was automatic generated / don't edit.

