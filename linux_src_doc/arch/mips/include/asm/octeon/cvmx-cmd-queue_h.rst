.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-cmd-queue.h

.. _`cvmx_cmd_queue_enable_max_depth`:

CVMX_CMD_QUEUE_ENABLE_MAX_DEPTH
===============================

.. c:function::  CVMX_CMD_QUEUE_ENABLE_MAX_DEPTH()

    don't use it and it slows down the command queue processing significantly.

.. _`cvmx_cmd_queue_id_t`:

typedef cvmx_cmd_queue_id_t
===========================

.. c:type:: typedef cvmx_cmd_queue_id_t

    queues. Each hardware block has up to 65536 sub identifiers for multiple command queues. Not all chips support all hardware units.

.. _`cvmx_cmd_queue_result_t`:

typedef cvmx_cmd_queue_result_t
===============================

.. c:type:: typedef cvmx_cmd_queue_result_t

    a new buffer and the associated FPA pool is empty. It can also fail if the number of queued command words reaches the maximum set at initialization.

.. _`__cvmx_cmd_queue_all_state_t`:

typedef \__cvmx_cmd_queue_all_state_t
=====================================

.. c:type:: typedef __cvmx_cmd_queue_all_state_t

    It is stored in a bootmem named block and shared by all applications running on Octeon. Tickets are stored in a differnet cache line that queue information to reduce the contention on the ll/sc used to get a ticket. If this is not the case, the update of queue state causes the ll/sc to fail quite often.

.. _`cvmx_cmd_queue_initialize`:

cvmx_cmd_queue_initialize
=========================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_initialize(cvmx_cmd_queue_id_t queue_id, int max_depth, int fpa_pool, int pool_size)

    allocated and the hardware unit is configured to point to the new command queue.

    :param queue_id:
        Hardware command queue to initialize.
    :type queue_id: cvmx_cmd_queue_id_t

    :param max_depth:
        Maximum outstanding commands that can be queued.
    :type max_depth: int

    :param fpa_pool:
        FPA pool the command queues should come from.
    :type fpa_pool: int

    :param pool_size:
        Size of each buffer in the FPA pool (bytes)
    :type pool_size: int

.. _`cvmx_cmd_queue_initialize.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. _`cvmx_cmd_queue_shutdown`:

cvmx_cmd_queue_shutdown
=======================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_shutdown(cvmx_cmd_queue_id_t queue_id)

    hardware connected to the queue must be stopped before this function is called.

    :param queue_id:
        Queue to shutdown
    :type queue_id: cvmx_cmd_queue_id_t

.. _`cvmx_cmd_queue_shutdown.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. _`cvmx_cmd_queue_length`:

cvmx_cmd_queue_length
=====================

.. c:function:: int cvmx_cmd_queue_length(cvmx_cmd_queue_id_t queue_id)

    function may be relatively slow for some hardware units.

    :param queue_id:
        Hardware command queue to query
    :type queue_id: cvmx_cmd_queue_id_t

.. _`cvmx_cmd_queue_length.description`:

Description
-----------

Returns Number of outstanding commands

.. _`cvmx_cmd_queue_buffer`:

cvmx_cmd_queue_buffer
=====================

.. c:function:: void *cvmx_cmd_queue_buffer(cvmx_cmd_queue_id_t queue_id)

    function is to allow CVMX routine access t othe low level buffer for initial hardware setup. User applications should not call this function directly.

    :param queue_id:
        Command queue to query
    :type queue_id: cvmx_cmd_queue_id_t

.. _`cvmx_cmd_queue_buffer.description`:

Description
-----------

Returns Command buffer or NULL on failure

.. _`__cvmx_cmd_queue_get_index`:

\__cvmx_cmd_queue_get_index
===========================

.. c:function:: int __cvmx_cmd_queue_get_index(cvmx_cmd_queue_id_t queue_id)

    :param queue_id:
        Queue ID to get an index for
    :type queue_id: cvmx_cmd_queue_id_t

.. _`__cvmx_cmd_queue_get_index.description`:

Description
-----------

Returns Index into the state arrays

.. _`__cvmx_cmd_queue_lock`:

\__cvmx_cmd_queue_lock
======================

.. c:function:: void __cvmx_cmd_queue_lock(cvmx_cmd_queue_id_t queue_id, __cvmx_cmd_queue_state_t *qptr)

    time as us.

    :param queue_id:
        Queue ID to lock
    :type queue_id: cvmx_cmd_queue_id_t

    :param qptr:
        Pointer to the queue's global state
    :type qptr: __cvmx_cmd_queue_state_t \*

.. _`__cvmx_cmd_queue_unlock`:

\__cvmx_cmd_queue_unlock
========================

.. c:function:: void __cvmx_cmd_queue_unlock(__cvmx_cmd_queue_state_t *qptr)

    :param qptr:
        Queue to unlock
    :type qptr: __cvmx_cmd_queue_state_t \*

.. _`__cvmx_cmd_queue_get_state`:

\__cvmx_cmd_queue_get_state
===========================

.. c:function:: __cvmx_cmd_queue_state_t *__cvmx_cmd_queue_get_state(cvmx_cmd_queue_id_t queue_id)

    :param queue_id:
        Queue id to get
    :type queue_id: cvmx_cmd_queue_id_t

.. _`__cvmx_cmd_queue_get_state.description`:

Description
-----------

Returns Queue structure or NULL on failure

.. _`cvmx_cmd_queue_write`:

cvmx_cmd_queue_write
====================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_write(cvmx_cmd_queue_id_t queue_id, int use_locking, int cmd_count, uint64_t *cmds)

    This is a generic function; the fixed number of command word functions yield higher performance.

    :param queue_id:
        Hardware command queue to write to
    :type queue_id: cvmx_cmd_queue_id_t

    :param use_locking:
        Use internal locking to ensure exclusive access for queue
        updates. If you don't use this locking you must ensure
        exclusivity some other way. Locking is strongly recommended.
    :type use_locking: int

    :param cmd_count:
        Number of command words to write
    :type cmd_count: int

    :param cmds:
        Array of commands to write
    :type cmds: uint64_t \*

.. _`cvmx_cmd_queue_write.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. _`cvmx_cmd_queue_write2`:

cvmx_cmd_queue_write2
=====================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_write2(cvmx_cmd_queue_id_t queue_id, int use_locking, uint64_t cmd1, uint64_t cmd2)

    queue.

    :param queue_id:
        Hardware command queue to write to
    :type queue_id: cvmx_cmd_queue_id_t

    :param use_locking:
        Use internal locking to ensure exclusive access for queue
        updates. If you don't use this locking you must ensure
        exclusivity some other way. Locking is strongly recommended.
    :type use_locking: int

    :param cmd1:
        Command
    :type cmd1: uint64_t

    :param cmd2:
        Command
    :type cmd2: uint64_t

.. _`cvmx_cmd_queue_write2.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. _`cvmx_cmd_queue_write3`:

cvmx_cmd_queue_write3
=====================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_write3(cvmx_cmd_queue_id_t queue_id, int use_locking, uint64_t cmd1, uint64_t cmd2, uint64_t cmd3)

    queue.

    :param queue_id:
        Hardware command queue to write to
    :type queue_id: cvmx_cmd_queue_id_t

    :param use_locking:
        Use internal locking to ensure exclusive access for queue
        updates. If you don't use this locking you must ensure
        exclusivity some other way. Locking is strongly recommended.
    :type use_locking: int

    :param cmd1:
        Command
    :type cmd1: uint64_t

    :param cmd2:
        Command
    :type cmd2: uint64_t

    :param cmd3:
        Command
    :type cmd3: uint64_t

.. _`cvmx_cmd_queue_write3.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

.. This file was automatic generated / don't edit.

