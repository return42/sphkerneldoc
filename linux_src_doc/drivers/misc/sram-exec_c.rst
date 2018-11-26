.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/sram-exec.c

.. _`sram_exec_copy`:

sram_exec_copy
==============

.. c:function:: void *sram_exec_copy(struct gen_pool *pool, void *dst, void *src, size_t size)

    copy data to a protected executable region of sram

    :param pool:
        struct gen_pool retrieved that is part of this sram
    :type pool: struct gen_pool \*

    :param dst:
        Destination address for the copy, that must be inside pool
    :type dst: void \*

    :param src:
        Source address for the data to copy
    :type src: void \*

    :param size:
        Size of copy to perform, which starting from dst, must reside in pool
    :type size: size_t

.. _`sram_exec_copy.return`:

Return
------

Address for copied data that can safely be called through function
pointer, or NULL if problem.

This helper function allows sram driver to act as central control location
of 'protect-exec' pools which are normal sram pools but are always set
read-only and executable except when copying data to them, at which point
they are set to read-write non-executable, to make sure no memory is
writeable and executable at the same time. This region must be page-aligned
and is checked during probe, otherwise page attribute manipulation would
not be possible. Care must be taken to only call the returned address as
dst address is not guaranteed to be safely callable.

.. _`sram_exec_copy.note`:

NOTE
----

This function uses the fncpy macro to move code to the executable
region. Some architectures have strict requirements for relocating
executable code, so fncpy is a macro that must be defined by any arch
making use of this functionality that guarantees a safe copy of exec
data and returns a safe address that can be called as a C function
pointer.

.. This file was automatic generated / don't edit.

