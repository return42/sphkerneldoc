.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/kexec.h

.. _`kexec_buf`:

struct kexec_buf
================

.. c:type:: struct kexec_buf

    parameters for finding a place for a buffer in memory

.. _`kexec_buf.definition`:

Definition
----------

.. code-block:: c

    struct kexec_buf {
        struct kimage *image;
        void *buffer;
        unsigned long bufsz;
        unsigned long mem;
        unsigned long memsz;
        unsigned long buf_align;
        unsigned long buf_min;
        unsigned long buf_max;
        bool top_down;
    }

.. _`kexec_buf.members`:

Members
-------

image
    kexec image in which memory to search.

buffer
    Contents which will be copied to the allocated memory.

bufsz
    Size of \ ``buffer``\ .

mem
    On return will have address of the buffer in memory.

memsz
    Size for the buffer in memory.

buf_align
    Minimum alignment needed.

buf_min
    The buffer can't be placed below this address.

buf_max
    The buffer can't be placed above this address.

top_down
    Allocate from top of memory.

.. This file was automatic generated / don't edit.

