.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/smc/smc_wr.c

.. _`smc_wr_tx_get_free_slot`:

smc_wr_tx_get_free_slot
=======================

.. c:function:: int smc_wr_tx_get_free_slot(struct smc_link *link, smc_wr_tx_handler handler, struct smc_wr_buf **wr_buf, struct smc_wr_tx_pend_priv **wr_pend_priv)

    returns buffer for message assembly, and sets info for pending transmit tracking

    :param link:
        Pointer to smc_link used to later send the message.
    :type link: struct smc_link \*

    :param handler:
        Send completion handler function pointer.
    :type handler: smc_wr_tx_handler

    :param wr_buf:
        Out value returns pointer to message buffer.
    :type wr_buf: struct smc_wr_buf \*\*

    :param wr_pend_priv:
        Out value returns pointer serving as handler context.
    :type wr_pend_priv: struct smc_wr_tx_pend_priv \*\*

.. _`smc_wr_tx_get_free_slot.return`:

Return
------

0 on success, or -errno on error.

.. This file was automatic generated / don't edit.

