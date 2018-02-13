.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/queue.c

.. _`__mmc_init_request`:

\__mmc_init_request
===================

.. c:function:: int __mmc_init_request(struct mmc_queue *mq, struct request *req, gfp_t gfp)

    initialize the MMC-specific per-request data

    :param struct mmc_queue \*mq:
        *undescribed*

    :param struct request \*req:
        the request

    :param gfp_t gfp:
        memory allocation policy

.. _`mmc_init_queue`:

mmc_init_queue
==============

.. c:function:: int mmc_init_queue(struct mmc_queue *mq, struct mmc_card *card, spinlock_t *lock, const char *subname)

    initialise a queue structure.

    :param struct mmc_queue \*mq:
        mmc queue

    :param struct mmc_card \*card:
        mmc card to attach this queue

    :param spinlock_t \*lock:
        queue lock

    :param const char \*subname:
        partition subname

.. _`mmc_init_queue.description`:

Description
-----------

Initialise a MMC card request queue.

.. This file was automatic generated / don't edit.

