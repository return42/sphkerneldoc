.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/smc/smc_llc.c

.. _`smc_llc_add_pending_send`:

smc_llc_add_pending_send
========================

.. c:function:: int smc_llc_add_pending_send(struct smc_link *link, struct smc_wr_buf **wr_buf, struct smc_wr_tx_pend_priv **pend)

    add LLC control message to pending WQE transmits

    :param struct smc_link \*link:
        Pointer to SMC link used for sending LLC control message.

    :param struct smc_wr_buf \*\*wr_buf:
        Out variable returning pointer to work request payload buffer.

    :param struct smc_wr_tx_pend_priv \*\*pend:
        Out variable returning pointer to private pending WR tracking.
        It's the context the transmit complete handler will get.

.. _`smc_llc_add_pending_send.description`:

Description
-----------

Reserves and pre-fills an entry for a pending work request send/tx.
Used by mid-level \ :c:func:`smc_llc_send_msg`\  to prepare for later actual send/tx.
Can sleep due to smc_get_ctrl_buf (if not in softirq context).

.. _`smc_llc_add_pending_send.return`:

Return
------

0 on success, otherwise an error value.

.. This file was automatic generated / don't edit.

