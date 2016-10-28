.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/hdm-dim2/dim2_hdm.c

.. _`hdm_channel`:

struct hdm_channel
==================

.. c:type:: struct hdm_channel

    private structure to keep channel specific data

.. _`hdm_channel.definition`:

Definition
----------

.. code-block:: c

    struct hdm_channel {
        char name[sizeof "caNNN"];
        bool is_initialized;
        struct dim_channel ch;
        struct list_head pending_list;
        struct list_head started_list;
        enum most_channel_direction direction;
        enum most_channel_data_type data_type;
    }

.. _`hdm_channel.members`:

Members
-------

is_initialized
    identifier to know whether the channel is initialized

ch
    HAL specific channel data

pending_list
    list to keep MBO's before starting transfer

started_list
    list to keep MBO's after starting transfer

direction
    channel direction (TX or RX)

data_type
    channel data type

.. _`dim2_hdm`:

struct dim2_hdm
===============

.. c:type:: struct dim2_hdm

    private structure to keep interface specific data

.. _`dim2_hdm.definition`:

Definition
----------

.. code-block:: c

    struct dim2_hdm {
        struct hdm_channel hch[DMA_CHANNELS];
        struct most_channel_capability capabilities[DMA_CHANNELS];
        struct most_interface most_iface;
        char name[16 + sizeof "dim2-"];
        void __iomem *io_base;
        unsigned int irq_ahb0;
        int clk_speed;
        struct task_struct *netinfo_task;
        wait_queue_head_t netinfo_waitq;
        int deliver_netinfo;
        unsigned char mac_addrs[6];
        unsigned char link_state;
        int atx_idx;
        struct medialb_bus bus;
    }

.. _`dim2_hdm.members`:

Members
-------

hch
    an array of channel specific data

capabilities
    an array of channel capability data

most_iface
    most interface structure

io_base
    I/O register base address

irq_ahb0
    dim2 AHB0 irq number

clk_speed
    user selectable (through command line parameter) clock speed

netinfo_task
    thread to deliver network status

netinfo_waitq
    waitq for the thread to sleep

deliver_netinfo
    to identify whether network status received

mac_addrs
    INIC mac address

link_state
    network link state

atx_idx
    index of async tx channel

bus
    *undescribed*

.. _`dimcb_io_read`:

dimcb_io_read
=============

.. c:function:: u32 dimcb_io_read(u32 __iomem *ptr32)

    callback from HAL to read an I/O register

    :param u32 __iomem \*ptr32:
        register address

.. _`dimcb_io_write`:

dimcb_io_write
==============

.. c:function:: void dimcb_io_write(u32 __iomem *ptr32, u32 value)

    callback from HAL to write value to an I/O register

    :param u32 __iomem \*ptr32:
        register address

    :param u32 value:
        value to write

.. _`dimcb_on_error`:

dimcb_on_error
==============

.. c:function:: void dimcb_on_error(u8 error_id, const char *error_message)

    callback from HAL to report miscommunication between HDM and HAL

    :param u8 error_id:
        Error ID

    :param const char \*error_message:
        Error message. Some text in a free format

.. _`startup_dim`:

startup_dim
===========

.. c:function:: int startup_dim(struct platform_device *pdev)

    initialize the dim2 interface

    :param struct platform_device \*pdev:
        platform device

.. _`startup_dim.description`:

Description
-----------

Get the value of command line parameter "clock_speed" if given or use the
default value, enable the clock and PLL, and initialize the dim2 interface.

.. _`try_start_dim_transfer`:

try_start_dim_transfer
======================

.. c:function:: int try_start_dim_transfer(struct hdm_channel *hdm_ch)

    try to transfer a buffer on a channel

    :param struct hdm_channel \*hdm_ch:
        channel specific data

.. _`try_start_dim_transfer.description`:

Description
-----------

Transfer a buffer from pending_list if the channel is ready

.. _`deliver_netinfo_thread`:

deliver_netinfo_thread
======================

.. c:function:: int deliver_netinfo_thread(void *data)

    thread to deliver network status to mostcore

    :param void \*data:
        private data

.. _`deliver_netinfo_thread.description`:

Description
-----------

Wait for network status and deliver it to mostcore once it is received

.. _`retrieve_netinfo`:

retrieve_netinfo
================

.. c:function:: void retrieve_netinfo(struct dim2_hdm *dev, struct mbo *mbo)

    retrieve network status from received buffer

    :param struct dim2_hdm \*dev:
        private data

    :param struct mbo \*mbo:
        received MBO

.. _`retrieve_netinfo.description`:

Description
-----------

Parse the message in buffer and get node address, link state, MAC address.
Wake up a thread to deliver this status to mostcore

.. _`service_done_flag`:

service_done_flag
=================

.. c:function:: void service_done_flag(struct dim2_hdm *dev, int ch_idx)

    handle completed buffers

    :param struct dim2_hdm \*dev:
        private data

    :param int ch_idx:
        channel index

.. _`service_done_flag.description`:

Description
-----------

Return back the completed buffers to mostcore, using completion callback

.. _`dim2_tasklet_fn`:

dim2_tasklet_fn
===============

.. c:function:: void dim2_tasklet_fn(unsigned long data)

    tasklet function

    :param unsigned long data:
        private data

.. _`dim2_tasklet_fn.description`:

Description
-----------

Service each initialized channel, if needed

.. _`dim2_ahb_isr`:

dim2_ahb_isr
============

.. c:function:: irqreturn_t dim2_ahb_isr(int irq, void *_dev)

    interrupt service routine

    :param int irq:
        irq number

    :param void \*_dev:
        private data

.. _`dim2_ahb_isr.description`:

Description
-----------

Acknowledge the interrupt and schedule a tasklet to service channels.
Return IRQ_HANDLED.

.. _`complete_all_mbos`:

complete_all_mbos
=================

.. c:function:: void complete_all_mbos(struct list_head *head)

    complete MBO's in a list

    :param struct list_head \*head:
        list head

.. _`complete_all_mbos.description`:

Description
-----------

Delete all the entries in list and return back MBO's to mostcore using
completion call back.

.. _`configure_channel`:

configure_channel
=================

.. c:function:: int configure_channel(struct most_interface *most_iface, int ch_idx, struct most_channel_config *ccfg)

    initialize a channel

    :param struct most_interface \*most_iface:
        *undescribed*

    :param int ch_idx:
        *undescribed*

    :param struct most_channel_config \*ccfg:
        *undescribed*

.. _`configure_channel.description`:

Description
-----------

Receives configuration information from mostcore and initialize
the corresponding channel. Return 0 on success, negative on failure.

.. _`enqueue`:

enqueue
=======

.. c:function:: int enqueue(struct most_interface *most_iface, int ch_idx, struct mbo *mbo)

    enqueue a buffer for data transfer

    :param struct most_interface \*most_iface:
        *undescribed*

    :param int ch_idx:
        *undescribed*

    :param struct mbo \*mbo:
        pointer to the buffer object

.. _`enqueue.description`:

Description
-----------

Push the buffer into pending_list and try to transfer one buffer from
pending_list. Return 0 on success, negative on failure.

.. _`request_netinfo`:

request_netinfo
===============

.. c:function:: void request_netinfo(struct most_interface *most_iface, int ch_idx)

    triggers retrieving of network info

    :param struct most_interface \*most_iface:
        *undescribed*

    :param int ch_idx:
        *undescribed*

.. _`request_netinfo.description`:

Description
-----------

Send a command to INIC which triggers retrieving of network info by means of
"Message exchange over MDP/MEP". Return 0 on success, negative on failure.

.. _`poison_channel`:

poison_channel
==============

.. c:function:: int poison_channel(struct most_interface *most_iface, int ch_idx)

    poison buffers of a channel

    :param struct most_interface \*most_iface:
        *undescribed*

    :param int ch_idx:
        *undescribed*

.. _`poison_channel.description`:

Description
-----------

Destroy a channel and complete all the buffers in both started_list &
pending_list. Return 0 on success, negative on failure.

.. _`dim2_remove`:

dim2_remove
===========

.. c:function:: int dim2_remove(struct platform_device *pdev)

    dim2 remove handler

    :param struct platform_device \*pdev:
        platform device structure

.. _`dim2_remove.description`:

Description
-----------

Unregister the interface from mostcore

.. This file was automatic generated / don't edit.

