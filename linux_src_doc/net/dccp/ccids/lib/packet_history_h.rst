.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccids/lib/packet_history.h

.. _`tfrc_rx_hist_index`:

tfrc_rx_hist_index
==================

.. c:function:: u8 tfrc_rx_hist_index(const struct tfrc_rx_hist *h, const u8 n)

    index to reach n-th entry after loss_start

    :param h:
        *undescribed*
    :type h: const struct tfrc_rx_hist \*

    :param n:
        *undescribed*
    :type n: const u8

.. _`tfrc_rx_hist_last_rcv`:

tfrc_rx_hist_last_rcv
=====================

.. c:function:: struct tfrc_rx_hist_entry *tfrc_rx_hist_last_rcv(const struct tfrc_rx_hist *h)

    entry with highest-received-seqno so far

    :param h:
        *undescribed*
    :type h: const struct tfrc_rx_hist \*

.. _`tfrc_rx_hist_entry`:

tfrc_rx_hist_entry
==================

.. c:function:: struct tfrc_rx_hist_entry *tfrc_rx_hist_entry(const struct tfrc_rx_hist *h, const u8 n)

    return the n-th history entry after loss_start

    :param h:
        *undescribed*
    :type h: const struct tfrc_rx_hist \*

    :param n:
        *undescribed*
    :type n: const u8

.. _`tfrc_rx_hist_loss_prev`:

tfrc_rx_hist_loss_prev
======================

.. c:function:: struct tfrc_rx_hist_entry *tfrc_rx_hist_loss_prev(const struct tfrc_rx_hist *h)

    entry with highest-received-seqno before loss was detected

    :param h:
        *undescribed*
    :type h: const struct tfrc_rx_hist \*

.. This file was automatic generated / don't edit.

