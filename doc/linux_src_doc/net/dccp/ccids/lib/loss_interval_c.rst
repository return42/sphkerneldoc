.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccids/lib/loss_interval.c

.. _`tfrc_lh_update_i_mean`:

tfrc_lh_update_i_mean
=====================

.. c:function:: u8 tfrc_lh_update_i_mean(struct tfrc_loss_hist *lh, struct sk_buff *skb)

    Update the \`open' loss interval I_0

    :param struct tfrc_loss_hist \*lh:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`tfrc_lh_update_i_mean.for-recomputing-p`:

For recomputing p
-----------------

returns \`true' if p > p_prev  <=>  1/p < 1/p_prev

.. _`tfrc_lh_interval_add`:

tfrc_lh_interval_add
====================

.. c:function:: int tfrc_lh_interval_add(struct tfrc_loss_hist *lh, struct tfrc_rx_hist *rh, u32 (*calc_first_li)(struct sock *), struct sock *sk)

    Insert new record into the Loss Interval database

    :param struct tfrc_loss_hist \*lh:
        Loss Interval database

    :param struct tfrc_rx_hist \*rh:
        Receive history containing a fresh loss event

    :param u32 (\*calc_first_li)(struct sock \*):
        Caller-dependent routine to compute length of first interval

    :param struct sock \*sk:
        Used by \ ``calc_first_li``\  in caller-specific way (subtyping)

.. _`tfrc_lh_interval_add.description`:

Description
-----------

Updates I_mean and returns 1 if a new interval has in fact been added to \ ``lh``\ .

.. This file was automatic generated / don't edit.

