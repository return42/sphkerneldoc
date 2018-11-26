.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/dim2/dim2.c

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
        u16 *reset_dbr_size;
        struct list_head pending_list;
        struct list_head started_list;
        enum most_channel_direction direction;
        enum most_channel_data_type data_type;
    }

.. _`hdm_channel.members`:

Members
-------

name
    *undescribed*

is_initialized
    identifier to know whether the channel is initialized

ch
    HAL specific channel data

reset_dbr_size
    *undescribed*

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
        struct device dev;
        struct hdm_channel hch[DMA_CHANNELS];
        struct most_channel_capability capabilities[DMA_CHANNELS];
        struct most_interface most_iface;
        char name[16 + sizeof "dim2-"];
        void __iomem *io_base;
        u8 clk_speed;
        struct clk *clk;
        struct clk *clk_pll;
        struct task_struct *netinfo_task;
        wait_queue_head_t netinfo_waitq;
        int deliver_netinfo;
        unsigned char mac_addrs[6];
        unsigned char link_state;
        int atx_idx;
        struct medialb_bus bus;
        void (*on_netinfo)(struct most_interface *most_iface, unsigned char link_state, unsigned char *addrs);
        void (*disable_platform)(struct platform_device *);
    }

.. _`dim2_hdm.members`:

Members
-------

dev
    *undescribed*

hch
    an array of channel specific data

capabilities
    an array of channel capability data

most_iface
    most interface structure

name
    *undescribed*

io_base
    I/O register base address

clk_speed
    *undescribed*

clk
    *undescribed*

clk_pll
    *undescribed*

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

on_netinfo
    *undescribed*

disable_platform
    *undescribed*

.. _`dimcb_io_read`:

dimcb_io_read
=============

.. c:function:: u32 dimcb_io_read(u32 __iomem *ptr32)

    callback from HAL to read an I/O register

    :param ptr32:
        register address
    :type ptr32: u32 __iomem \*

.. _`dimcb_io_write`:

dimcb_io_write
==============

.. c:function:: void dimcb_io_write(u32 __iomem *ptr32, u32 value)

    callback from HAL to write value to an I/O register

    :param ptr32:
        register address
    :type ptr32: u32 __iomem \*

    :param value:
        value to write
    :type value: u32

.. _`dimcb_on_error`:

dimcb_on_error
==============

.. c:function:: void dimcb_on_error(u8 error_id, const char *error_message)

    callback from HAL to report miscommunication between HDM and HAL

    :param error_id:
        Error ID
    :type error_id: u8

    :param error_message:
        Error message. Some text in a free format
    :type error_message: const char \*

.. _`try_start_dim_transfer`:

try_start_dim_transfer
======================

.. c:function:: int try_start_dim_transfer(struct hdm_channel *hdm_ch)

    try to transfer a buffer on a channel

    :param hdm_ch:
        channel specific data
    :type hdm_ch: struct hdm_channel \*

.. _`try_start_dim_transfer.description`:

Description
-----------

Transfer a buffer from pending_list if the channel is ready

.. _`deliver_netinfo_thread`:

deliver_netinfo_thread
======================

.. c:function:: int deliver_netinfo_thread(void *data)

    thread to deliver network status to mostcore

    :param data:
        private data
    :type data: void \*

.. _`deliver_netinfo_thread.description`:

Description
-----------

Wait for network status and deliver it to mostcore once it is received

.. _`retrieve_netinfo`:

retrieve_netinfo
================

.. c:function:: void retrieve_netinfo(struct dim2_hdm *dev, struct mbo *mbo)

    retrieve network status from received buffer

    :param dev:
        private data
    :type dev: struct dim2_hdm \*

    :param mbo:
        received MBO
    :type mbo: struct mbo \*

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

    :param dev:
        private data
    :type dev: struct dim2_hdm \*

    :param ch_idx:
        channel index
    :type ch_idx: int

.. _`service_done_flag.description`:

Description
-----------

Return back the completed buffers to mostcore, using completion callback

.. _`dim2_tasklet_fn`:

dim2_tasklet_fn
===============

.. c:function:: void dim2_tasklet_fn(unsigned long data)

    tasklet function

    :param data:
        private data
    :type data: unsigned long

.. _`dim2_tasklet_fn.description`:

Description
-----------

Service each initialized channel, if needed

.. _`dim2_ahb_isr`:

dim2_ahb_isr
============

.. c:function:: irqreturn_t dim2_ahb_isr(int irq, void *_dev)

    interrupt service routine

    :param irq:
        irq number
    :type irq: int

    :param _dev:
        private data
    :type _dev: void \*

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

    :param head:
        list head
    :type head: struct list_head \*

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

    :param most_iface:
        *undescribed*
    :type most_iface: struct most_interface \*

    :param ch_idx:
        *undescribed*
    :type ch_idx: int

    :param ccfg:
        *undescribed*
    :type ccfg: struct most_channel_config \*

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

    :param most_iface:
        *undescribed*
    :type most_iface: struct most_interface \*

    :param ch_idx:
        *undescribed*
    :type ch_idx: int

    :param mbo:
        pointer to the buffer object
    :type mbo: struct mbo \*

.. _`enqueue.description`:

Description
-----------

Push the buffer into pending_list and try to transfer one buffer from
pending_list. Return 0 on success, negative on failure.

.. _`request_netinfo`:

request_netinfo
===============

.. c:function:: void request_netinfo(struct most_interface *most_iface, int ch_idx, void (*on_netinfo)(struct most_interface *, unsigned char, unsigned char *))

    triggers retrieving of network info

    :param most_iface:
        *undescribed*
    :type most_iface: struct most_interface \*

    :param ch_idx:
        *undescribed*
    :type ch_idx: int

    :param void (\*on_netinfo)(struct most_interface \*, unsigned char, unsigned char \*):
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

    :param most_iface:
        *undescribed*
    :type most_iface: struct most_interface \*

    :param ch_idx:
        *undescribed*
    :type ch_idx: int

.. _`poison_channel.description`:

Description
-----------

Destroy a channel and complete all the buffers in both started_list &
pending_list. Return 0 on success, negative on failure.

.. _`get_dim2_clk_speed`:

get_dim2_clk_speed
==================

.. c:function:: int get_dim2_clk_speed(const char *clock_speed, u8 *val)

    converts string to DIM2 clock speed value

    :param clock_speed:
        string in the format "{NUMBER}fs"
    :type clock_speed: const char \*

    :param val:
        pointer to get one of the CLK_{NUMBER}FS values
    :type val: u8 \*

.. _`get_dim2_clk_speed.description`:

Description
-----------

By success stores one of the CLK_{NUMBER}FS in the \*val and returns 0,
otherwise returns -EINVAL.

.. _`dim2_remove`:

dim2_remove
===========

.. c:function:: int dim2_remove(struct platform_device *pdev)

    dim2 remove handler

    :param pdev:
        platform device structure
    :type pdev: struct platform_device \*

.. _`dim2_remove.description`:

Description
-----------

Unregister the interface from mostcore

.. This file was automatic generated / don't edit.

