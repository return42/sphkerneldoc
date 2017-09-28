.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/hsi/hsi.h

.. _`hsi_channel`:

struct hsi_channel
==================

.. c:type:: struct hsi_channel

    channel resource used by the hsi clients

.. _`hsi_channel.definition`:

Definition
----------

.. code-block:: c

    struct hsi_channel {
        unsigned int id;
        const char *name;
    }

.. _`hsi_channel.members`:

Members
-------

id
    Channel number

name
    Channel name

.. _`hsi_config`:

struct hsi_config
=================

.. c:type:: struct hsi_config

    Configuration for RX/TX HSI modules

.. _`hsi_config.definition`:

Definition
----------

.. code-block:: c

    struct hsi_config {
        unsigned int mode;
        struct hsi_channel *channels;
        unsigned int num_channels;
        unsigned int num_hw_channels;
        unsigned int speed;
        union {
            unsigned int flow;
            unsigned int arb_mode;
        } ;
    }

.. _`hsi_config.members`:

Members
-------

mode
    Bit transmission mode (STREAM or FRAME)

channels
    Channel resources used by the client

num_channels
    Number of channel resources

num_hw_channels
    Number of channels the transceiver is configured for [1..16]

speed
    Max bit transmission speed (Kbit/s)

{unnamed_union}
    anonymous

flow
    RX flow type (SYNCHRONIZED or PIPELINE)

arb_mode
    Arbitration mode for TX frame (Round robin, priority)

.. _`hsi_board_info`:

struct hsi_board_info
=====================

.. c:type:: struct hsi_board_info

    HSI client board info

.. _`hsi_board_info.definition`:

Definition
----------

.. code-block:: c

    struct hsi_board_info {
        const char *name;
        unsigned int hsi_id;
        unsigned int port;
        struct hsi_config tx_cfg;
        struct hsi_config rx_cfg;
        void *platform_data;
        struct dev_archdata *archdata;
    }

.. _`hsi_board_info.members`:

Members
-------

name
    Name for the HSI device

hsi_id
    HSI controller id where the client sits

port
    Port number in the controller where the client sits

tx_cfg
    HSI TX configuration

rx_cfg
    HSI RX configuration

platform_data
    Platform related data

archdata
    Architecture-dependent device data

.. _`hsi_client`:

struct hsi_client
=================

.. c:type:: struct hsi_client

    HSI client attached to an HSI port

.. _`hsi_client.definition`:

Definition
----------

.. code-block:: c

    struct hsi_client {
        struct device device;
        struct hsi_config tx_cfg;
        struct hsi_config rx_cfg;
    }

.. _`hsi_client.members`:

Members
-------

device
    Driver model representation of the device

tx_cfg
    HSI TX configuration

rx_cfg
    HSI RX configuration

.. _`hsi_client_driver`:

struct hsi_client_driver
========================

.. c:type:: struct hsi_client_driver

    Driver associated to an HSI client

.. _`hsi_client_driver.definition`:

Definition
----------

.. code-block:: c

    struct hsi_client_driver {
        struct device_driver driver;
    }

.. _`hsi_client_driver.members`:

Members
-------

driver
    Driver model representation of the driver

.. _`hsi_msg`:

struct hsi_msg
==============

.. c:type:: struct hsi_msg

    HSI message descriptor

.. _`hsi_msg.definition`:

Definition
----------

.. code-block:: c

    struct hsi_msg {
        struct list_head link;
        struct hsi_client *cl;
        struct sg_table sgt;
        void *context;
        void (*complete)(struct hsi_msg *msg);
        void (*destructor)(struct hsi_msg *msg);
        int status;
        unsigned int actual_len;
        unsigned int channel;
        unsigned int ttype:1;
        unsigned int break_frame:1;
    }

.. _`hsi_msg.members`:

Members
-------

link
    Free to use by the current descriptor owner

cl
    HSI device client that issues the transfer

sgt
    Head of the scatterlist array

context
    Client context data associated to the transfer

complete
    Transfer completion callback

destructor
    Destructor to free resources when flushing

status
    Status of the transfer when completed

actual_len
    Actual length of data transferred on completion

channel
    Channel were to TX/RX the message

ttype
    Transfer type (TX if set, RX otherwise)

break_frame
    if true HSI will send/receive a break frame. Data buffers are
    ignored in the request.

.. _`hsi_port`:

struct hsi_port
===============

.. c:type:: struct hsi_port

    HSI port device

.. _`hsi_port.definition`:

Definition
----------

.. code-block:: c

    struct hsi_port {
        struct device device;
        struct hsi_config tx_cfg;
        struct hsi_config rx_cfg;
        unsigned int num;
        unsigned int shared:1;
        int claimed;
        struct mutex lock;
        int (*async)(struct hsi_msg *msg);
        int (*setup)(struct hsi_client *cl);
        int (*flush)(struct hsi_client *cl);
        int (*start_tx)(struct hsi_client *cl);
        int (*stop_tx)(struct hsi_client *cl);
        int (*release)(struct hsi_client *cl);
        struct blocking_notifier_head n_head;
    }

.. _`hsi_port.members`:

Members
-------

device
    Driver model representation of the device

tx_cfg
    Current TX path configuration

rx_cfg
    Current RX path configuration

num
    Port number

shared
    Set when port can be shared by different clients

claimed
    Reference count of clients which claimed the port

lock
    Serialize port claim

async
    Asynchronous transfer callback

setup
    Callback to set the HSI client configuration

flush
    Callback to clean the HW state and destroy all pending transfers

start_tx
    Callback to inform that a client wants to TX data

stop_tx
    Callback to inform that a client no longer wishes to TX data

release
    Callback to inform that a client no longer uses the port

n_head
    Notifier chain for signaling port events to the clients.

.. _`hsi_controller`:

struct hsi_controller
=====================

.. c:type:: struct hsi_controller

    HSI controller device

.. _`hsi_controller.definition`:

Definition
----------

.. code-block:: c

    struct hsi_controller {
        struct device device;
        struct module *owner;
        unsigned int id;
        unsigned int num_ports;
        struct hsi_port **port;
    }

.. _`hsi_controller.members`:

Members
-------

device
    Driver model representation of the device

owner
    Pointer to the module owning the controller

id
    HSI controller ID

num_ports
    Number of ports in the HSI controller

port
    Array of HSI ports

.. _`hsi_id`:

hsi_id
======

.. c:function:: unsigned int hsi_id(struct hsi_client *cl)

    Get HSI controller ID associated to a client

    :param struct hsi_client \*cl:
        Pointer to a HSI client

.. _`hsi_id.description`:

Description
-----------

Return the controller id where the client is attached to

.. _`hsi_port_id`:

hsi_port_id
===========

.. c:function:: unsigned int hsi_port_id(struct hsi_client *cl)

    Gets the port number a client is attached to

    :param struct hsi_client \*cl:
        Pointer to HSI client

.. _`hsi_port_id.description`:

Description
-----------

Return the port number associated to the client

.. _`hsi_setup`:

hsi_setup
=========

.. c:function:: int hsi_setup(struct hsi_client *cl)

    Configure the client's port

    :param struct hsi_client \*cl:
        Pointer to the HSI client

.. _`hsi_setup.description`:

Description
-----------

When sharing ports, clients should either relay on a single
client setup or have the same setup for all of them.

Return -errno on failure, 0 on success

.. _`hsi_flush`:

hsi_flush
=========

.. c:function:: int hsi_flush(struct hsi_client *cl)

    Flush all pending transactions on the client's port

    :param struct hsi_client \*cl:
        Pointer to the HSI client

.. _`hsi_flush.description`:

Description
-----------

This function will destroy all pending hsi_msg in the port and reset
the HW port so it is ready to receive and transmit from a clean state.

Return -errno on failure, 0 on success

.. _`hsi_async_read`:

hsi_async_read
==============

.. c:function:: int hsi_async_read(struct hsi_client *cl, struct hsi_msg *msg)

    Submit a read transfer

    :param struct hsi_client \*cl:
        Pointer to the HSI client

    :param struct hsi_msg \*msg:
        HSI message descriptor of the transfer

.. _`hsi_async_read.description`:

Description
-----------

Return -errno on failure, 0 on success

.. _`hsi_async_write`:

hsi_async_write
===============

.. c:function:: int hsi_async_write(struct hsi_client *cl, struct hsi_msg *msg)

    Submit a write transfer

    :param struct hsi_client \*cl:
        Pointer to the HSI client

    :param struct hsi_msg \*msg:
        HSI message descriptor of the transfer

.. _`hsi_async_write.description`:

Description
-----------

Return -errno on failure, 0 on success

.. _`hsi_start_tx`:

hsi_start_tx
============

.. c:function:: int hsi_start_tx(struct hsi_client *cl)

    Signal the port that the client wants to start a TX

    :param struct hsi_client \*cl:
        Pointer to the HSI client

.. _`hsi_start_tx.description`:

Description
-----------

Return -errno on failure, 0 on success

.. _`hsi_stop_tx`:

hsi_stop_tx
===========

.. c:function:: int hsi_stop_tx(struct hsi_client *cl)

    Signal the port that the client no longer wants to transmit

    :param struct hsi_client \*cl:
        Pointer to the HSI client

.. _`hsi_stop_tx.description`:

Description
-----------

Return -errno on failure, 0 on success

.. This file was automatic generated / don't edit.

