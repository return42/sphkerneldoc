.. -*- coding: utf-8; mode: rst -*-

================
cvmx-cmd-queue.c
================


.. _`__cvmx_cmd_queue_init_state_ptr`:

__cvmx_cmd_queue_init_state_ptr
===============================

.. c:function:: cvmx_cmd_queue_result_t __cvmx_cmd_queue_init_state_ptr ( void)

    :param void:
        no arguments



.. _`__cvmx_cmd_queue_init_state_ptr.description`:

Description
-----------


Returns CVMX_CMD_QUEUE_SUCCESS or a failure code



.. _`cvmx_cmd_queue_initialize`:

cvmx_cmd_queue_initialize
=========================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_initialize (cvmx_cmd_queue_id_t queue_id, int max_depth, int fpa_pool, int pool_size)

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



.. _`cvmx_cmd_queue_initialize.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code



.. _`cvmx_cmd_queue_shutdown`:

cvmx_cmd_queue_shutdown
=======================

.. c:function:: cvmx_cmd_queue_result_t cvmx_cmd_queue_shutdown (cvmx_cmd_queue_id_t queue_id)

    :param cvmx_cmd_queue_id_t queue_id:
        Queue to shutdown



.. _`cvmx_cmd_queue_shutdown.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code



.. _`cvmx_cmd_queue_shutdown.description`:

Description
-----------

Returns CVMX_CMD_QUEUE_SUCCESS or a failure code



.. _`cvmx_cmd_queue_length`:

cvmx_cmd_queue_length
=====================

.. c:function:: int cvmx_cmd_queue_length (cvmx_cmd_queue_id_t queue_id)

    :param cvmx_cmd_queue_id_t queue_id:
        Hardware command queue to query



.. _`cvmx_cmd_queue_length.description`:

Description
-----------

Returns Number of outstanding commands



.. _`cvmx_cmd_queue_length.description`:

Description
-----------

Returns Number of outstanding commands



.. _`cvmx_cmd_queue_buffer`:

cvmx_cmd_queue_buffer
=====================

.. c:function:: void *cvmx_cmd_queue_buffer (cvmx_cmd_queue_id_t queue_id)

    :param cvmx_cmd_queue_id_t queue_id:
        Command queue to query



.. _`cvmx_cmd_queue_buffer.description`:

Description
-----------

Returns Command buffer or NULL on failure



.. _`cvmx_cmd_queue_buffer.description`:

Description
-----------

Returns Command buffer or NULL on failure

