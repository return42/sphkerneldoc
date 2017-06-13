.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/dynack.h

.. _`ath_dyn_rxbuf`:

struct ath_dyn_rxbuf
====================

.. c:type:: struct ath_dyn_rxbuf

    ACK frame ring buffer

.. _`ath_dyn_rxbuf.definition`:

Definition
----------

.. code-block:: c

    struct ath_dyn_rxbuf {
        u16 h_rb;
        u16 t_rb;
        u32 tstamp;
    }

.. _`ath_dyn_rxbuf.members`:

Members
-------

h_rb
    ring buffer head

t_rb
    ring buffer tail

tstamp
    ACK RX timestamp buffer

.. _`ath_dyn_txbuf`:

struct ath_dyn_txbuf
====================

.. c:type:: struct ath_dyn_txbuf

    tx frame ring buffer

.. _`ath_dyn_txbuf.definition`:

Definition
----------

.. code-block:: c

    struct ath_dyn_txbuf {
        u16 h_rb;
        u16 t_rb;
        struct haddr_pair addr;
        struct ts_info ts;
    }

.. _`ath_dyn_txbuf.members`:

Members
-------

h_rb
    ring buffer head

t_rb
    ring buffer tail

addr
    dest/src address pair for a given TX frame

ts
    TX frame timestamp buffer

.. _`ath_dynack`:

struct ath_dynack
=================

.. c:type:: struct ath_dynack

    dynack processing info

.. _`ath_dynack.definition`:

Definition
----------

.. code-block:: c

    struct ath_dynack {
        bool enabled;
        int ackto;
        unsigned long lto;
        struct list_head nodes;
        spinlock_t qlock;
        struct ath_dyn_rxbuf ack_rbf;
        struct ath_dyn_txbuf st_rbf;
    }

.. _`ath_dynack.members`:

Members
-------

enabled
    enable dyn ack processing

ackto
    current ACK timeout

lto
    last ACK timeout computation

nodes
    ath_node linked list

qlock
    ts queue spinlock

ack_rbf
    ACK ts ring buffer

st_rbf
    status ts ring buffer

.. This file was automatic generated / don't edit.

