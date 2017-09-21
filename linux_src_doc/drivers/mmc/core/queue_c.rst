.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/queue.c

.. _`mmc_init_request`:

mmc_init_request
================

.. c:function:: int mmc_init_request(struct request_queue *q, struct request *req, gfp_t gfp)

    initialize the MMC-specific per-request data

    :param struct request_queue \*q:
        the request queue

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

.. _`mmc_queue_suspend`:

mmc_queue_suspend
=================

.. c:function:: void mmc_queue_suspend(struct mmc_queue *mq)

    suspend a MMC request queue

    :param struct mmc_queue \*mq:
        MMC queue to suspend

.. _`mmc_queue_suspend.description`:

Description
-----------

Stop the block request queue, and wait for our thread to
complete any outstanding requests.  This ensures that we
won't suspend while a request is being processed.

.. _`mmc_queue_resume`:

mmc_queue_resume
================

.. c:function:: void mmc_queue_resume(struct mmc_queue *mq)

    resume a previously suspended MMC request queue

    :param struct mmc_queue \*mq:
        MMC queue to resume

.. This file was automatic generated / don't edit.

