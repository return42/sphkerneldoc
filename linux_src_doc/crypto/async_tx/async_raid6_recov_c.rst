.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/async_tx/async_raid6_recov.c

.. _`async_raid6_2data_recov`:

async_raid6_2data_recov
=======================

.. c:function:: struct dma_async_tx_descriptor *async_raid6_2data_recov(int disks, size_t bytes, int faila, int failb, struct page **blocks, struct async_submit_ctl *submit)

    asynchronously calculate two missing data blocks

    :param disks:
        number of disks in the RAID-6 array
    :type disks: int

    :param bytes:
        block size
    :type bytes: size_t

    :param faila:
        first failed drive index
    :type faila: int

    :param failb:
        second failed drive index
    :type failb: int

    :param blocks:
        array of source pointers where the last two entries are p and q
    :type blocks: struct page \*\*

    :param submit:
        submission/completion modifiers
    :type submit: struct async_submit_ctl \*

.. _`async_raid6_datap_recov`:

async_raid6_datap_recov
=======================

.. c:function:: struct dma_async_tx_descriptor *async_raid6_datap_recov(int disks, size_t bytes, int faila, struct page **blocks, struct async_submit_ctl *submit)

    asynchronously calculate a data and the 'p' block

    :param disks:
        number of disks in the RAID-6 array
    :type disks: int

    :param bytes:
        block size
    :type bytes: size_t

    :param faila:
        failed drive index
    :type faila: int

    :param blocks:
        array of source pointers where the last two entries are p and q
    :type blocks: struct page \*\*

    :param submit:
        submission/completion modifiers
    :type submit: struct async_submit_ctl \*

.. This file was automatic generated / don't edit.

