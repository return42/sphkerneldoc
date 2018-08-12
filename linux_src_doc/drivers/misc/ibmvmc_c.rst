.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/ibmvmc.c

.. _`h_request_vmc`:

h_request_vmc
=============

.. c:function:: long h_request_vmc(u32 *vmc_index)

    - request a hypervisor virtual management channel device

    :param u32 \*vmc_index:
        drc index of the vmc device created

.. _`h_request_vmc.description`:

Description
-----------

Requests the hypervisor create a new virtual management channel device,
allowing this partition to send hypervisor virtualization control
commands.

.. _`h_request_vmc.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_handle_event`:

ibmvmc_handle_event
===================

.. c:function:: irqreturn_t ibmvmc_handle_event(int irq, void *dev_instance)

    - Interrupt handler for crq events

    :param int irq:
        number of irq to handle, not used

    :param void \*dev_instance:
        crq_server_adapter that received interrupt

.. _`ibmvmc_handle_event.description`:

Description
-----------

Disables interrupts and schedules ibmvmc_task

Always returns IRQ_HANDLED

.. _`ibmvmc_release_crq_queue`:

ibmvmc_release_crq_queue
========================

.. c:function:: void ibmvmc_release_crq_queue(struct crq_server_adapter *adapter)

    Release CRQ Queue

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

.. _`ibmvmc_release_crq_queue.return`:

Return
------

0 - Success
Non-Zero - Failure

.. _`ibmvmc_reset_crq_queue`:

ibmvmc_reset_crq_queue
======================

.. c:function:: int ibmvmc_reset_crq_queue(struct crq_server_adapter *adapter)

    Reset CRQ Queue

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

.. _`ibmvmc_reset_crq_queue.description`:

Description
-----------

This function calls h_free_crq and then calls H_REG_CRQ and does all the
bookkeeping to get us back to where we can communicate.

.. _`ibmvmc_reset_crq_queue.return`:

Return
------

0 - Success
Non-Zero - Failure

.. _`crq_queue_next_crq`:

crq_queue_next_crq
==================

.. c:function:: struct ibmvmc_crq_msg *crq_queue_next_crq(struct crq_queue *queue)

    - Returns the next entry in message queue

    :param struct crq_queue \*queue:
        crq_queue to use

.. _`crq_queue_next_crq.description`:

Description
-----------

Returns pointer to next entry in queue, or NULL if there are no new
entried in the CRQ.

.. _`ibmvmc_send_crq`:

ibmvmc_send_crq
===============

.. c:function:: long ibmvmc_send_crq(struct crq_server_adapter *adapter, u64 word1, u64 word2)

    Send CRQ

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param u64 word1:
        Word1 Data field

    :param u64 word2:
        Word2 Data field

.. _`ibmvmc_send_crq.return`:

Return
------

0 - Success
Non-Zero - Failure

.. _`alloc_dma_buffer`:

alloc_dma_buffer
================

.. c:function:: void *alloc_dma_buffer(struct vio_dev *vdev, size_t size, dma_addr_t *dma_handle)

    Create DMA Buffer

    :param struct vio_dev \*vdev:
        vio_dev struct

    :param size_t size:
        Size field

    :param dma_addr_t \*dma_handle:
        DMA address field

.. _`alloc_dma_buffer.description`:

Description
-----------

Allocates memory for the command queue and maps remote memory into an
ioba.

Returns a pointer to the buffer

.. _`free_dma_buffer`:

free_dma_buffer
===============

.. c:function:: void free_dma_buffer(struct vio_dev *vdev, size_t size, void *vaddr, dma_addr_t dma_handle)

    Free DMA Buffer

    :param struct vio_dev \*vdev:
        vio_dev struct

    :param size_t size:
        Size field

    :param void \*vaddr:
        Address field

    :param dma_addr_t dma_handle:
        DMA address field

.. _`free_dma_buffer.description`:

Description
-----------

Releases memory for a command queue and unmaps mapped remote memory.

.. _`ibmvmc_get_valid_hmc_buffer`:

ibmvmc_get_valid_hmc_buffer
===========================

.. c:function:: struct ibmvmc_buffer *ibmvmc_get_valid_hmc_buffer(u8 hmc_index)

    Retrieve Valid HMC Buffer

    :param u8 hmc_index:
        HMC Index Field

.. _`ibmvmc_get_valid_hmc_buffer.return`:

Return
------

Pointer to ibmvmc_buffer

.. _`ibmvmc_get_free_hmc_buffer`:

ibmvmc_get_free_hmc_buffer
==========================

.. c:function:: struct ibmvmc_buffer *ibmvmc_get_free_hmc_buffer(struct crq_server_adapter *adapter, u8 hmc_index)

    Get Free HMC Buffer

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param u8 hmc_index:
        Hmc Index field

.. _`ibmvmc_get_free_hmc_buffer.return`:

Return
------

Pointer to ibmvmc_buffer

.. _`ibmvmc_free_hmc_buffer`:

ibmvmc_free_hmc_buffer
======================

.. c:function:: void ibmvmc_free_hmc_buffer(struct ibmvmc_hmc *hmc, struct ibmvmc_buffer *buffer)

    Free an HMC Buffer

    :param struct ibmvmc_hmc \*hmc:
        ibmvmc_hmc struct

    :param struct ibmvmc_buffer \*buffer:
        ibmvmc_buffer struct

.. _`ibmvmc_count_hmc_buffers`:

ibmvmc_count_hmc_buffers
========================

.. c:function:: void ibmvmc_count_hmc_buffers(u8 hmc_index, unsigned int *valid, unsigned int *free)

    Count HMC Buffers

    :param u8 hmc_index:
        HMC Index field

    :param unsigned int \*valid:
        Valid number of buffers field

    :param unsigned int \*free:
        Free number of buffers field

.. _`ibmvmc_get_free_hmc`:

ibmvmc_get_free_hmc
===================

.. c:function:: struct ibmvmc_hmc *ibmvmc_get_free_hmc( void)

    Get Free HMC

    :param  void:
        no arguments

.. _`ibmvmc_get_free_hmc.return`:

Return
------

Pointer to an available HMC Connection
Null otherwise

.. _`ibmvmc_return_hmc`:

ibmvmc_return_hmc
=================

.. c:function:: int ibmvmc_return_hmc(struct ibmvmc_hmc *hmc, bool release_readers)

    Return an HMC Connection

    :param struct ibmvmc_hmc \*hmc:
        ibmvmc_hmc struct

    :param bool release_readers:
        Number of readers connected to session

.. _`ibmvmc_return_hmc.description`:

Description
-----------

This function releases the HMC connections back into the pool.

.. _`ibmvmc_return_hmc.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_send_open`:

ibmvmc_send_open
================

.. c:function:: int ibmvmc_send_open(struct ibmvmc_buffer *buffer, struct ibmvmc_hmc *hmc)

    Interface Open

    :param struct ibmvmc_buffer \*buffer:
        Pointer to ibmvmc_buffer struct

    :param struct ibmvmc_hmc \*hmc:
        Pointer to ibmvmc_hmc struct

.. _`ibmvmc_send_open.description`:

Description
-----------

This command is sent by the management partition as the result of a
management partition device request. It causes the hypervisor to
prepare a set of data buffers for the management application connection
indicated HMC idx. A unique HMC Idx would be used if multiple management
applications running concurrently were desired. Before responding to this
command, the hypervisor must provide the management partition with at
least one of these new buffers via the Add Buffer. This indicates whether
the messages are inbound or outbound from the hypervisor.

.. _`ibmvmc_send_open.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_send_close`:

ibmvmc_send_close
=================

.. c:function:: int ibmvmc_send_close(struct ibmvmc_hmc *hmc)

    Interface Close

    :param struct ibmvmc_hmc \*hmc:
        Pointer to ibmvmc_hmc struct

.. _`ibmvmc_send_close.description`:

Description
-----------

This command is sent by the management partition to terminate a
management application to hypervisor connection. When this command is
sent, the management partition has quiesced all I/O operations to all
buffers associated with this management application connection, and
has freed any storage for these buffers.

.. _`ibmvmc_send_close.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_send_capabilities`:

ibmvmc_send_capabilities
========================

.. c:function:: int ibmvmc_send_capabilities(struct crq_server_adapter *adapter)

    Send VMC Capabilities

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

.. _`ibmvmc_send_capabilities.description`:

Description
-----------

The capabilities message is an administrative message sent after the CRQ
initialization sequence of messages and is used to exchange VMC capabilities
between the management partition and the hypervisor. The management
partition must send this message and the hypervisor must respond with VMC
capabilities Response message before HMC interface message can begin. Any
HMC interface messages received before the exchange of capabilities has
complete are dropped.

.. _`ibmvmc_send_capabilities.return`:

Return
------

0 - Success

.. _`ibmvmc_send_add_buffer_resp`:

ibmvmc_send_add_buffer_resp
===========================

.. c:function:: int ibmvmc_send_add_buffer_resp(struct crq_server_adapter *adapter, u8 status, u8 hmc_session, u8 hmc_index, u16 buffer_id)

    Add Buffer Response

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param u8 status:
        Status field

    :param u8 hmc_session:
        HMC Session field

    :param u8 hmc_index:
        HMC Index field

    :param u16 buffer_id:
        Buffer Id field

.. _`ibmvmc_send_add_buffer_resp.description`:

Description
-----------

This command is sent by the management partition to the hypervisor in
response to the Add Buffer message. The Status field indicates the result of
the command.

.. _`ibmvmc_send_add_buffer_resp.return`:

Return
------

0 - Success

.. _`ibmvmc_send_rem_buffer_resp`:

ibmvmc_send_rem_buffer_resp
===========================

.. c:function:: int ibmvmc_send_rem_buffer_resp(struct crq_server_adapter *adapter, u8 status, u8 hmc_session, u8 hmc_index, u16 buffer_id)

    Remove Buffer Response

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param u8 status:
        Status field

    :param u8 hmc_session:
        HMC Session field

    :param u8 hmc_index:
        HMC Index field

    :param u16 buffer_id:
        Buffer Id field

.. _`ibmvmc_send_rem_buffer_resp.description`:

Description
-----------

This command is sent by the management partition to the hypervisor in
response to the Remove Buffer message. The Buffer ID field indicates
which buffer the management partition selected to remove. The Status
field indicates the result of the command.

.. _`ibmvmc_send_rem_buffer_resp.return`:

Return
------

0 - Success

.. _`ibmvmc_send_msg`:

ibmvmc_send_msg
===============

.. c:function:: int ibmvmc_send_msg(struct crq_server_adapter *adapter, struct ibmvmc_buffer *buffer, struct ibmvmc_hmc *hmc, int msg_len)

    Signal Message

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param struct ibmvmc_buffer \*buffer:
        ibmvmc_buffer struct

    :param struct ibmvmc_hmc \*hmc:
        ibmvmc_hmc struct

    :param int msg_len:
        *undescribed*

.. _`ibmvmc_send_msg.description`:

Description
-----------

This command is sent between the management partition and the hypervisor
in order to signal the arrival of an HMC protocol message. The command
can be sent by both the management partition and the hypervisor. It is
used for all traffic between the management application and the hypervisor,
regardless of who initiated the communication.

There is no response to this message.

.. _`ibmvmc_send_msg.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_open`:

ibmvmc_open
===========

.. c:function:: int ibmvmc_open(struct inode *inode, struct file *file)

    Open Session

    :param struct inode \*inode:
        inode struct

    :param struct file \*file:
        file struct

.. _`ibmvmc_open.return`:

Return
------

0 - Success

.. _`ibmvmc_close`:

ibmvmc_close
============

.. c:function:: int ibmvmc_close(struct inode *inode, struct file *file)

    Close Session

    :param struct inode \*inode:
        inode struct

    :param struct file \*file:
        file struct

.. _`ibmvmc_close.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_read`:

ibmvmc_read
===========

.. c:function:: ssize_t ibmvmc_read(struct file *file, char *buf, size_t nbytes, loff_t *ppos)

    Read

    :param struct file \*file:
        file struct

    :param char \*buf:
        Character buffer

    :param size_t nbytes:
        Size in bytes

    :param loff_t \*ppos:
        Offset

.. _`ibmvmc_read.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_poll`:

ibmvmc_poll
===========

.. c:function:: unsigned int ibmvmc_poll(struct file *file, poll_table *wait)

    Poll

    :param struct file \*file:
        file struct

    :param poll_table \*wait:
        Poll Table

.. _`ibmvmc_poll.return`:

Return
------

poll.h return values

.. _`ibmvmc_write`:

ibmvmc_write
============

.. c:function:: ssize_t ibmvmc_write(struct file *file, const char *buffer, size_t count, loff_t *ppos)

    Write

    :param struct file \*file:
        file struct

    :param const char \*buffer:
        *undescribed*

    :param size_t count:
        Count field

    :param loff_t \*ppos:
        Offset

.. _`ibmvmc_write.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_setup_hmc`:

ibmvmc_setup_hmc
================

.. c:function:: long ibmvmc_setup_hmc(struct ibmvmc_file_session *session)

    Setup the HMC

    :param struct ibmvmc_file_session \*session:
        ibmvmc_file_session struct

.. _`ibmvmc_setup_hmc.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_ioctl_sethmcid`:

ibmvmc_ioctl_sethmcid
=====================

.. c:function:: long ibmvmc_ioctl_sethmcid(struct ibmvmc_file_session *session, unsigned char __user *new_hmc_id)

    IOCTL Set HMC ID

    :param struct ibmvmc_file_session \*session:
        ibmvmc_file_session struct

    :param unsigned char __user \*new_hmc_id:
        HMC id field

.. _`ibmvmc_ioctl_sethmcid.description`:

Description
-----------

IOCTL command to setup the hmc id

.. _`ibmvmc_ioctl_sethmcid.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_ioctl_query`:

ibmvmc_ioctl_query
==================

.. c:function:: long ibmvmc_ioctl_query(struct ibmvmc_file_session *session, struct ibmvmc_query_struct __user *ret_struct)

    IOCTL Query

    :param struct ibmvmc_file_session \*session:
        ibmvmc_file_session struct

    :param struct ibmvmc_query_struct __user \*ret_struct:
        ibmvmc_query_struct

.. _`ibmvmc_ioctl_query.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_ioctl_requestvmc`:

ibmvmc_ioctl_requestvmc
=======================

.. c:function:: long ibmvmc_ioctl_requestvmc(struct ibmvmc_file_session *session, u32 __user *ret_vmc_index)

    IOCTL Request VMC

    :param struct ibmvmc_file_session \*session:
        ibmvmc_file_session struct

    :param u32 __user \*ret_vmc_index:
        VMC Index

.. _`ibmvmc_ioctl_requestvmc.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_ioctl`:

ibmvmc_ioctl
============

.. c:function:: long ibmvmc_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    IOCTL

    :param struct file \*file:
        *undescribed*

    :param unsigned int cmd:
        cmd field

    :param unsigned long arg:
        Argument field

.. _`ibmvmc_ioctl.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_add_buffer`:

ibmvmc_add_buffer
=================

.. c:function:: int ibmvmc_add_buffer(struct crq_server_adapter *adapter, struct ibmvmc_crq_msg *crq)

    Add Buffer

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param struct ibmvmc_crq_msg \*crq:
        ibmvmc_crq_msg struct

.. _`ibmvmc_add_buffer.description`:

Description
-----------

This message transfers a buffer from hypervisor ownership to management
partition ownership. The LIOBA is obtained from the virtual TCE table
associated with the hypervisor side of the VMC device, and points to a
buffer of size MTU (as established in the capabilities exchange).

.. _`ibmvmc_add_buffer.typical-flow-for-ading-buffers`:

Typical flow for ading buffers
------------------------------

1. A new management application connection is opened by the management
partition.
2. The hypervisor assigns new buffers for the traffic associated with
that connection.
3. The hypervisor sends VMC Add Buffer messages to the management
partition, informing it of the new buffers.
4. The hypervisor sends an HMC protocol message (to the management
application) notifying it of the new buffers. This informs the
application that it has buffers available for sending HMC
commands.

.. _`ibmvmc_add_buffer.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_rem_buffer`:

ibmvmc_rem_buffer
=================

.. c:function:: int ibmvmc_rem_buffer(struct crq_server_adapter *adapter, struct ibmvmc_crq_msg *crq)

    Remove Buffer

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param struct ibmvmc_crq_msg \*crq:
        ibmvmc_crq_msg struct

.. _`ibmvmc_rem_buffer.description`:

Description
-----------

This message requests an HMC buffer to be transferred from management
partition ownership to hypervisor ownership. The management partition may
not be able to satisfy the request at a particular point in time if all its
buffers are in use. The management partition requires a depth of at least
one inbound buffer to allow management application commands to flow to the
hypervisor. It is, therefore, an interface error for the hypervisor to
attempt to remove the management partition's last buffer.

The hypervisor is expected to manage buffer usage with the management
application directly and inform the management partition when buffers may be
removed. The typical flow for removing buffers:

1. The management application no longer needs a communication path to a
particular hypervisor function. That function is closed.
2. The hypervisor and the management application quiesce all traffic to that
function. The hypervisor requests a reduction in buffer pool size.
3. The management application acknowledges the reduction in buffer pool size.
4. The hypervisor sends a Remove Buffer message to the management partition,
informing it of the reduction in buffers.
5. The management partition verifies it can remove the buffer. This is
possible if buffers have been quiesced.

.. _`ibmvmc_rem_buffer.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_process_capabilities`:

ibmvmc_process_capabilities
===========================

.. c:function:: void ibmvmc_process_capabilities(struct crq_server_adapter *adapter, struct ibmvmc_crq_msg *crqp)

    Process Capabilities

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param struct ibmvmc_crq_msg \*crqp:
        ibmvmc_crq_msg struct

.. _`ibmvmc_validate_hmc_session`:

ibmvmc_validate_hmc_session
===========================

.. c:function:: int ibmvmc_validate_hmc_session(struct crq_server_adapter *adapter, struct ibmvmc_crq_msg *crq)

    Validate HMC Session

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param struct ibmvmc_crq_msg \*crq:
        ibmvmc_crq_msg struct

.. _`ibmvmc_validate_hmc_session.return`:

Return
------

0 - Success
Non-zero - Failure

.. _`ibmvmc_reset`:

ibmvmc_reset
============

.. c:function:: void ibmvmc_reset(struct crq_server_adapter *adapter, bool xport_event)

    Reset

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param bool xport_event:
        If true, the partner closed their CRQ; we don't need to reset.
        If false, we need to schedule a CRQ reset.

.. _`ibmvmc_reset.description`:

Description
-----------

Closes all HMC sessions and conditionally schedules a CRQ reset.

.. _`ibmvmc_reset_task`:

ibmvmc_reset_task
=================

.. c:function:: int ibmvmc_reset_task(void *data)

    Reset Task

    :param void \*data:
        Data field

.. _`ibmvmc_reset_task.description`:

Description
-----------

Performs a CRQ reset of the VMC device in process context.

.. _`ibmvmc_reset_task.note`:

NOTE
----

This function should not be called directly, use ibmvmc_reset.

.. _`ibmvmc_process_open_resp`:

ibmvmc_process_open_resp
========================

.. c:function:: void ibmvmc_process_open_resp(struct ibmvmc_crq_msg *crq, struct crq_server_adapter *adapter)

    Process Open Response

    :param struct ibmvmc_crq_msg \*crq:
        ibmvmc_crq_msg struct

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

.. _`ibmvmc_process_open_resp.description`:

Description
-----------

This command is sent by the hypervisor in response to the Interface
Open message. When this message is received, the indicated buffer is
again available for management partition use.

.. _`ibmvmc_process_close_resp`:

ibmvmc_process_close_resp
=========================

.. c:function:: void ibmvmc_process_close_resp(struct ibmvmc_crq_msg *crq, struct crq_server_adapter *adapter)

    Process Close Response

    :param struct ibmvmc_crq_msg \*crq:
        ibmvmc_crq_msg struct

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

.. _`ibmvmc_process_close_resp.description`:

Description
-----------

This command is sent by the hypervisor in response to the managemant
application Interface Close message.

If the close fails, simply reset the entire driver as the state of the VMC
must be in tough shape.

.. _`ibmvmc_crq_process`:

ibmvmc_crq_process
==================

.. c:function:: void ibmvmc_crq_process(struct crq_server_adapter *adapter, struct ibmvmc_crq_msg *crq)

    Process CRQ

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

    :param struct ibmvmc_crq_msg \*crq:
        ibmvmc_crq_msg struct

.. _`ibmvmc_crq_process.description`:

Description
-----------

Process the CRQ message based upon the type of message received.

.. _`ibmvmc_handle_crq_init`:

ibmvmc_handle_crq_init
======================

.. c:function:: void ibmvmc_handle_crq_init(struct ibmvmc_crq_msg *crq, struct crq_server_adapter *adapter)

    Handle CRQ Init

    :param struct ibmvmc_crq_msg \*crq:
        ibmvmc_crq_msg struct

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

.. _`ibmvmc_handle_crq_init.description`:

Description
-----------

Handle the type of crq initialization based on whether
it is a message or a response.

.. _`ibmvmc_handle_crq`:

ibmvmc_handle_crq
=================

.. c:function:: void ibmvmc_handle_crq(struct ibmvmc_crq_msg *crq, struct crq_server_adapter *adapter)

    Handle CRQ

    :param struct ibmvmc_crq_msg \*crq:
        ibmvmc_crq_msg struct

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

.. _`ibmvmc_handle_crq.description`:

Description
-----------

Read the command elements from the command queue and execute the
requests based upon the type of crq message.

.. _`ibmvmc_init_crq_queue`:

ibmvmc_init_crq_queue
=====================

.. c:function:: int ibmvmc_init_crq_queue(struct crq_server_adapter *adapter)

    Init CRQ Queue

    :param struct crq_server_adapter \*adapter:
        crq_server_adapter struct

.. _`ibmvmc_init_crq_queue.return`:

Return
------

0 - Success
Non-zero - Failure

.. This file was automatic generated / don't edit.

