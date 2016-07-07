.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-cmd-queue.h

.. _`cvmx_cmd_queue_enable_max_depth`:

CVMX_CMD_QUEUE_ENABLE_MAX_DEPTH
===============================

.. c:function::  CVMX_CMD_QUEUE_ENABLE_MAX_DEPTH()

    don't use it and it slows down the command queue processing significantly.

.. _`cvmx_cmd_queue_initialize`:

cvmx_cmd_queue_initialize
=========================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_initialize(cvmx_cmd_queue_id_t queue_id, int max_depth, int fpa_pool, int pool_size)

    allocated and the hardware unit is configured to point to the new command queue.

    :param cvmx_cmd_queue_id_t queue_id:
        Hardware command queue to initialize.

    :param int max_depth:
        Maximum outstanding commands that can be queued.

    :param int fpa_pool:
        FPA pool the command queues should come from.

    :param int pool_size:
        Size of each buffer in the FPA pool (bytes)

.. _`cvmx_cmd_queue_initialize.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. _`cvmx_cmd_queue_shutdown`:

cvmx_cmd_queue_shutdown
=======================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_shutdown(cvmx_cmd_queue_id_t queue_id)

    hardware connected to the queue must be stopped before this function is called.

    :param cvmx_cmd_queue_id_t queue_id:
        Queue to shutdown

.. _`cvmx_cmd_queue_shutdown.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. _`cvmx_cmd_queue_length`:

cvmx_cmd_queue_length
=====================

.. c:function:: int cvmx_cmd_queue_length(cvmx_cmd_queue_id_t queue_id)

    function may be relatively slow for some hardware units.

    :param cvmx_cmd_queue_id_t queue_id:
        Hardware command queue to query

.. _`cvmx_cmd_queue_length.description`:

Description
-----------

Returns Number of outstanding commands

.. _`cvmx_cmd_queue_buffer`:

cvmx_cmd_queue_buffer
=====================

.. c:function:: void *cvmx_cmd_queue_buffer(cvmx_cmd_queue_id_t queue_id)

    function is to allow CVMX routine access t othe low level buffer for initial hardware setup. User applications should not call this function directly.

    :param cvmx_cmd_queue_id_t queue_id:
        Command queue to query

.. _`cvmx_cmd_queue_buffer.description`:

Description
-----------

Returns Command buffer or NULL on failure

.. _`__cvmx_cmd_queue_get_index`:

__cvmx_cmd_queue_get_index
==========================

.. c:function:: int __cvmx_cmd_queue_get_index(cvmx_cmd_queue_id_t queue_id)

    :param cvmx_cmd_queue_id_t queue_id:
        Queue ID to get an index for

.. _`__cvmx_cmd_queue_get_index.description`:

Description
-----------

Returns Index into the state arrays

.. _`__cvmx_cmd_queue_lock`:

__cvmx_cmd_queue_lock
=====================

.. c:function:: void __cvmx_cmd_queue_lock(cvmx_cmd_queue_id_t queue_id, __cvmx_cmd_queue_state_t *qptr)

    time as us.

    :param cvmx_cmd_queue_id_t queue_id:
        Queue ID to lock

    :param __cvmx_cmd_queue_state_t \*qptr:
        Pointer to the queue's global state

.. _`__cvmx_cmd_queue_unlock`:

__cvmx_cmd_queue_unlock
=======================

.. c:function:: void __cvmx_cmd_queue_unlock(__cvmx_cmd_queue_state_t *qptr)

    :param __cvmx_cmd_queue_state_t \*qptr:
        Queue to unlock

.. _`__cvmx_cmd_queue_get_state`:

__cvmx_cmd_queue_get_state
==========================

.. c:function:: __cvmx_cmd_queue_state_t *__cvmx_cmd_queue_get_state(cvmx_cmd_queue_id_t queue_id)

    :param cvmx_cmd_queue_id_t queue_id:
        Queue id to get

.. _`__cvmx_cmd_queue_get_state.description`:

Description
-----------

Returns Queue structure or NULL on failure

.. _`cvmx_cmd_queue_write`:

cvmx_cmd_queue_write
====================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_write(cvmx_cmd_queue_id_t queue_id, int use_locking, int cmd_count, uint64_t *cmds)

    This is a generic function; the fixed number of command word functions yield higher performance.

    :param cvmx_cmd_queue_id_t queue_id:
        Hardware command queue to write to

    :param int use_locking:
        Use internal locking to ensure exclusive access for queue
        updates. If you don't use this locking you must ensure
        exclusivity some other way. Locking is strongly recommended.

    :param int cmd_count:
        Number of command words to write

    :param uint64_t \*cmds:
        Array of commands to write

.. _`cvmx_cmd_queue_write.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. _`cvmx_cmd_queue_write2`:

cvmx_cmd_queue_write2
=====================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_write2(cvmx_cmd_queue_id_t queue_id, int use_locking, uint64_t cmd1, uint64_t cmd2)

    queue.

    :param cvmx_cmd_queue_id_t queue_id:
        Hardware command queue to write to

    :param int use_locking:
        Use internal locking to ensure exclusive access for queue
        updates. If you don't use this locking you must ensure
        exclusivity some other way. Locking is strongly recommended.

    :param uint64_t cmd1:
        Command

    :param uint64_t cmd2:
        Command

.. _`cvmx_cmd_queue_write2.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. _`cvmx_cmd_queue_write3`:

cvmx_cmd_queue_write3
=====================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_write3(cvmx_cmd_queue_id_t queue_id, int use_locking, uint64_t cmd1, uint64_t cmd2, uint64_t cmd3)

    queue.

    :param cvmx_cmd_queue_id_t queue_id:
        Hardware command queue to write to

    :param int use_locking:
        Use internal locking to ensure exclusive access for queue
        updates. If you don't use this locking you must ensure
        exclusivity some other way. Locking is strongly recommended.

    :param uint64_t cmd1:
        Command

    :param uint64_t cmd2:
        Command

    :param uint64_t cmd3:
        Command

.. _`cvmx_cmd_queue_write3.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. This file was automatic generated / don't edit.

