.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mailbox_client.h

.. _`mbox_client`:

struct mbox_client
==================

.. c:type:: struct mbox_client

    User of a mailbox

.. _`mbox_client.definition`:

Definition
----------

.. code-block:: c

    struct mbox_client {
        struct device *dev;
        bool tx_block;
        unsigned long tx_tout;
        bool knows_txdone;
        void (* rx_callback) (struct mbox_client *cl, void *mssg);
        void (* tx_prepare) (struct mbox_client *cl, void *mssg);
        void (* tx_done) (struct mbox_client *cl, void *mssg, int r);
    }

.. _`mbox_client.members`:

Members
-------

dev
    The client device

tx_block
    If the mbox_send_message should block until data is
    transmitted.

tx_tout
    Max block period in ms before TX is assumed failure

knows_txdone
    If the client could run the TX state machine. Usually
    if the client receives some ACK packet for transmission.
    Unused if the controller already has TX_Done/RTR IRQ.

rx_callback
    Atomic callback to provide client the data received

tx_prepare
    Atomic callback to ask client to prepare the payload
    before initiating the transmission if required.

tx_done
    Atomic callback to tell client of data transmission

.. This file was automatic generated / don't edit.

