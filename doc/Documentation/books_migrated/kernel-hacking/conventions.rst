.. -*- coding: utf-8; mode: rst -*-

.. _conventions:

************************
Routines and Conventions
************************


.. _conventions-doublelinkedlist:

Double-linked lists include/linux/list.h
========================================

There used to be three sets of linked-list routines in the kernel
headers, but this one is the winner. If you don't have some particular
pressing need for a single list, it's a good choice.

In particular, :c:func:`list_for_each_entry()` is useful.


.. _convention-returns:

Return Conventions
==================

For code called in user context, it's very common to defy C convention,
and return 0 for success, and a negative error number (eg. -EFAULT) for
failure. This can be unintuitive at first, but it's fairly widespread in
the kernel.

Using :c:func:`ERR_PTR()` ``include/linux/err.h``; to encode a
negative error number into a pointer, and :c:func:`IS_ERR()` and
:c:func:`PTR_ERR()` to get it back out again: avoids a separate
pointer parameter for the error number. Icky, but in a good way.


.. _conventions-borkedcompile:

Breaking Compilation
====================

Linus and the other developers sometimes change function or structure
names in development kernels; this is not done just to keep everyone on
their toes: it reflects a fundamental change (eg. can no longer be
called with interrupts on, or does extra checks, or doesn't do checks
which were caught before). Usually this is accompanied by a fairly
complete note to the linux-kernel mailing list; search the archive.
Simply doing a global replace on the file usually makes things *worse*.


.. _conventions-initialising:

Initializing structure members
==============================

The preferred method of initializing structures is to use designated
initialisers, as defined by ISO C99, eg:


.. code-block:: c

    static struct block_device_operations opt_fops = {
            .open               = opt_open,
            .release            = opt_release,
            .ioctl              = opt_ioctl,
            .check_media_change = opt_media_change,
    };

This makes it easy to grep for, and makes it clear which structure
fields are set. You should do this because it looks cool.


.. _conventions-gnu-extns:

GNU Extensions
==============

GNU Extensions are explicitly allowed in the Linux kernel. Note that
some of the more complex ones are not very well supported, due to lack
of general use, but the following are considered standard (see the GCC
info page section "C Extensions" for more details - Yes, really the info
page, the man page is only a short summary of the stuff in info).

-  Inline functions

-  Statement expressions (ie. the ({ and }) constructs).

-  Declaring attributes of a function / variable / type
   (__attribute__)

-  typeof

-  Zero length arrays

-  Macro varargs

-  Arithmetic on void pointers

-  Non-Constant initializers

-  Assembler Instructions (not outside arch/ and include/asm/)

-  Function names as strings (__func__).

-  __builtin_constant_p()

Be wary when using long long in the kernel, the code gcc generates for
it is horrible and worse: division and multiplication does not work on
i386 because the GCC runtime functions for it are missing from the
kernel environment.


.. _conventions-cplusplus:

C++
===

Using C++ in the kernel is usually a bad idea, because the kernel does
not provide the necessary runtime environment and the include files are
not tested for it. It is still possible, but not recommended. If you
really want to do this, forget about exceptions at least.


.. _conventions-ifdef:

#if
===

It is generally considered cleaner to use macros in header files (or at
the top of .c files) to abstract away functions rather than using `#if'
pre-processor statements throughout the source code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
