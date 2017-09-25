.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mailbox_controller.h

.. _`mbox_chan_ops`:

struct mbox_chan_ops
====================

.. c:type:: struct mbox_chan_ops

    methods to control mailbox channels

.. _`mbox_chan_ops.definition`:

Definition
----------

.. code-block:: c

    struct mbox_chan_ops {
        int (*send_data)(struct mbox_chan *chan, void *data);
        int (*startup)(struct mbox_chan *chan);
        void (*shutdown)(struct mbox_chan *chan);
        bool (*last_tx_done)(struct mbox_chan *chan);
        bool (*peek_data)(struct mbox_chan *chan);
    }

.. _`mbox_chan_ops.members`:

Members
-------

send_data
    The API asks the MBOX controller driver, in atomic
    context try to transmit a message on the bus. Returns 0 if
    data is accepted for transmission, -EBUSY while rejecting
    if the remote hasn't yet read the last data sent. Actual
    transmission of data is reported by the controller via
    mbox_chan_txdone (if it has some TX ACK irq). It must not
    sleep.

startup
    Called when a client requests the chan. The controller
    could ask clients for additional parameters of communication
    to be provided via client's chan_data. This call may
    block. After this call the Controller must forward any
    data received on the chan by calling mbox_chan_received_data.
    The controller may do stuff that need to sleep.

shutdown
    Called when a client relinquishes control of a chan.
    This call may block too. The controller must not forward
    any received data anymore.
    The controller may do stuff that need to sleep.

last_tx_done
    If the controller sets 'txdone_poll', the API calls
    this to poll status of last TX. The controller must
    give priority to IRQ method over polling and never
    set both txdone_poll and txdone_irq. Only in polling
    mode 'send_data' is expected to return -EBUSY.
    The controller may do stuff that need to sleep/block.
    Used only if txdone_poll:=true && txdone_irq:=false

peek_data
    Atomic check for any received data. Return true if controller
    has some data to push to the client. False otherwise.

.. _`mbox_controller`:

struct mbox_controller
======================

.. c:type:: struct mbox_controller

    Controller of a class of communication channels

.. _`mbox_controller.definition`:

Definition
----------

.. code-block:: c

    struct mbox_controller {
        struct device *dev;
        const struct mbox_chan_ops *ops;
        struct mbox_chan *chans;
        int num_chans;
        bool txdone_irq;
        bool txdone_poll;
        unsigned txpoll_period;
        struct mbox_chan *(*of_xlate)(struct mbox_controller *mbox, const struct of_phandle_args *sp);
        struct hrtimer poll_hrt;
        struct list_head node;
    }

.. _`mbox_controller.members`:

Members
-------

dev
    Device backing this controller

ops
    Operators that work on each communication chan

chans
    Array of channels

num_chans
    Number of channels in the 'chans' array.

txdone_irq
    Indicates if the controller can report to API when
    the last transmitted data was read by the remote.
    Eg, if it has some TX ACK irq.

txdone_poll
    If the controller can read but not report the TX
    done. Ex, some register shows the TX status but
    no interrupt rises. Ignored if 'txdone_irq' is set.

txpoll_period
    If 'txdone_poll' is in effect, the API polls for
    last TX's status after these many millisecs

of_xlate
    Controller driver specific mapping of channel via DT

poll_hrt
    API private. hrtimer used to poll for TXDONE on all
    channels.

node
    API private. To hook into list of controllers.

.. _`mbox_chan`:

struct mbox_chan
================

.. c:type:: struct mbox_chan

    s/w representation of a communication chan

.. _`mbox_chan.definition`:

Definition
----------

.. code-block:: c

    struct mbox_chan {
        struct mbox_controller *mbox;
        unsigned txdone_method;
        struct mbox_client *cl;
        struct completion tx_complete;
        void *active_req;
        unsigned msg_count, msg_free;
        void *msg_data[MBOX_TX_QUEUE_LEN];
        spinlock_t lock;
        void *con_priv;
    }

.. _`mbox_chan.members`:

Members
-------

mbox
    Pointer to the parent/provider of this channel

txdone_method
    Way to detect TXDone chosen by the API

cl
    Pointer to the current owner of this channel

tx_complete
    Transmission completion

active_req
    Currently active request hook

msg_count
    No. of mssg currently queued

msg_free
    Index of next available mssg slot

msg_data
    Hook for data packet

lock
    Serialise access to the channel

con_priv
    Hook for controller driver to attach private data

.. This file was automatic generated / don't edit.

