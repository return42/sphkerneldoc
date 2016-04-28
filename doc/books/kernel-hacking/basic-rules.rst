.. -*- coding: utf-8; mode: rst -*-

.. _basic-rules:

================
Some Basic Rules
================

No memory protection
    If you corrupt memory, whether in user context or interrupt context,
    the whole machine will crash. Are you sure you can't do what you
    want in userspace?

No floating point or MMX
    The FPU context is not saved; even in user context the FPU state
    probably won't correspond with the current process: you would mess
    with some user process' FPU state. If you really want to do this,
    you would have to explicitly save/restore the full FPU state (and
    avoid context switches). It is generally a bad idea; use fixed point
    arithmetic first.

A rigid stack limit
    Depending on configuration options the kernel stack is about 3K to
    6K for most 32-bit architectures: it's about 14K on most 64-bit
    archs, and often shared with interrupts so you can't use it all.
    Avoid deep recursion and huge local arrays on the stack (allocate
    them dynamically instead).

The Linux kernel is portable
    Let's keep it that way. Your code should be 64-bit clean, and
    endian-independent. You should also minimize CPU specific stuff,
    e.g. inline assembly should be cleanly encapsulated and minimized to
    ease porting. Generally it should be restricted to the
    architecture-dependent part of the kernel tree.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
