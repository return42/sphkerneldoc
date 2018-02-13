.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/iucv/iucv.c

.. _`__iucv_call_b2f0`:

\__iucv_call_b2f0
=================

.. c:function:: int __iucv_call_b2f0(int command, union iucv_param *parm)

    :param int command:
        *undescribed*

    :param union iucv_param \*parm:
        pointer to a struct iucv_parm block

.. _`__iucv_call_b2f0.description`:

Description
-----------

Calls CP to execute IUCV commands.

Returns the result of the CP IUCV call.

.. _`__iucv_query_maxconn`:

\__iucv_query_maxconn
=====================

.. c:function:: int __iucv_query_maxconn(void *param, unsigned long *max_pathid)

    :param void \*param:
        *undescribed*

    :param unsigned long \*max_pathid:
        *undescribed*

.. _`__iucv_query_maxconn.description`:

Description
-----------

Determines the maximum number of connections that may be established.

Returns the maximum number of connections or -EPERM is IUCV is not
available.

.. _`iucv_allow_cpu`:

iucv_allow_cpu
==============

.. c:function:: void iucv_allow_cpu(void *data)

    :param void \*data:
        unused

.. _`iucv_allow_cpu.description`:

Description
-----------

Allow iucv interrupts on this cpu.

.. _`iucv_block_cpu`:

iucv_block_cpu
==============

.. c:function:: void iucv_block_cpu(void *data)

    :param void \*data:
        unused

.. _`iucv_block_cpu.description`:

Description
-----------

Block iucv interrupts on this cpu.

.. _`iucv_block_cpu_almost`:

iucv_block_cpu_almost
=====================

.. c:function:: void iucv_block_cpu_almost(void *data)

    :param void \*data:
        unused

.. _`iucv_block_cpu_almost.description`:

Description
-----------

Allow connection-severed interrupts only on this cpu.

.. _`iucv_declare_cpu`:

iucv_declare_cpu
================

.. c:function:: void iucv_declare_cpu(void *data)

    :param void \*data:
        unused

.. _`iucv_declare_cpu.description`:

Description
-----------

Declare a interrupt buffer on this cpu.

.. _`iucv_retrieve_cpu`:

iucv_retrieve_cpu
=================

.. c:function:: void iucv_retrieve_cpu(void *data)

    :param void \*data:
        unused

.. _`iucv_retrieve_cpu.description`:

Description
-----------

Retrieve interrupt buffer on this cpu.

.. _`iucv_setmask_mp`:

iucv_setmask_mp
===============

.. c:function:: void iucv_setmask_mp( void)

    :param  void:
        no arguments

.. _`iucv_setmask_mp.description`:

Description
-----------

Allow iucv interrupts on all cpus.

.. _`iucv_setmask_up`:

iucv_setmask_up
===============

.. c:function:: void iucv_setmask_up( void)

    :param  void:
        no arguments

.. _`iucv_setmask_up.description`:

Description
-----------

Allow iucv interrupts on a single cpu.

.. _`iucv_enable`:

iucv_enable
===========

.. c:function:: int iucv_enable( void)

    :param  void:
        no arguments

.. _`iucv_enable.description`:

Description
-----------

This function makes iucv ready for use. It allocates the pathid
table, declares an iucv interrupt buffer and enables the iucv
interrupts. Called when the first user has registered an iucv
handler.

.. _`iucv_disable`:

iucv_disable
============

.. c:function:: void iucv_disable( void)

    :param  void:
        no arguments

.. _`iucv_disable.description`:

Description
-----------

This function shuts down iucv. It disables iucv interrupts, retrieves
the iucv interrupt buffer and frees the pathid table. Called after the
last user unregister its iucv handler.

.. _`iucv_sever_pathid`:

iucv_sever_pathid
=================

.. c:function:: int iucv_sever_pathid(u16 pathid, u8 *userdata)

    :param u16 pathid:
        path identification number.

    :param u8 \*userdata:
        16-bytes of user data.

.. _`iucv_sever_pathid.description`:

Description
-----------

Sever an iucv path to free up the pathid. Used internally.

.. _`__iucv_cleanup_queue`:

\__iucv_cleanup_queue
=====================

.. c:function:: void __iucv_cleanup_queue(void *dummy)

    :param void \*dummy:
        unused dummy argument

.. _`__iucv_cleanup_queue.description`:

Description
-----------

Nop function called via smp_call_function to force work items from
pending external iucv interrupts to the work queue.

.. _`iucv_cleanup_queue`:

iucv_cleanup_queue
==================

.. c:function:: void iucv_cleanup_queue( void)

    :param  void:
        no arguments

.. _`iucv_cleanup_queue.description`:

Description
-----------

Function called after a path has been severed to find all remaining
work items for the now stale pathid. The caller needs to hold the
iucv_table_lock.

.. _`iucv_register`:

iucv_register
=============

.. c:function:: int iucv_register(struct iucv_handler *handler, int smp)

    :param struct iucv_handler \*handler:
        address of iucv handler structure

    :param int smp:
        != 0 indicates that the handler can deal with out of order messages

.. _`iucv_register.description`:

Description
-----------

Registers a driver with IUCV.

Returns 0 on success, -ENOMEM if the memory allocation for the pathid
table failed, or -EIO if IUCV_DECLARE_BUFFER failed on all cpus.

.. _`iucv_unregister`:

iucv_unregister
===============

.. c:function:: void iucv_unregister(struct iucv_handler *handler, int smp)

    :param struct iucv_handler \*handler:
        address of iucv handler structure

    :param int smp:
        != 0 indicates that the handler can deal with out of order messages

.. _`iucv_unregister.description`:

Description
-----------

Unregister driver from IUCV.

.. _`iucv_path_accept`:

iucv_path_accept
================

.. c:function:: int iucv_path_accept(struct iucv_path *path, struct iucv_handler *handler, u8 *userdata, void *private)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_handler \*handler:
        address of iucv handler structure

    :param u8 \*userdata:
        16 bytes of data reflected to the communication partner

    :param void \*private:
        private data passed to interrupt handlers for this path

.. _`iucv_path_accept.description`:

Description
-----------

This function is issued after the user received a connection pending
external interrupt and now wishes to complete the IUCV communication path.

Returns the result of the CP IUCV call.

.. _`iucv_path_connect`:

iucv_path_connect
=================

.. c:function:: int iucv_path_connect(struct iucv_path *path, struct iucv_handler *handler, u8 *userid, u8 *system, u8 *userdata, void *private)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_handler \*handler:
        address of iucv handler structure

    :param u8 \*userid:
        8-byte user identification

    :param u8 \*system:
        8-byte target system identification

    :param u8 \*userdata:
        16 bytes of data reflected to the communication partner

    :param void \*private:
        private data passed to interrupt handlers for this path

.. _`iucv_path_connect.description`:

Description
-----------

This function establishes an IUCV path. Although the connect may complete
successfully, you are not able to use the path until you receive an IUCV
Connection Complete external interrupt.

Returns the result of the CP IUCV call.

.. _`iucv_path_quiesce`:

iucv_path_quiesce
=================

.. c:function:: int iucv_path_quiesce(struct iucv_path *path, u8 *userdata)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param u8 \*userdata:
        16 bytes of data reflected to the communication partner

.. _`iucv_path_quiesce.description`:

Description
-----------

This function temporarily suspends incoming messages on an IUCV path.
You can later reactivate the path by invoking the iucv_resume function.

Returns the result from the CP IUCV call.

.. _`iucv_path_resume`:

iucv_path_resume
================

.. c:function:: int iucv_path_resume(struct iucv_path *path, u8 *userdata)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param u8 \*userdata:
        16 bytes of data reflected to the communication partner

.. _`iucv_path_resume.description`:

Description
-----------

This function resumes incoming messages on an IUCV path that has
been stopped with iucv_path_quiesce.

Returns the result from the CP IUCV call.

.. _`iucv_path_sever`:

iucv_path_sever
===============

.. c:function:: int iucv_path_sever(struct iucv_path *path, u8 *userdata)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param u8 \*userdata:
        16 bytes of data reflected to the communication partner

.. _`iucv_path_sever.description`:

Description
-----------

This function terminates an IUCV path.

Returns the result from the CP IUCV call.

.. _`iucv_message_purge`:

iucv_message_purge
==================

.. c:function:: int iucv_message_purge(struct iucv_path *path, struct iucv_message *msg, u32 srccls)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_message \*msg:
        address of iucv msg structure

    :param u32 srccls:
        source class of message

.. _`iucv_message_purge.description`:

Description
-----------

Cancels a message you have sent.

Returns the result from the CP IUCV call.

.. _`iucv_message_receive_iprmdata`:

iucv_message_receive_iprmdata
=============================

.. c:function:: int iucv_message_receive_iprmdata(struct iucv_path *path, struct iucv_message *msg, u8 flags, void *buffer, size_t size, size_t *residual)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_message \*msg:
        address of iucv msg structure

    :param u8 flags:
        how the message is received (IUCV_IPBUFLST)

    :param void \*buffer:
        address of data buffer or address of struct iucv_array

    :param size_t size:
        length of data buffer

    :param size_t \*residual:
        *undescribed*

.. _`iucv_message_receive_iprmdata.description`:

Description
-----------

Internal function used by iucv_message_receive and \__iucv_message_receive
to receive RMDATA data stored in struct iucv_message.

.. _`__iucv_message_receive`:

\__iucv_message_receive
=======================

.. c:function:: int __iucv_message_receive(struct iucv_path *path, struct iucv_message *msg, u8 flags, void *buffer, size_t size, size_t *residual)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_message \*msg:
        address of iucv msg structure

    :param u8 flags:
        how the message is received (IUCV_IPBUFLST)

    :param void \*buffer:
        address of data buffer or address of struct iucv_array

    :param size_t size:
        length of data buffer

    :param size_t \*residual:
        *undescribed*

.. _`__iucv_message_receive.description`:

Description
-----------

This function receives messages that are being sent to you over
established paths. This function will deal with RMDATA messages
embedded in struct iucv_message as well.

.. _`__iucv_message_receive.locking`:

Locking
-------

no locking

Returns the result from the CP IUCV call.

.. _`iucv_message_receive`:

iucv_message_receive
====================

.. c:function:: int iucv_message_receive(struct iucv_path *path, struct iucv_message *msg, u8 flags, void *buffer, size_t size, size_t *residual)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_message \*msg:
        address of iucv msg structure

    :param u8 flags:
        how the message is received (IUCV_IPBUFLST)

    :param void \*buffer:
        address of data buffer or address of struct iucv_array

    :param size_t size:
        length of data buffer

    :param size_t \*residual:
        *undescribed*

.. _`iucv_message_receive.description`:

Description
-----------

This function receives messages that are being sent to you over
established paths. This function will deal with RMDATA messages
embedded in struct iucv_message as well.

.. _`iucv_message_receive.locking`:

Locking
-------

local_bh_enable/local_bh_disable

Returns the result from the CP IUCV call.

.. _`iucv_message_reject`:

iucv_message_reject
===================

.. c:function:: int iucv_message_reject(struct iucv_path *path, struct iucv_message *msg)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_message \*msg:
        address of iucv msg structure

.. _`iucv_message_reject.description`:

Description
-----------

The reject function refuses a specified message. Between the time you
are notified of a message and the time that you complete the message,
the message may be rejected.

Returns the result from the CP IUCV call.

.. _`iucv_message_reply`:

iucv_message_reply
==================

.. c:function:: int iucv_message_reply(struct iucv_path *path, struct iucv_message *msg, u8 flags, void *reply, size_t size)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_message \*msg:
        address of iucv msg structure

    :param u8 flags:
        how the reply is sent (IUCV_IPRMDATA, IUCV_IPPRTY, IUCV_IPBUFLST)

    :param void \*reply:
        address of reply data buffer or address of struct iucv_array

    :param size_t size:
        length of reply data buffer

.. _`iucv_message_reply.description`:

Description
-----------

This function responds to the two-way messages that you receive. You
must identify completely the message to which you wish to reply. ie,
pathid, msgid, and trgcls. Prmmsg signifies the data is moved into
the parameter list.

Returns the result from the CP IUCV call.

.. _`__iucv_message_send`:

\__iucv_message_send
====================

.. c:function:: int __iucv_message_send(struct iucv_path *path, struct iucv_message *msg, u8 flags, u32 srccls, void *buffer, size_t size)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_message \*msg:
        address of iucv msg structure

    :param u8 flags:
        how the message is sent (IUCV_IPRMDATA, IUCV_IPPRTY, IUCV_IPBUFLST)

    :param u32 srccls:
        source class of message

    :param void \*buffer:
        address of send buffer or address of struct iucv_array

    :param size_t size:
        length of send buffer

.. _`__iucv_message_send.description`:

Description
-----------

This function transmits data to another application. Data to be
transmitted is in a buffer and this is a one-way message and the
receiver will not reply to the message.

.. _`__iucv_message_send.locking`:

Locking
-------

no locking

Returns the result from the CP IUCV call.

.. _`iucv_message_send`:

iucv_message_send
=================

.. c:function:: int iucv_message_send(struct iucv_path *path, struct iucv_message *msg, u8 flags, u32 srccls, void *buffer, size_t size)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_message \*msg:
        address of iucv msg structure

    :param u8 flags:
        how the message is sent (IUCV_IPRMDATA, IUCV_IPPRTY, IUCV_IPBUFLST)

    :param u32 srccls:
        source class of message

    :param void \*buffer:
        address of send buffer or address of struct iucv_array

    :param size_t size:
        length of send buffer

.. _`iucv_message_send.description`:

Description
-----------

This function transmits data to another application. Data to be
transmitted is in a buffer and this is a one-way message and the
receiver will not reply to the message.

.. _`iucv_message_send.locking`:

Locking
-------

local_bh_enable/local_bh_disable

Returns the result from the CP IUCV call.

.. _`iucv_message_send2way`:

iucv_message_send2way
=====================

.. c:function:: int iucv_message_send2way(struct iucv_path *path, struct iucv_message *msg, u8 flags, u32 srccls, void *buffer, size_t size, void *answer, size_t asize, size_t *residual)

    :param struct iucv_path \*path:
        address of iucv path structure

    :param struct iucv_message \*msg:
        address of iucv msg structure

    :param u8 flags:
        how the message is sent and the reply is received
        (IUCV_IPRMDATA, IUCV_IPBUFLST, IUCV_IPPRTY, IUCV_ANSLST)

    :param u32 srccls:
        source class of message

    :param void \*buffer:
        address of send buffer or address of struct iucv_array

    :param size_t size:
        length of send buffer

    :param void \*answer:
        *undescribed*

    :param size_t asize:
        size of reply buffer

    :param size_t \*residual:
        *undescribed*

.. _`iucv_message_send2way.description`:

Description
-----------

This function transmits data to another application. Data to be
transmitted is in a buffer. The receiver of the send is expected to
reply to the message and a buffer is provided into which IUCV moves
the reply to this message.

Returns the result from the CP IUCV call.

.. _`iucv_tasklet_fn`:

iucv_tasklet_fn
===============

.. c:function:: void iucv_tasklet_fn(unsigned long ignored)

    :param unsigned long ignored:
        *undescribed*

.. _`iucv_tasklet_fn.description`:

Description
-----------

This tasklet loops over the queue of irq buffers created by
iucv_external_interrupt, calls the appropriate action handler
and then frees the buffer.

.. _`iucv_work_fn`:

iucv_work_fn
============

.. c:function:: void iucv_work_fn(struct work_struct *work)

    :param struct work_struct \*work:
        *undescribed*

.. _`iucv_work_fn.description`:

Description
-----------

This work function loops over the queue of path pending irq blocks
created by iucv_external_interrupt, calls the appropriate action
handler and then frees the buffer.

.. _`iucv_external_interrupt`:

iucv_external_interrupt
=======================

.. c:function:: void iucv_external_interrupt(struct ext_code ext_code, unsigned int param32, unsigned long param64)

    :param struct ext_code ext_code:
        *undescribed*

    :param unsigned int param32:
        *undescribed*

    :param unsigned long param64:
        *undescribed*

.. _`iucv_external_interrupt.description`:

Description
-----------

Handles external interrupts coming in from CP.
Places the interrupt buffer on a queue and schedules \ :c:func:`iucv_tasklet_fn`\ .

.. _`iucv_path_table_empty`:

iucv_path_table_empty
=====================

.. c:function:: int iucv_path_table_empty( void)

    determine if iucv path table is empty

    :param  void:
        no arguments

.. _`iucv_path_table_empty.description`:

Description
-----------

Returns 0 if there are still iucv pathes defined
1 if there are no iucv pathes defined

.. _`iucv_pm_freeze`:

iucv_pm_freeze
==============

.. c:function:: int iucv_pm_freeze(struct device *dev)

    Freeze PM callback

    :param struct device \*dev:
        iucv-based device

.. _`iucv_pm_freeze.description`:

Description
-----------

disable iucv interrupts
invoke callback function of the iucv-based driver
shut down iucv, if no iucv-pathes are established anymore

.. _`iucv_pm_thaw`:

iucv_pm_thaw
============

.. c:function:: int iucv_pm_thaw(struct device *dev)

    Thaw PM callback

    :param struct device \*dev:
        iucv-based device

.. _`iucv_pm_thaw.make-iucv-ready-for-use-again`:

make iucv ready for use again
-----------------------------

allocate path table, declare interrupt buffers
and enable iucv interrupts
invoke callback function of the iucv-based driver

.. _`iucv_pm_restore`:

iucv_pm_restore
===============

.. c:function:: int iucv_pm_restore(struct device *dev)

    Restore PM callback

    :param struct device \*dev:
        iucv-based device

.. _`iucv_pm_restore.make-iucv-ready-for-use-again`:

make iucv ready for use again
-----------------------------

allocate path table, declare interrupt buffers
and enable iucv interrupts
invoke callback function of the iucv-based driver

.. _`iucv_init`:

iucv_init
=========

.. c:function:: int iucv_init( void)

    :param  void:
        no arguments

.. _`iucv_init.description`:

Description
-----------

Allocates and initializes various data structures.

.. _`iucv_exit`:

iucv_exit
=========

.. c:function:: void __exit iucv_exit( void)

    :param  void:
        no arguments

.. _`iucv_exit.description`:

Description
-----------

Frees everything allocated from iucv_init.

.. This file was automatic generated / don't edit.

