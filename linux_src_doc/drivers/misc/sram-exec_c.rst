.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/sram-exec.c

.. _`sram_exec_copy`:

sram_exec_copy
==============

.. c:function:: int sram_exec_copy(struct gen_pool *pool, void *dst, void *src, size_t size)

    copy data to a protected executable region of sram

    :param struct gen_pool \*pool:
        struct gen_pool retrieved that is part of this sram

    :param void \*dst:
        Destination address for the copy, that must be inside pool

    :param void \*src:
        Source address for the data to copy

    :param size_t size:
        Size of copy to perform, which starting from dst, must reside in pool

.. _`sram_exec_copy.description`:

Description
-----------

This helper function allows sram driver to act as central control location
of 'protect-exec' pools which are normal sram pools but are always set
read-only and executable except when copying data to them, at which point
they are set to read-write non-executable, to make sure no memory is
writeable and executable at the same time. This region must be page-aligned
and is checked during probe, otherwise page attribute manipulation would
not be possible.

.. This file was automatic generated / don't edit.

