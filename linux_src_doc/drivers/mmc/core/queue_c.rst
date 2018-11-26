.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/queue.c

.. _`__mmc_init_request`:

\__mmc_init_request
===================

.. c:function:: int __mmc_init_request(struct mmc_queue *mq, struct request *req, gfp_t gfp)

    initialize the MMC-specific per-request data

    :param mq:
        *undescribed*
    :type mq: struct mmc_queue \*

    :param req:
        the request
    :type req: struct request \*

    :param gfp:
        memory allocation policy
    :type gfp: gfp_t

.. _`mmc_init_queue`:

mmc_init_queue
==============

.. c:function:: int mmc_init_queue(struct mmc_queue *mq, struct mmc_card *card, spinlock_t *lock, const char *subname)

    initialise a queue structure.

    :param mq:
        mmc queue
    :type mq: struct mmc_queue \*

    :param card:
        mmc card to attach this queue
    :type card: struct mmc_card \*

    :param lock:
        queue lock
    :type lock: spinlock_t \*

    :param subname:
        partition subname
    :type subname: const char \*

.. _`mmc_init_queue.description`:

Description
-----------

Initialise a MMC card request queue.

.. This file was automatic generated / don't edit.

