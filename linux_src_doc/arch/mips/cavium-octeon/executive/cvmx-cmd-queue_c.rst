.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/cvmx-cmd-queue.c

.. _`__cvmx_cmd_queue_init_state_ptr`:

\__cvmx_cmd_queue_init_state_ptr
================================

.. c:function:: cvmx_cmd_queue_result_t __cvmx_cmd_queue_init_state_ptr( void)

    :param void:
        no arguments
    :type void: 

.. _`__cvmx_cmd_queue_init_state_ptr.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code

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

.. This file was automatic generated / don't edit.

