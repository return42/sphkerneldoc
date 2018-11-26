.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mailbox/ti-msgmgr.c

.. _`ti_msgmgr_valid_queue_desc`:

struct ti_msgmgr_valid_queue_desc
=================================

.. c:type:: struct ti_msgmgr_valid_queue_desc

    SoC valid queues meant for this processor

.. _`ti_msgmgr_valid_queue_desc.definition`:

Definition
----------

.. code-block:: c

    struct ti_msgmgr_valid_queue_desc {
        u8 queue_id;
        u8 proxy_id;
        bool is_tx;
    }

.. _`ti_msgmgr_valid_queue_desc.members`:

Members
-------

queue_id
    Queue Number for this path

proxy_id
    Proxy ID representing the processor in SoC

is_tx
    Is this a receive path?

.. _`ti_msgmgr_desc`:

struct ti_msgmgr_desc
=====================

.. c:type:: struct ti_msgmgr_desc

    Description of message manager integration

.. _`ti_msgmgr_desc.definition`:

Definition
----------

.. code-block:: c

    struct ti_msgmgr_desc {
        u8 queue_count;
        u8 max_message_size;
        u8 max_messages;
        u8 data_first_reg;
        u8 data_last_reg;
        u32 status_cnt_mask;
        u32 status_err_mask;
        bool tx_polled;
        int tx_poll_timeout_ms;
        const struct ti_msgmgr_valid_queue_desc *valid_queues;
        const char *data_region_name;
        const char *status_region_name;
        const char *ctrl_region_name;
        int num_valid_queues;
        bool is_sproxy;
    }

.. _`ti_msgmgr_desc.members`:

Members
-------

queue_count
    Number of Queues

max_message_size
    Message size in bytes

max_messages
    Number of messages

data_first_reg
    First data register for proxy data region

data_last_reg
    Last data register for proxy data region

status_cnt_mask
    Mask for getting the status value

status_err_mask
    Mask for getting the error value, if applicable

tx_polled
    Do I need to use polled mechanism for tx

tx_poll_timeout_ms
    Timeout in ms if polled

valid_queues
    List of Valid queues that the processor can access

data_region_name
    Name of the proxy data region

status_region_name
    Name of the proxy status region

ctrl_region_name
    Name of the proxy control region

num_valid_queues
    Number of valid queues

is_sproxy
    Is this an Secure Proxy instance?

.. _`ti_msgmgr_desc.description`:

Description
-----------

This structure is used in of match data to describe how integration
for a specific compatible SoC is done.

.. _`ti_queue_inst`:

struct ti_queue_inst
====================

.. c:type:: struct ti_queue_inst

    Description of a queue instance

.. _`ti_queue_inst.definition`:

Definition
----------

.. code-block:: c

    struct ti_queue_inst {
        char name[30];
        u8 queue_id;
        u8 proxy_id;
        int irq;
        bool is_tx;
        void __iomem *queue_buff_start;
        void __iomem *queue_buff_end;
        void __iomem *queue_state;
        void __iomem *queue_ctrl;
        struct mbox_chan *chan;
        u32 *rx_buff;
    }

.. _`ti_queue_inst.members`:

Members
-------

name
    Queue Name

queue_id
    Queue Identifier as mapped on SoC

proxy_id
    Proxy Identifier as mapped on SoC

irq
    IRQ for Rx Queue

is_tx
    'true' if transmit queue, else, 'false'

queue_buff_start
    First register of Data Buffer

queue_buff_end
    Last (or confirmation) register of Data buffer

queue_state
    Queue status register

queue_ctrl
    Queue Control register

chan
    Mailbox channel

rx_buff
    Receive buffer pointer allocated at probe, max_message_size

.. _`ti_msgmgr_inst`:

struct ti_msgmgr_inst
=====================

.. c:type:: struct ti_msgmgr_inst

    Description of a Message Manager Instance

.. _`ti_msgmgr_inst.definition`:

Definition
----------

.. code-block:: c

    struct ti_msgmgr_inst {
        struct device *dev;
        const struct ti_msgmgr_desc *desc;
        void __iomem *queue_proxy_region;
        void __iomem *queue_state_debug_region;
        void __iomem *queue_ctrl_region;
        u8 num_valid_queues;
        struct ti_queue_inst *qinsts;
        struct mbox_controller mbox;
        struct mbox_chan *chans;
    }

.. _`ti_msgmgr_inst.members`:

Members
-------

dev
    device pointer corresponding to the Message Manager instance

desc
    Description of the SoC integration

queue_proxy_region
    Queue proxy region where queue buffers are located

queue_state_debug_region
    Queue status register regions

queue_ctrl_region
    Queue Control register regions

num_valid_queues
    Number of valid queues defined for the processor
    Note: other queues are probably reserved for other processors
    in the SoC.

qinsts
    Array of valid Queue Instances for the Processor

mbox
    Mailbox Controller

chans
    Array for channels corresponding to the Queue Instances.

.. _`ti_msgmgr_queue_get_num_messages`:

ti_msgmgr_queue_get_num_messages
================================

.. c:function:: int ti_msgmgr_queue_get_num_messages(const struct ti_msgmgr_desc *d, struct ti_queue_inst *qinst)

    Get the number of pending messages

    :param d:
        Description of message manager
    :type d: const struct ti_msgmgr_desc \*

    :param qinst:
        Queue instance for which we check the number of pending messages
    :type qinst: struct ti_queue_inst \*

.. _`ti_msgmgr_queue_get_num_messages.return`:

Return
------

number of messages pending in the queue (0 == no pending messages)

.. _`ti_msgmgr_queue_is_error`:

ti_msgmgr_queue_is_error
========================

.. c:function:: bool ti_msgmgr_queue_is_error(const struct ti_msgmgr_desc *d, struct ti_queue_inst *qinst)

    Check to see if there is queue error

    :param d:
        Description of message manager
    :type d: const struct ti_msgmgr_desc \*

    :param qinst:
        Queue instance for which we check the number of pending messages
    :type qinst: struct ti_queue_inst \*

.. _`ti_msgmgr_queue_is_error.return`:

Return
------

true if error, else false

.. _`ti_msgmgr_queue_rx_interrupt`:

ti_msgmgr_queue_rx_interrupt
============================

.. c:function:: irqreturn_t ti_msgmgr_queue_rx_interrupt(int irq, void *p)

    Interrupt handler for receive Queue

    :param irq:
        Interrupt number
    :type irq: int

    :param p:
        Channel Pointer
    :type p: void \*

.. _`ti_msgmgr_queue_rx_interrupt.return`:

Return
------

-EINVAL if there is no instance
IRQ_NONE if the interrupt is not ours.
IRQ_HANDLED if the rx interrupt was successfully handled.

.. _`ti_msgmgr_queue_peek_data`:

ti_msgmgr_queue_peek_data
=========================

.. c:function:: bool ti_msgmgr_queue_peek_data(struct mbox_chan *chan)

    Peek to see if there are any rx messages.

    :param chan:
        Channel Pointer
    :type chan: struct mbox_chan \*

.. _`ti_msgmgr_queue_peek_data.return`:

Return
------

'true' if there is pending rx data, 'false' if there is none.

.. _`ti_msgmgr_last_tx_done`:

ti_msgmgr_last_tx_done
======================

.. c:function:: bool ti_msgmgr_last_tx_done(struct mbox_chan *chan)

    See if all the tx messages are sent

    :param chan:
        Channel pointer
    :type chan: struct mbox_chan \*

.. _`ti_msgmgr_last_tx_done.return`:

Return
------

'true' is no pending tx data, 'false' if there are any.

.. _`ti_msgmgr_send_data`:

ti_msgmgr_send_data
===================

.. c:function:: int ti_msgmgr_send_data(struct mbox_chan *chan, void *data)

    Send data

    :param chan:
        Channel Pointer
    :type chan: struct mbox_chan \*

    :param data:
        ti_msgmgr_message \* Message Pointer
    :type data: void \*

.. _`ti_msgmgr_send_data.return`:

Return
------

0 if all goes good, else appropriate error messages.

.. _`ti_msgmgr_queue_rx_irq_req`:

ti_msgmgr_queue_rx_irq_req
==========================

.. c:function:: int ti_msgmgr_queue_rx_irq_req(struct device *dev, const struct ti_msgmgr_desc *d, struct ti_queue_inst *qinst, struct mbox_chan *chan)

    RX IRQ request

    :param dev:
        device pointer
    :type dev: struct device \*

    :param d:
        descriptor for ti_msgmgr
    :type d: const struct ti_msgmgr_desc \*

    :param qinst:
        Queue instance
    :type qinst: struct ti_queue_inst \*

    :param chan:
        Channel pointer
    :type chan: struct mbox_chan \*

.. _`ti_msgmgr_queue_startup`:

ti_msgmgr_queue_startup
=======================

.. c:function:: int ti_msgmgr_queue_startup(struct mbox_chan *chan)

    Startup queue

    :param chan:
        Channel pointer
    :type chan: struct mbox_chan \*

.. _`ti_msgmgr_queue_startup.return`:

Return
------

0 if all goes good, else return corresponding error message

.. _`ti_msgmgr_queue_shutdown`:

ti_msgmgr_queue_shutdown
========================

.. c:function:: void ti_msgmgr_queue_shutdown(struct mbox_chan *chan)

    Shutdown the queue

    :param chan:
        Channel pointer
    :type chan: struct mbox_chan \*

.. _`ti_msgmgr_of_xlate`:

ti_msgmgr_of_xlate
==================

.. c:function:: struct mbox_chan *ti_msgmgr_of_xlate(struct mbox_controller *mbox, const struct of_phandle_args *p)

    Translation of phandle to queue

    :param mbox:
        Mailbox controller
    :type mbox: struct mbox_controller \*

    :param p:
        phandle pointer
    :type p: const struct of_phandle_args \*

.. _`ti_msgmgr_of_xlate.return`:

Return
------

Mailbox channel corresponding to the queue, else return error
pointer.

.. _`ti_msgmgr_queue_setup`:

ti_msgmgr_queue_setup
=====================

.. c:function:: int ti_msgmgr_queue_setup(int idx, struct device *dev, struct device_node *np, struct ti_msgmgr_inst *inst, const struct ti_msgmgr_desc *d, const struct ti_msgmgr_valid_queue_desc *qd, struct ti_queue_inst *qinst, struct mbox_chan *chan)

    Setup data structures for each queue instance

    :param idx:
        index of the queue
    :type idx: int

    :param dev:
        pointer to the message manager device
    :type dev: struct device \*

    :param np:
        pointer to the of node
    :type np: struct device_node \*

    :param inst:
        Queue instance pointer
    :type inst: struct ti_msgmgr_inst \*

    :param d:
        Message Manager instance description data
    :type d: const struct ti_msgmgr_desc \*

    :param qd:
        Queue description data
    :type qd: const struct ti_msgmgr_valid_queue_desc \*

    :param qinst:
        Queue instance pointer
    :type qinst: struct ti_queue_inst \*

    :param chan:
        pointer to mailbox channel
    :type chan: struct mbox_chan \*

.. _`ti_msgmgr_queue_setup.return`:

Return
------

0 if all went well, else return corresponding error

.. This file was automatic generated / don't edit.

