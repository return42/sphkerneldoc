.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/riscv/mm/ioremap.c

.. _`iounmap`:

iounmap
=======

.. c:function:: void iounmap(volatile void __iomem *addr)

    Free a IO remapping

    :param addr:
        virtual address from ioremap\_\*
    :type addr: volatile void __iomem \*

.. _`iounmap.description`:

Description
-----------

Caller must ensure there is only one unmapping for the same pointer.

.. This file was automatic generated / don't edit.

