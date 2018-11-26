.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/arm_scmi/driver.c

.. _`scmi_xfers_info`:

struct scmi_xfers_info
======================

.. c:type:: struct scmi_xfers_info

    Structure to manage transfer information

.. _`scmi_xfers_info.definition`:

Definition
----------

.. code-block:: c

    struct scmi_xfers_info {
        struct scmi_xfer *xfer_block;
        unsigned long *xfer_alloc_table;
        spinlock_t xfer_lock;
    }

.. _`scmi_xfers_info.members`:

Members
-------

xfer_block
    Preallocated Message array

xfer_alloc_table
    Bitmap table for allocated messages.
    Index of this bitmap table is also used for message
    sequence identifier.

xfer_lock
    Protection for message allocation

.. _`scmi_desc`:

struct scmi_desc
================

.. c:type:: struct scmi_desc

    Description of SoC integration

.. _`scmi_desc.definition`:

Definition
----------

.. code-block:: c

    struct scmi_desc {
        int max_rx_timeout_ms;
        int max_msg;
        int max_msg_size;
    }

.. _`scmi_desc.members`:

Members
-------

max_rx_timeout_ms
    Timeout for communication with SoC (in Milliseconds)

max_msg
    Maximum number of messages that can be pending
    simultaneously in the system

max_msg_size
    Maximum size of data per message that can be handled.

.. _`scmi_chan_info`:

struct scmi_chan_info
=====================

.. c:type:: struct scmi_chan_info

    Structure representing a SCMI channel informfation

.. _`scmi_chan_info.definition`:

Definition
----------

.. code-block:: c

    struct scmi_chan_info {
        struct mbox_client cl;
        struct mbox_chan *chan;
        void __iomem *payload;
        struct device *dev;
        struct scmi_handle *handle;
    }

.. _`scmi_chan_info.members`:

Members
-------

cl
    Mailbox Client

chan
    Transmit/Receive mailbox channel

payload
    Transmit/Receive mailbox channel payload area

dev
    Reference to device in the SCMI hierarchy corresponding to this
    channel

handle
    Pointer to SCMI entity handle

.. _`scmi_info`:

struct scmi_info
================

.. c:type:: struct scmi_info

    Structure representing a SCMI instance

.. _`scmi_info.definition`:

Definition
----------

.. code-block:: c

    struct scmi_info {
        struct device *dev;
        const struct scmi_desc *desc;
        struct scmi_revision_info version;
        struct scmi_handle handle;
        struct scmi_xfers_info minfo;
        struct idr tx_idr;
        u8 *protocols_imp;
        struct list_head node;
        int users;
    }

.. _`scmi_info.members`:

Members
-------

dev
    Device pointer

desc
    SoC description for this instance

version
    SCMI revision information containing protocol version,
    implementation version and (sub-)vendor identification.

handle
    Instance of SCMI handle to send to clients

minfo
    Message info

tx_idr
    IDR object to map protocol id to channel info pointer

protocols_imp
    List of protocols implemented, currently maximum of
    MAX_PROTOCOLS_IMP elements allocated by the base protocol

node
    List head

users
    Number of users of this instance

.. _`scmi_dump_header_dbg`:

scmi_dump_header_dbg
====================

.. c:function:: void scmi_dump_header_dbg(struct device *dev, struct scmi_msg_hdr *hdr)

    Helper to dump a message header.

    :param dev:
        Device pointer corresponding to the SCMI entity
    :type dev: struct device \*

    :param hdr:
        pointer to header.
    :type hdr: struct scmi_msg_hdr \*

.. _`scmi_rx_callback`:

scmi_rx_callback
================

.. c:function:: void scmi_rx_callback(struct mbox_client *cl, void *m)

    mailbox client callback for receive messages

    :param cl:
        client pointer
    :type cl: struct mbox_client \*

    :param m:
        mailbox message
    :type m: void \*

.. _`scmi_rx_callback.description`:

Description
-----------

Processes one received message to appropriate transfer information and
signals completion of the transfer.

.. _`scmi_rx_callback.note`:

NOTE
----

This function will be invoked in IRQ context, hence should be
as optimal as possible.

.. _`pack_scmi_header`:

pack_scmi_header
================

.. c:function:: u32 pack_scmi_header(struct scmi_msg_hdr *hdr)

    packs and returns 32-bit header

    :param hdr:
        pointer to header containing all the information on message id,
        protocol id and sequence id.
    :type hdr: struct scmi_msg_hdr \*

.. _`pack_scmi_header.return`:

Return
------

32-bit packed command header to be sent to the platform.

.. _`scmi_tx_prepare`:

scmi_tx_prepare
===============

.. c:function:: void scmi_tx_prepare(struct mbox_client *cl, void *m)

    mailbox client callback to prepare for the transfer

    :param cl:
        client pointer
    :type cl: struct mbox_client \*

    :param m:
        mailbox message
    :type m: void \*

.. _`scmi_tx_prepare.description`:

Description
-----------

This function prepares the shared memory which contains the header and the
payload.

.. _`scmi_xfer_get`:

scmi_xfer_get
=============

.. c:function:: struct scmi_xfer *scmi_xfer_get(const struct scmi_handle *handle)

    Allocate one message

    :param handle:
        Pointer to SCMI entity handle
    :type handle: const struct scmi_handle \*

.. _`scmi_xfer_get.description`:

Description
-----------

Helper function which is used by various command functions that are
exposed to clients of this driver for allocating a message traffic event.

This function can sleep depending on pending requests already in the system
for the SCMI entity. Further, this also holds a spinlock to maintain
integrity of internal data structures.

.. _`scmi_xfer_get.return`:

Return
------

0 if all went fine, else corresponding error.

.. _`scmi_xfer_put`:

scmi_xfer_put
=============

.. c:function:: void scmi_xfer_put(const struct scmi_handle *handle, struct scmi_xfer *xfer)

    Release a message

    :param handle:
        Pointer to SCMI entity handle
    :type handle: const struct scmi_handle \*

    :param xfer:
        message that was reserved by scmi_xfer_get
    :type xfer: struct scmi_xfer \*

.. _`scmi_xfer_put.description`:

Description
-----------

This holds a spinlock to maintain integrity of internal data structures.

.. _`scmi_do_xfer`:

scmi_do_xfer
============

.. c:function:: int scmi_do_xfer(const struct scmi_handle *handle, struct scmi_xfer *xfer)

    Do one transfer

    :param handle:
        Pointer to SCMI entity handle
    :type handle: const struct scmi_handle \*

    :param xfer:
        Transfer to initiate and wait for response
    :type xfer: struct scmi_xfer \*

.. _`scmi_do_xfer.return`:

Return
------

-ETIMEDOUT in case of no response, if transmit error,
return corresponding error, else if all goes well,
return 0.

.. _`scmi_xfer_get_init`:

scmi_xfer_get_init
==================

.. c:function:: int scmi_xfer_get_init(const struct scmi_handle *handle, u8 msg_id, u8 prot_id, size_t tx_size, size_t rx_size, struct scmi_xfer **p)

    Allocate and initialise one message

    :param handle:
        Pointer to SCMI entity handle
    :type handle: const struct scmi_handle \*

    :param msg_id:
        Message identifier
    :type msg_id: u8

    :param prot_id:
        Protocol identifier for the message
    :type prot_id: u8

    :param tx_size:
        transmit message size
    :type tx_size: size_t

    :param rx_size:
        receive message size
    :type rx_size: size_t

    :param p:
        pointer to the allocated and initialised message
    :type p: struct scmi_xfer \*\*

.. _`scmi_xfer_get_init.description`:

Description
-----------

This function allocates the message using \ ``scmi_xfer_get``\  and
initialise the header.

.. _`scmi_xfer_get_init.return`:

Return
------

0 if all went fine with \ ``p``\  pointing to message, else
corresponding error.

.. _`scmi_version_get`:

scmi_version_get
================

.. c:function:: int scmi_version_get(const struct scmi_handle *handle, u8 protocol, u32 *version)

    command to get the revision of the SCMI entity

    :param handle:
        Pointer to SCMI entity handle
    :type handle: const struct scmi_handle \*

    :param protocol:
        Protocol identifier for the message
    :type protocol: u8

    :param version:
        Holds returned version of protocol.
    :type version: u32 \*

.. _`scmi_version_get.description`:

Description
-----------

Updates the SCMI information in the internal data structure.

.. _`scmi_version_get.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`scmi_handle_get`:

scmi_handle_get
===============

.. c:function:: struct scmi_handle *scmi_handle_get(struct device *dev)

    Get the SCMI handle for a device

    :param dev:
        pointer to device for which we want SCMI handle
    :type dev: struct device \*

.. _`scmi_handle_get.note`:

NOTE
----

The function does not track individual clients of the framework
and is expected to be maintained by caller of SCMI protocol library.
scmi_handle_put must be balanced with successful scmi_handle_get

.. _`scmi_handle_get.return`:

Return
------

pointer to handle if successful, NULL on error

.. _`scmi_handle_put`:

scmi_handle_put
===============

.. c:function:: int scmi_handle_put(const struct scmi_handle *handle)

    Release the handle acquired by scmi_handle_get

    :param handle:
        handle acquired by scmi_handle_get
    :type handle: const struct scmi_handle \*

.. _`scmi_handle_put.note`:

NOTE
----

The function does not track individual clients of the framework
and is expected to be maintained by caller of SCMI protocol library.
scmi_handle_put must be balanced with successful scmi_handle_get

.. _`scmi_handle_put.return`:

Return
------

0 is successfully released
if null was passed, it returns -EINVAL;

.. This file was automatic generated / don't edit.

