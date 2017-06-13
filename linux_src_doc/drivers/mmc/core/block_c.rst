.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/block.c

.. _`mmc_blk_rw_try_restart`:

mmc_blk_rw_try_restart
======================

.. c:function:: void mmc_blk_rw_try_restart(struct mmc_queue *mq, struct request *req, struct mmc_queue_req *mqrq)

    tries to restart the current async request

    :param struct mmc_queue \*mq:
        the queue with the card and host to restart

    :param struct request \*req:
        a new request that want to be started after the current one

    :param struct mmc_queue_req \*mqrq:
        *undescribed*

.. This file was automatic generated / don't edit.

