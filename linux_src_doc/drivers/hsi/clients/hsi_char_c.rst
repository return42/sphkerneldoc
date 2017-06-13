.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hsi/clients/hsi_char.c

.. _`hsc_channel`:

struct hsc_channel
==================

.. c:type:: struct hsc_channel

    hsi_char internal channel data

.. _`hsc_channel.definition`:

Definition
----------

.. code-block:: c

    struct hsc_channel {
        unsigned int ch;
        unsigned long flags;
        struct list_head free_msgs_list;
        struct list_head rx_msgs_queue;
        struct list_head tx_msgs_queue;
        spinlock_t lock;
        struct hsi_client *cl;
        struct hsc_client_data *cl_data;
        wait_queue_head_t rx_wait;
        wait_queue_head_t tx_wait;
    }

.. _`hsc_channel.members`:

Members
-------

ch
    channel number

flags
    Keeps state of the channel (open/close, reading, writing)

free_msgs_list
    List of free HSI messages/requests

rx_msgs_queue
    List of pending RX requests

tx_msgs_queue
    List of pending TX requests

lock
    Serialize access to the lists

cl
    reference to the associated hsi_client

cl_data
    reference to the client data that this channels belongs to

rx_wait
    RX requests wait queue

tx_wait
    TX requests wait queue

.. _`hsc_client_data`:

struct hsc_client_data
======================

.. c:type:: struct hsc_client_data

    hsi_char internal client data

.. _`hsc_client_data.definition`:

Definition
----------

.. code-block:: c

    struct hsc_client_data {
        struct cdev cdev;
        struct mutex lock;
        unsigned long flags;
        unsigned int usecnt;
        struct hsi_client *cl;
        struct hsc_channel channels;
    }

.. _`hsc_client_data.members`:

Members
-------

cdev
    Characther device associated to the hsi_client

lock
    Lock to serialize open/close access

flags
    Keeps track of port state (rx hwbreak armed)

usecnt
    Use count for claiming the HSI port (mutex protected)

cl
    Referece to the HSI client

channels
    Array of channels accessible by the client

.. This file was automatic generated / don't edit.

