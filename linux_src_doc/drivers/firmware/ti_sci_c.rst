.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/ti_sci.c

.. _`ti_sci_xfer`:

struct ti_sci_xfer
==================

.. c:type:: struct ti_sci_xfer

    Structure representing a message flow

.. _`ti_sci_xfer.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_xfer {
        struct ti_msgmgr_message tx_message;
        u8 rx_len;
        u8 *xfer_buf;
        struct completion done;
    }

.. _`ti_sci_xfer.members`:

Members
-------

tx_message
    Transmit message

rx_len
    Receive message length

xfer_buf
    Preallocated buffer to store receive message
    Since we work with request-ACK protocol, we can
    reuse the same buffer for the rx path as we
    use for the tx path.

done
    completion event

.. _`ti_sci_xfers_info`:

struct ti_sci_xfers_info
========================

.. c:type:: struct ti_sci_xfers_info

    Structure to manage transfer information

.. _`ti_sci_xfers_info.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_xfers_info {
        struct semaphore sem_xfer_count;
        struct ti_sci_xfer *xfer_block;
        unsigned long *xfer_alloc_table;
        spinlock_t xfer_lock;
    }

.. _`ti_sci_xfers_info.members`:

Members
-------

sem_xfer_count
    Counting Semaphore for managing max simultaneous
    Messages.

xfer_block
    Preallocated Message array

xfer_alloc_table
    Bitmap table for allocated messages.
    Index of this bitmap table is also used for message
    sequence identifier.

xfer_lock
    Protection for message allocation

.. _`ti_sci_desc`:

struct ti_sci_desc
==================

.. c:type:: struct ti_sci_desc

    Description of SoC integration

.. _`ti_sci_desc.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_desc {
        u8 host_id;
        int max_rx_timeout_ms;
        int max_msgs;
        int max_msg_size;
    }

.. _`ti_sci_desc.members`:

Members
-------

host_id
    Host identifier representing the compute entity

max_rx_timeout_ms
    Timeout for communication with SoC (in Milliseconds)

max_msgs
    Maximum number of messages that can be pending
    simultaneously in the system

max_msg_size
    Maximum size of data per message that can be handled.

.. _`ti_sci_info`:

struct ti_sci_info
==================

.. c:type:: struct ti_sci_info

    Structure representing a TI SCI instance

.. _`ti_sci_info.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_info {
        struct device *dev;
        struct notifier_block nb;
        const struct ti_sci_desc *desc;
        struct dentry *d;
        void __iomem *debug_region;
        char *debug_buffer;
        size_t debug_region_size;
        struct ti_sci_handle handle;
        struct mbox_client cl;
        struct mbox_chan *chan_tx;
        struct mbox_chan *chan_rx;
        struct ti_sci_xfers_info minfo;
        struct list_head node;
        int users;
    }

.. _`ti_sci_info.members`:

Members
-------

dev
    Device pointer

nb
    Reboot Notifier block

desc
    SoC description for this instance

d
    Debugfs file entry

debug_region
    Memory region where the debug message are available

debug_buffer
    Buffer allocated to copy debug messages.

debug_region_size
    Debug region size

handle
    Instance of TI SCI handle to send to clients.

cl
    Mailbox Client

chan_tx
    Transmit mailbox channel

chan_rx
    Receive mailbox channel

minfo
    Message info

node
    list head

users
    Number of users of this instance

.. _`ti_sci_debug_show`:

ti_sci_debug_show
=================

.. c:function:: int ti_sci_debug_show(struct seq_file *s, void *unused)

    Helper to dump the debug log

    :param struct seq_file \*s:
        sequence file pointer

    :param void \*unused:
        unused.

.. _`ti_sci_debug_show.return`:

Return
------

0

.. _`ti_sci_debug_open`:

ti_sci_debug_open
=================

.. c:function:: int ti_sci_debug_open(struct inode *inode, struct file *file)

    debug file open

    :param struct inode \*inode:
        inode pointer

    :param struct file \*file:
        file pointer

.. _`ti_sci_debug_open.return`:

Return
------

result of single_open

.. _`ti_sci_debugfs_create`:

ti_sci_debugfs_create
=====================

.. c:function:: int ti_sci_debugfs_create(struct platform_device *pdev, struct ti_sci_info *info)

    Create log debug file

    :param struct platform_device \*pdev:
        platform device pointer

    :param struct ti_sci_info \*info:
        Pointer to SCI entity information

.. _`ti_sci_debugfs_create.return`:

Return
------

0 if all went fine, else corresponding error.

.. _`ti_sci_debugfs_destroy`:

ti_sci_debugfs_destroy
======================

.. c:function:: void ti_sci_debugfs_destroy(struct platform_device *pdev, struct ti_sci_info *info)

    clean up log debug file

    :param struct platform_device \*pdev:
        platform device pointer

    :param struct ti_sci_info \*info:
        Pointer to SCI entity information

.. _`ti_sci_dump_header_dbg`:

ti_sci_dump_header_dbg
======================

.. c:function:: void ti_sci_dump_header_dbg(struct device *dev, struct ti_sci_msg_hdr *hdr)

    Helper to dump a message header.

    :param struct device \*dev:
        Device pointer corresponding to the SCI entity

    :param struct ti_sci_msg_hdr \*hdr:
        pointer to header.

.. _`ti_sci_rx_callback`:

ti_sci_rx_callback
==================

.. c:function:: void ti_sci_rx_callback(struct mbox_client *cl, void *m)

    mailbox client callback for receive messages

    :param struct mbox_client \*cl:
        client pointer

    :param void \*m:
        mailbox message

.. _`ti_sci_rx_callback.description`:

Description
-----------

Processes one received message to appropriate transfer information and
signals completion of the transfer.

.. _`ti_sci_rx_callback.note`:

NOTE
----

This function will be invoked in IRQ context, hence should be
as optimal as possible.

.. _`ti_sci_get_one_xfer`:

ti_sci_get_one_xfer
===================

.. c:function:: struct ti_sci_xfer *ti_sci_get_one_xfer(struct ti_sci_info *info, u16 msg_type, u32 msg_flags, size_t tx_message_size, size_t rx_message_size)

    Allocate one message

    :param struct ti_sci_info \*info:
        Pointer to SCI entity information

    :param u16 msg_type:
        Message type

    :param u32 msg_flags:
        Flag to set for the message

    :param size_t tx_message_size:
        transmit message size

    :param size_t rx_message_size:
        receive message size

.. _`ti_sci_get_one_xfer.description`:

Description
-----------

Helper function which is used by various command functions that are
exposed to clients of this driver for allocating a message traffic event.

This function can sleep depending on pending requests already in the system
for the SCI entity. Further, this also holds a spinlock to maintain integrity
of internal data structures.

.. _`ti_sci_get_one_xfer.return`:

Return
------

0 if all went fine, else corresponding error.

.. _`ti_sci_put_one_xfer`:

ti_sci_put_one_xfer
===================

.. c:function:: void ti_sci_put_one_xfer(struct ti_sci_xfers_info *minfo, struct ti_sci_xfer *xfer)

    Release a message

    :param struct ti_sci_xfers_info \*minfo:
        transfer info pointer

    :param struct ti_sci_xfer \*xfer:
        message that was reserved by ti_sci_get_one_xfer

.. _`ti_sci_put_one_xfer.description`:

Description
-----------

This holds a spinlock to maintain integrity of internal data structures.

.. _`ti_sci_do_xfer`:

ti_sci_do_xfer
==============

.. c:function:: int ti_sci_do_xfer(struct ti_sci_info *info, struct ti_sci_xfer *xfer)

    Do one transfer

    :param struct ti_sci_info \*info:
        Pointer to SCI entity information

    :param struct ti_sci_xfer \*xfer:
        Transfer to initiate and wait for response

.. _`ti_sci_do_xfer.return`:

Return
------

-ETIMEDOUT in case of no response, if transmit error,
return corresponding error, else if all goes well,
return 0.

.. _`ti_sci_cmd_get_revision`:

ti_sci_cmd_get_revision
=======================

.. c:function:: int ti_sci_cmd_get_revision(struct ti_sci_info *info)

    command to get the revision of the SCI entity

    :param struct ti_sci_info \*info:
        Pointer to SCI entity information

.. _`ti_sci_cmd_get_revision.description`:

Description
-----------

Updates the SCI information in the internal data structure.

.. _`ti_sci_cmd_get_revision.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_is_response_ack`:

ti_sci_is_response_ack
======================

.. c:function:: bool ti_sci_is_response_ack(void *r)

    Generic ACK/NACK message checkup

    :param void \*r:
        pointer to response buffer

.. _`ti_sci_is_response_ack.return`:

Return
------

true if the response was an ACK, else returns false.

.. _`ti_sci_set_device_state`:

ti_sci_set_device_state
=======================

.. c:function:: int ti_sci_set_device_state(const struct ti_sci_handle *handle, u32 id, u32 flags, u8 state)

    Set device state helper

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 id:
        Device identifier

    :param u32 flags:
        flags to setup for the device

    :param u8 state:
        State to move the device to

.. _`ti_sci_set_device_state.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_get_device_state`:

ti_sci_get_device_state
=======================

.. c:function:: int ti_sci_get_device_state(const struct ti_sci_handle *handle, u32 id, u32 *clcnt, u32 *resets, u8 *p_state, u8 *c_state)

    Get device state helper

    :param const struct ti_sci_handle \*handle:
        Handle to the device

    :param u32 id:
        Device Identifier

    :param u32 \*clcnt:
        Pointer to Context Loss Count

    :param u32 \*resets:
        pointer to resets

    :param u8 \*p_state:
        pointer to p_state

    :param u8 \*c_state:
        pointer to c_state

.. _`ti_sci_get_device_state.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_get_device`:

ti_sci_cmd_get_device
=====================

.. c:function:: int ti_sci_cmd_get_device(const struct ti_sci_handle *handle, u32 id)

    command to request for device managed by TISCI

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle as retrieved by \*ti_sci_get_handle

    :param u32 id:
        Device Identifier

.. _`ti_sci_cmd_get_device.description`:

Description
-----------

Request for the device - NOTE: the client MUST maintain integrity of
usage count by balancing get_device with put_device. No refcounting is
managed by driver for that purpose.

.. _`ti_sci_cmd_get_device.note`:

NOTE
----

The request is for exclusive access for the processor.

.. _`ti_sci_cmd_get_device.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_idle_device`:

ti_sci_cmd_idle_device
======================

.. c:function:: int ti_sci_cmd_idle_device(const struct ti_sci_handle *handle, u32 id)

    Command to idle a device managed by TISCI

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle as retrieved by \*ti_sci_get_handle

    :param u32 id:
        Device Identifier

.. _`ti_sci_cmd_idle_device.description`:

Description
-----------

Request for the device - NOTE: the client MUST maintain integrity of
usage count by balancing get_device with put_device. No refcounting is
managed by driver for that purpose.

.. _`ti_sci_cmd_idle_device.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_put_device`:

ti_sci_cmd_put_device
=====================

.. c:function:: int ti_sci_cmd_put_device(const struct ti_sci_handle *handle, u32 id)

    command to release a device managed by TISCI

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle as retrieved by \*ti_sci_get_handle

    :param u32 id:
        Device Identifier

.. _`ti_sci_cmd_put_device.description`:

Description
-----------

Request for the device - NOTE: the client MUST maintain integrity of
usage count by balancing get_device with put_device. No refcounting is
managed by driver for that purpose.

.. _`ti_sci_cmd_put_device.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_dev_is_valid`:

ti_sci_cmd_dev_is_valid
=======================

.. c:function:: int ti_sci_cmd_dev_is_valid(const struct ti_sci_handle *handle, u32 id)

    Is the device valid

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle as retrieved by \*ti_sci_get_handle

    :param u32 id:
        Device Identifier

.. _`ti_sci_cmd_dev_is_valid.return`:

Return
------

0 if all went fine and the device ID is valid, else return
appropriate error.

.. _`ti_sci_cmd_dev_get_clcnt`:

ti_sci_cmd_dev_get_clcnt
========================

.. c:function:: int ti_sci_cmd_dev_get_clcnt(const struct ti_sci_handle *handle, u32 id, u32 *count)

    Get context loss counter

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle

    :param u32 id:
        Device Identifier

    :param u32 \*count:
        Pointer to Context Loss counter to populate

.. _`ti_sci_cmd_dev_get_clcnt.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_dev_is_idle`:

ti_sci_cmd_dev_is_idle
======================

.. c:function:: int ti_sci_cmd_dev_is_idle(const struct ti_sci_handle *handle, u32 id, bool *r_state)

    Check if the device is requested to be idle

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle

    :param u32 id:
        Device Identifier

    :param bool \*r_state:
        true if requested to be idle

.. _`ti_sci_cmd_dev_is_idle.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_dev_is_stop`:

ti_sci_cmd_dev_is_stop
======================

.. c:function:: int ti_sci_cmd_dev_is_stop(const struct ti_sci_handle *handle, u32 id, bool *r_state, bool *curr_state)

    Check if the device is requested to be stopped

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle

    :param u32 id:
        Device Identifier

    :param bool \*r_state:
        true if requested to be stopped

    :param bool \*curr_state:
        true if currently stopped.

.. _`ti_sci_cmd_dev_is_stop.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_dev_is_on`:

ti_sci_cmd_dev_is_on
====================

.. c:function:: int ti_sci_cmd_dev_is_on(const struct ti_sci_handle *handle, u32 id, bool *r_state, bool *curr_state)

    Check if the device is requested to be ON

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle

    :param u32 id:
        Device Identifier

    :param bool \*r_state:
        true if requested to be ON

    :param bool \*curr_state:
        true if currently ON and active

.. _`ti_sci_cmd_dev_is_on.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_dev_is_trans`:

ti_sci_cmd_dev_is_trans
=======================

.. c:function:: int ti_sci_cmd_dev_is_trans(const struct ti_sci_handle *handle, u32 id, bool *curr_state)

    Check if the device is currently transitioning

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle

    :param u32 id:
        Device Identifier

    :param bool \*curr_state:
        true if currently transitioning.

.. _`ti_sci_cmd_dev_is_trans.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_set_device_resets`:

ti_sci_cmd_set_device_resets
============================

.. c:function:: int ti_sci_cmd_set_device_resets(const struct ti_sci_handle *handle, u32 id, u32 reset_state)

    command to set resets for device managed by TISCI

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle as retrieved by \*ti_sci_get_handle

    :param u32 id:
        Device Identifier

    :param u32 reset_state:
        Device specific reset bit field

.. _`ti_sci_cmd_set_device_resets.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_cmd_get_device_resets`:

ti_sci_cmd_get_device_resets
============================

.. c:function:: int ti_sci_cmd_get_device_resets(const struct ti_sci_handle *handle, u32 id, u32 *reset_state)

    Get reset state for device managed by TISCI

    :param const struct ti_sci_handle \*handle:
        Pointer to TISCI handle

    :param u32 id:
        Device Identifier

    :param u32 \*reset_state:
        Pointer to reset state to populate

.. _`ti_sci_cmd_get_device_resets.return`:

Return
------

0 if all went fine, else return appropriate error.

.. _`ti_sci_set_clock_state`:

ti_sci_set_clock_state
======================

.. c:function:: int ti_sci_set_clock_state(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, u32 flags, u8 state)

    Set clock state helper

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param u32 flags:
        Header flags as needed

    :param u8 state:
        State to request for the clock.

.. _`ti_sci_set_clock_state.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_get_clock_state`:

ti_sci_cmd_get_clock_state
==========================

.. c:function:: int ti_sci_cmd_get_clock_state(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, u8 *programmed_state, u8 *current_state)

    Get clock state helper

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param u8 \*programmed_state:
        State requested for clock to move to

    :param u8 \*current_state:
        State that the clock is currently in

.. _`ti_sci_cmd_get_clock_state.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_get_clock`:

ti_sci_cmd_get_clock
====================

.. c:function:: int ti_sci_cmd_get_clock(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, bool needs_ssc, bool can_change_freq, bool enable_input_term)

    Get control of a clock from TI SCI

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param bool needs_ssc:
        'true' if Spread Spectrum clock is desired, else 'false'

    :param bool can_change_freq:
        'true' if frequency change is desired, else 'false'

    :param bool enable_input_term:
        'true' if input termination is desired, else 'false'

.. _`ti_sci_cmd_get_clock.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_idle_clock`:

ti_sci_cmd_idle_clock
=====================

.. c:function:: int ti_sci_cmd_idle_clock(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id)

    Idle a clock which is in our control

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

.. _`ti_sci_cmd_idle_clock.note`:

NOTE
----

This clock must have been requested by get_clock previously.

.. _`ti_sci_cmd_idle_clock.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_put_clock`:

ti_sci_cmd_put_clock
====================

.. c:function:: int ti_sci_cmd_put_clock(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id)

    Release a clock from our control back to TISCI

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

.. _`ti_sci_cmd_put_clock.note`:

NOTE
----

This clock must have been requested by get_clock previously.

.. _`ti_sci_cmd_put_clock.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_clk_is_auto`:

ti_sci_cmd_clk_is_auto
======================

.. c:function:: int ti_sci_cmd_clk_is_auto(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, bool *req_state)

    Is the clock being auto managed

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param bool \*req_state:
        state indicating if the clock is auto managed

.. _`ti_sci_cmd_clk_is_auto.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_clk_is_on`:

ti_sci_cmd_clk_is_on
====================

.. c:function:: int ti_sci_cmd_clk_is_on(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, bool *req_state, bool *curr_state)

    Is the clock ON

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param bool \*req_state:
        state indicating if the clock is managed by us and enabled

    :param bool \*curr_state:
        state indicating if the clock is ready for operation

.. _`ti_sci_cmd_clk_is_on.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_clk_is_off`:

ti_sci_cmd_clk_is_off
=====================

.. c:function:: int ti_sci_cmd_clk_is_off(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, bool *req_state, bool *curr_state)

    Is the clock OFF

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param bool \*req_state:
        state indicating if the clock is managed by us and disabled

    :param bool \*curr_state:
        state indicating if the clock is NOT ready for operation

.. _`ti_sci_cmd_clk_is_off.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_clk_set_parent`:

ti_sci_cmd_clk_set_parent
=========================

.. c:function:: int ti_sci_cmd_clk_set_parent(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, u8 parent_id)

    Set the clock source of a specific device clock

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param u8 parent_id:
        Parent clock identifier to set

.. _`ti_sci_cmd_clk_set_parent.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_clk_get_parent`:

ti_sci_cmd_clk_get_parent
=========================

.. c:function:: int ti_sci_cmd_clk_get_parent(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, u8 *parent_id)

    Get current parent clock source

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param u8 \*parent_id:
        Current clock parent

.. _`ti_sci_cmd_clk_get_parent.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_clk_get_num_parents`:

ti_sci_cmd_clk_get_num_parents
==============================

.. c:function:: int ti_sci_cmd_clk_get_num_parents(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, u8 *num_parents)

    Get num parents of the current clk source

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param u8 \*num_parents:
        Returns he number of parents to the current clock.

.. _`ti_sci_cmd_clk_get_num_parents.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_clk_get_match_freq`:

ti_sci_cmd_clk_get_match_freq
=============================

.. c:function:: int ti_sci_cmd_clk_get_match_freq(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, u64 min_freq, u64 target_freq, u64 max_freq, u64 *match_freq)

    Find a good match for frequency

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param u64 min_freq:
        The minimum allowable frequency in Hz. This is the minimum
        allowable programmed frequency and does not account for clock
        tolerances and jitter.

    :param u64 target_freq:
        The target clock frequency in Hz. A frequency will be
        processed as close to this target frequency as possible.

    :param u64 max_freq:
        The maximum allowable frequency in Hz. This is the maximum
        allowable programmed frequency and does not account for clock
        tolerances and jitter.

    :param u64 \*match_freq:
        Frequency match in Hz response.

.. _`ti_sci_cmd_clk_get_match_freq.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_clk_set_freq`:

ti_sci_cmd_clk_set_freq
=======================

.. c:function:: int ti_sci_cmd_clk_set_freq(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, u64 min_freq, u64 target_freq, u64 max_freq)

    Set a frequency for clock

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param u64 min_freq:
        The minimum allowable frequency in Hz. This is the minimum
        allowable programmed frequency and does not account for clock
        tolerances and jitter.

    :param u64 target_freq:
        The target clock frequency in Hz. A frequency will be
        processed as close to this target frequency as possible.

    :param u64 max_freq:
        The maximum allowable frequency in Hz. This is the maximum
        allowable programmed frequency and does not account for clock
        tolerances and jitter.

.. _`ti_sci_cmd_clk_set_freq.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_cmd_clk_get_freq`:

ti_sci_cmd_clk_get_freq
=======================

.. c:function:: int ti_sci_cmd_clk_get_freq(const struct ti_sci_handle *handle, u32 dev_id, u8 clk_id, u64 *freq)

    Get current frequency

    :param const struct ti_sci_handle \*handle:
        pointer to TI SCI handle

    :param u32 dev_id:
        Device identifier this request is for

    :param u8 clk_id:
        Clock identifier for the device for this request.
        Each device has it's own set of clock inputs. This indexes
        which clock input to modify.

    :param u64 \*freq:
        Currently frequency in Hz

.. _`ti_sci_cmd_clk_get_freq.return`:

Return
------

0 if all went well, else returns appropriate error value.

.. _`ti_sci_get_handle`:

ti_sci_get_handle
=================

.. c:function:: const struct ti_sci_handle *ti_sci_get_handle(struct device *dev)

    Get the TI SCI handle for a device

    :param struct device \*dev:
        Pointer to device for which we want SCI handle

.. _`ti_sci_get_handle.note`:

NOTE
----

The function does not track individual clients of the framework
and is expected to be maintained by caller of TI SCI protocol library.
ti_sci_put_handle must be balanced with successful ti_sci_get_handle

.. _`ti_sci_get_handle.return`:

Return
------

pointer to handle if successful, else:
-EPROBE_DEFER if the instance is not ready
-ENODEV if the required node handler is missing
-EINVAL if invalid conditions are encountered.

.. _`ti_sci_put_handle`:

ti_sci_put_handle
=================

.. c:function:: int ti_sci_put_handle(const struct ti_sci_handle *handle)

    Release the handle acquired by ti_sci_get_handle

    :param const struct ti_sci_handle \*handle:
        Handle acquired by ti_sci_get_handle

.. _`ti_sci_put_handle.note`:

NOTE
----

The function does not track individual clients of the framework
and is expected to be maintained by caller of TI SCI protocol library.
ti_sci_put_handle must be balanced with successful ti_sci_get_handle

.. _`ti_sci_put_handle.return`:

Return
------

0 is successfully released
if an error pointer was passed, it returns the error value back,
if null was passed, it returns -EINVAL;

.. _`devm_ti_sci_get_handle`:

devm_ti_sci_get_handle
======================

.. c:function:: const struct ti_sci_handle *devm_ti_sci_get_handle(struct device *dev)

    Managed get handle

    :param struct device \*dev:
        device for which we want SCI handle for.

.. _`devm_ti_sci_get_handle.note`:

NOTE
----

This releases the handle once the device resources are
no longer needed. MUST NOT BE released with ti_sci_put_handle.
The function does not track individual clients of the framework
and is expected to be maintained by caller of TI SCI protocol library.

.. _`devm_ti_sci_get_handle.return`:

Return
------

0 if all went fine, else corresponding error.

.. This file was automatic generated / don't edit.

