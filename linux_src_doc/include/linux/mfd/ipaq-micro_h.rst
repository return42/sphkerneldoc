.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/ipaq-micro.h

.. _`ipaq_micro_txdev`:

struct ipaq_micro_txdev
=======================

.. c:type:: struct ipaq_micro_txdev

    TX state

.. _`ipaq_micro_txdev.definition`:

Definition
----------

.. code-block:: c

    struct ipaq_micro_txdev {
        u8 len;
        u8 index;
        u8 buf;
    }

.. _`ipaq_micro_txdev.members`:

Members
-------

len
    length of message in TX buffer

index
    current index into TX buffer

buf
    TX buffer

.. _`ipaq_micro_rxdev`:

struct ipaq_micro_rxdev
=======================

.. c:type:: struct ipaq_micro_rxdev

    RX state

.. _`ipaq_micro_rxdev.definition`:

Definition
----------

.. code-block:: c

    struct ipaq_micro_rxdev {
        enum rx_state state;
        unsigned char chksum;
        u8 id;
        unsigned int len;
        unsigned int index;
        u8 buf;
    }

.. _`ipaq_micro_rxdev.members`:

Members
-------

state
    context of RX state machine

chksum
    calculated checksum

id
    message ID from packet

len
    RX buffer length

index
    RX buffer index

buf
    RX buffer

.. _`ipaq_micro_msg`:

struct ipaq_micro_msg
=====================

.. c:type:: struct ipaq_micro_msg

    message to the iPAQ microcontroller

.. _`ipaq_micro_msg.definition`:

Definition
----------

.. code-block:: c

    struct ipaq_micro_msg {
        u8 id;
        u8 tx_len;
        u8 tx_data;
        u8 rx_len;
        u8 rx_data;
        struct completion ack;
        struct list_head node;
    }

.. _`ipaq_micro_msg.members`:

Members
-------

id
    4-bit ID of the message

tx_len
    length of TX data

tx_data
    TX data to send

rx_len
    length of receieved RX data

rx_data
    RX data to recieve

ack
    a completion that will be completed when RX is complete

node
    list node if message gets queued

.. _`ipaq_micro`:

struct ipaq_micro
=================

.. c:type:: struct ipaq_micro

    iPAQ microcontroller state

.. _`ipaq_micro.definition`:

Definition
----------

.. code-block:: c

    struct ipaq_micro {
        struct device *dev;
        void __iomem *base;
        void __iomem *sdlc;
        char version;
        struct ipaq_micro_txdev tx;
        struct ipaq_micro_rxdev rx;
        spinlock_t lock;
        struct ipaq_micro_msg *msg;
        struct list_head queue;
        void (*key)(void *data, int len, unsigned char *rxdata);
        void *key_data;
        void (*ts)(void *data, int len, unsigned char *rxdata);
        void *ts_data;
    }

.. _`ipaq_micro.members`:

Members
-------

dev
    corresponding platform device

base
    virtual memory base for underlying serial device

sdlc
    virtual memory base for Synchronous Data Link Controller

version
    version string

tx
    TX state

rx
    RX state

lock
    lock for this state container

msg
    current message

queue
    message queue

key
    callback for asynchronous key events

key_data
    data to pass along with key events

ts
    callback for asynchronous touchscreen events

ts_data
    data to pass along with key events

.. This file was automatic generated / don't edit.

