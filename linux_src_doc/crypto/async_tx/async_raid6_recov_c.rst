.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/async_tx/async_raid6_recov.c

.. _`async_raid6_2data_recov`:

async_raid6_2data_recov
=======================

.. c:function:: struct dma_async_tx_descriptor *async_raid6_2data_recov(int disks, size_t bytes, int faila, int failb, struct page **blocks, struct async_submit_ctl *submit)

    asynchronously calculate two missing data blocks

    :param int disks:
        number of disks in the RAID-6 array

    :param size_t bytes:
        block size

    :param int faila:
        first failed drive index

    :param int failb:
        second failed drive index

    :param struct page \*\*blocks:
        array of source pointers where the last two entries are p and q

    :param struct async_submit_ctl \*submit:
        submission/completion modifiers

.. _`async_raid6_datap_recov`:

async_raid6_datap_recov
=======================

.. c:function:: struct dma_async_tx_descriptor *async_raid6_datap_recov(int disks, size_t bytes, int faila, struct page **blocks, struct async_submit_ctl *submit)

    asynchronously calculate a data and the 'p' block

    :param int disks:
        number of disks in the RAID-6 array

    :param size_t bytes:
        block size

    :param int faila:
        failed drive index

    :param struct page \*\*blocks:
        array of source pointers where the last two entries are p and q

    :param struct async_submit_ctl \*submit:
        submission/completion modifiers

.. This file was automatic generated / don't edit.

