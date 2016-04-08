
.. _API-struct-tid-ampdu-tx:

===================
struct tid_ampdu_tx
===================

*man struct tid_ampdu_tx(9)*

*4.6.0-rc1*

TID aggregation information (Tx).


Synopsis
========

.. code-block:: c

    struct tid_ampdu_tx {
      struct rcu_head rcu_head;
      struct timer_list session_timer;
      struct timer_list addba_resp_timer;
      struct sk_buff_head pending;
      unsigned long state;
      unsigned long last_tx;
      u16 timeout;
      u8 dialog_token;
      u8 stop_initiator;
      bool tx_stop;
      u8 buf_size;
      u16 failed_bar_ssn;
      bool bar_pending;
      bool amsdu;
    };


Members
=======

rcu_head
    rcu head for freeing structure

session_timer
    check if we keep Tx-ing on the TID (by timeout value)

addba_resp_timer
    timer for peer's response to addba request

pending
    pending frames queue -- use sta's spinlock to protect

state
    session state (see above)

last_tx
    jiffies of last tx activity

timeout
    session timeout value to be filled in ADDBA requests

dialog_token
    dialog token for aggregation session

stop_initiator
    initiator of a session stop

tx_stop
    TX DelBA frame when stopping

buf_size
    reorder buffer size at receiver

failed_bar_ssn
    ssn of the last failed BAR tx attempt

bar_pending
    BAR needs to be re-sent

amsdu
    support A-MSDU withing A-MDPU


Description
===========

This structure's lifetime is managed by RCU, assignments to the array holding it must hold the aggregation mutex.

The TX path can access it under RCU lock-free if, and only if, the state has the flag ``HT_AGG_STATE_OPERATIONAL`` set. Otherwise, the TX path must also acquire the spinlock and
re-check the state, see comments in the tx code touching it.
