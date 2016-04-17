
.. _kernel-lib:

==============================
Basic Kernel Library Functions
==============================

The Linux kernel provides more basic utility functions.


Bitmap Operations
=================


.. toctree::
    :maxdepth: 1

    API---bitmap-shift-right
    API---bitmap-shift-left
    API-bitmap-find-next-zero-area-off
    API---bitmap-parse
    API-bitmap-parse-user
    API-bitmap-print-to-pagebuf
    API-bitmap-parselist-user
    API-bitmap-remap
    API-bitmap-bitremap
    API-bitmap-onto
    API-bitmap-fold
    API-bitmap-find-free-region
    API-bitmap-release-region
    API-bitmap-allocate-region
    API-bitmap-from-u32array
    API-bitmap-to-u32array
    API-bitmap-copy-le
    API---bitmap-parselist
    API-bitmap-pos-to-ord
    API-bitmap-ord-to-pos

Command-line Parsing
====================


.. toctree::
    :maxdepth: 1

    API-get-option
    API-get-options
    API-memparse

.. _crc:

CRC Functions
=============


.. toctree::
    :maxdepth: 1

    API-crc7-be
    API-crc16
    API-crc-itu-t
    kernel-lib-000-004-008
    API-crc-ccitt

.. _idr:

idr/ida Functions
=================

idr synchronization (stolen from radix-tree.h)

``idr_find`` is able to be called locklessly, using RCU. The caller must ensure calls to this function are made within ``rcu_read_lock`` regions. Other readers (lock-free or
otherwise) and modifications may be running concurrently.

It is still required that the caller manage the synchronization and lifetimes of the items. So if RCU lock-free lookups are used, typically this would mean that the items have
their own locks, or are amenable to lock-free access; and that the items are freed by RCU (or only freed after having been deleted from the idr tree ⋆and⋆ a ``synchronize_rcu``
grace period).

IDA - IDR based ID allocator

This is id allocator without id -> pointer translation. Memory usage is much lower than full blown idr because each id only occupies a bit. ida uses a custom leaf node which
contains IDA_BITMAP_BITS slots.

2007-04-25 written by Tejun Heo <htejun``gmail``.com>


.. toctree::
    :maxdepth: 1

    API-idr-preload
    API-idr-alloc
    API-idr-alloc-cyclic
    API-idr-remove
    API-idr-destroy
    API-idr-for-each
    API-idr-get-next
    API-idr-replace
    API-idr-init
    API-ida-pre-get
    API-ida-get-new-above
    API-ida-remove
    API-ida-destroy
    API-ida-simple-get
    API-ida-simple-remove
    API-ida-init
