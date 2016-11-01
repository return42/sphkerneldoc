.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hsi/clients/ssi_protocol.c

.. _`ssi_protocol`:

struct ssi_protocol
===================

.. c:type:: struct ssi_protocol

    SSI protocol (McSAAB) data

.. _`ssi_protocol.definition`:

Definition
----------

.. code-block:: c

    struct ssi_protocol {
        unsigned int main_state;
        unsigned int send_state;
        unsigned int recv_state;
        unsigned long flags;
        u8 rxid;
        u8 txid;
        unsigned int txqueue_len;
        struct timer_list tx_wd;
        struct timer_list rx_wd;
        struct timer_list keep_alive;
        spinlock_t lock;
        struct net_device *netdev;
        struct list_head txqueue;
        struct list_head cmdqueue;
        struct work_struct work;
        struct hsi_client *cl;
        struct list_head link;
        atomic_t tx_usecnt;
        int channel_id_cmd;
        int channel_id_data;
    }

.. _`ssi_protocol.members`:

Members
-------

main_state
    Main state machine

send_state
    TX state machine

recv_state
    RX state machine

flags
    Flags, currently only used to follow wake line test

rxid
    RX data id

txid
    TX data id

txqueue_len
    TX queue length

tx_wd
    TX watchdog

rx_wd
    RX watchdog

keep_alive
    Workaround for SSI HW bug

lock
    To serialize access to this struct

netdev
    Phonet network device

txqueue
    TX data queue

cmdqueue
    Queue of free commands

work
    *undescribed*

cl
    HSI client own reference

link
    Link for ssip_list

tx_usecnt
    *undescribed*

channel_id_cmd
    HSI channel id for command stream

channel_id_data
    HSI channel id for data stream

.. This file was automatic generated / don't edit.

