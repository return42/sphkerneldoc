.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/mmc_test.c

.. _`mmc_test_pages`:

struct mmc_test_pages
=====================

.. c:type:: struct mmc_test_pages

    pages allocated by 'alloc_pages()'.

.. _`mmc_test_pages.definition`:

Definition
----------

.. code-block:: c

    struct mmc_test_pages {
        struct page *page;
        unsigned int order;
    }

.. _`mmc_test_pages.members`:

Members
-------

page
    first page in the allocation

order
    order of the number of pages allocated

.. _`mmc_test_mem`:

struct mmc_test_mem
===================

.. c:type:: struct mmc_test_mem

    allocated memory.

.. _`mmc_test_mem.definition`:

Definition
----------

.. code-block:: c

    struct mmc_test_mem {
        struct mmc_test_pages *arr;
        unsigned int cnt;
    }

.. _`mmc_test_mem.members`:

Members
-------

arr
    array of allocations

cnt
    number of allocations

.. _`mmc_test_area`:

struct mmc_test_area
====================

.. c:type:: struct mmc_test_area

    information for performance tests.

.. _`mmc_test_area.definition`:

Definition
----------

.. code-block:: c

    struct mmc_test_area {
        unsigned long max_sz;
        unsigned int dev_addr;
        unsigned int max_tfr;
        unsigned int max_segs;
        unsigned int max_seg_sz;
        unsigned int blocks;
        unsigned int sg_len;
        struct mmc_test_mem *mem;
        struct scatterlist *sg;
    }

.. _`mmc_test_area.members`:

Members
-------

max_sz
    test area size (in bytes)

dev_addr
    address on card at which to do performance tests

max_tfr
    maximum transfer size allowed by driver (in bytes)

max_segs
    maximum segments allowed by driver in scatterlist \ ``sg``\ 

max_seg_sz
    maximum segment size allowed by driver

blocks
    number of (512 byte) blocks currently mapped by \ ``sg``\ 

sg_len
    length of currently mapped scatterlist \ ``sg``\ 

mem
    allocated memory

sg
    scatterlist

.. _`mmc_test_transfer_result`:

struct mmc_test_transfer_result
===============================

.. c:type:: struct mmc_test_transfer_result

    transfer results for performance tests.

.. _`mmc_test_transfer_result.definition`:

Definition
----------

.. code-block:: c

    struct mmc_test_transfer_result {
        struct list_head link;
        unsigned int count;
        unsigned int sectors;
        struct timespec64 ts;
        unsigned int rate;
        unsigned int iops;
    }

.. _`mmc_test_transfer_result.members`:

Members
-------

link
    double-linked list

count
    amount of group of sectors to check

sectors
    amount of sectors to check in one group

ts
    time values of transfer

rate
    calculated transfer rate

iops
    I/O operations per second (times 100)

.. _`mmc_test_general_result`:

struct mmc_test_general_result
==============================

.. c:type:: struct mmc_test_general_result

    results for tests.

.. _`mmc_test_general_result.definition`:

Definition
----------

.. code-block:: c

    struct mmc_test_general_result {
        struct list_head link;
        struct mmc_card *card;
        int testcase;
        int result;
        struct list_head tr_lst;
    }

.. _`mmc_test_general_result.members`:

Members
-------

link
    double-linked list

card
    card under test

testcase
    number of test case

result
    result of test run

tr_lst
    transfer measurements if any as mmc_test_transfer_result

.. _`mmc_test_dbgfs_file`:

struct mmc_test_dbgfs_file
==========================

.. c:type:: struct mmc_test_dbgfs_file

    debugfs related file.

.. _`mmc_test_dbgfs_file.definition`:

Definition
----------

.. code-block:: c

    struct mmc_test_dbgfs_file {
        struct list_head link;
        struct mmc_card *card;
        struct dentry *file;
    }

.. _`mmc_test_dbgfs_file.members`:

Members
-------

link
    double-linked list

card
    card under test

file
    file created under debugfs

.. _`mmc_test_card`:

struct mmc_test_card
====================

.. c:type:: struct mmc_test_card

    test information.

.. _`mmc_test_card.definition`:

Definition
----------

.. code-block:: c

    struct mmc_test_card {
        struct mmc_card *card;
        u8 scratch[BUFFER_SIZE];
        u8 *buffer;
    #ifdef CONFIG_HIGHMEM
        struct page *highmem;
    #endif
        struct mmc_test_area area;
        struct mmc_test_general_result *gr;
    }

.. _`mmc_test_card.members`:

Members
-------

card
    card under test

scratch
    transfer buffer

buffer
    transfer buffer

highmem
    buffer for highmem tests

area
    information for performance tests

gr
    pointer to results of current testcase

.. This file was automatic generated / don't edit.

