.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/qcom_scm-32.c

.. _`qcom_scm_command`:

struct qcom_scm_command
=======================

.. c:type:: struct qcom_scm_command

    one SCM command buffer

.. _`qcom_scm_command.definition`:

Definition
----------

.. code-block:: c

    struct qcom_scm_command {
        __le32 len;
        __le32 buf_offset;
        __le32 resp_hdr_offset;
        __le32 id;
        __le32 buf[0];
    }

.. _`qcom_scm_command.members`:

Members
-------

len
    total available memory for command and response

buf_offset
    start of command buffer

resp_hdr_offset
    start of response buffer

id
    command to be executed

buf
    buffer returned from \ :c:func:`qcom_scm_get_command_buffer`\ 

.. _`qcom_scm_command.an-scm-command-is-laid-out-in-memory-as-follows`:

An SCM command is laid out in memory as follows
-----------------------------------------------


------------------- <--- struct qcom_scm_command
\| command header  \|
------------------- <--- \ :c:func:`qcom_scm_get_command_buffer`\ 
\| command buffer  \|
------------------- <--- struct qcom_scm_response and
\| response header \|      \ :c:func:`qcom_scm_command_to_response`\ 
------------------- <--- \ :c:func:`qcom_scm_get_response_buffer`\ 
\| response buffer \|
-------------------

There can be arbitrary padding between the headers and buffers so
you should always use the appropriate qcom_scm_get\_\*\\ :c:func:`_buffer`\  routines
to access the buffers in a safe manner.

.. _`qcom_scm_response`:

struct qcom_scm_response
========================

.. c:type:: struct qcom_scm_response

    one SCM response buffer

.. _`qcom_scm_response.definition`:

Definition
----------

.. code-block:: c

    struct qcom_scm_response {
        __le32 len;
        __le32 buf_offset;
        __le32 is_complete;
    }

.. _`qcom_scm_response.members`:

Members
-------

len
    total available memory for response

buf_offset
    start of response data relative to start of qcom_scm_response

is_complete
    indicates if the command has finished processing

.. _`alloc_qcom_scm_command`:

alloc_qcom_scm_command
======================

.. c:function:: struct qcom_scm_command *alloc_qcom_scm_command(size_t cmd_size, size_t resp_size)

    Allocate an SCM command

    :param size_t cmd_size:
        size of the command buffer

    :param size_t resp_size:
        size of the response buffer

.. _`alloc_qcom_scm_command.description`:

Description
-----------

Allocate an SCM command, including enough room for the command
and response headers as well as the command and response buffers.

Returns a valid \ :c:type:`struct qcom_scm_command <qcom_scm_command>` on success or \ ``NULL``\  if the allocation fails.

.. _`free_qcom_scm_command`:

free_qcom_scm_command
=====================

.. c:function:: void free_qcom_scm_command(struct qcom_scm_command *cmd)

    Free an SCM command

    :param struct qcom_scm_command \*cmd:
        command to free

.. _`free_qcom_scm_command.description`:

Description
-----------

Free an SCM command.

.. _`qcom_scm_command_to_response`:

qcom_scm_command_to_response
============================

.. c:function:: struct qcom_scm_response *qcom_scm_command_to_response(const struct qcom_scm_command *cmd)

    Get a pointer to a qcom_scm_response

    :param const struct qcom_scm_command \*cmd:
        command

.. _`qcom_scm_command_to_response.description`:

Description
-----------

Returns a pointer to a response for a command.

.. _`qcom_scm_get_command_buffer`:

qcom_scm_get_command_buffer
===========================

.. c:function:: void *qcom_scm_get_command_buffer(const struct qcom_scm_command *cmd)

    Get a pointer to a command buffer

    :param const struct qcom_scm_command \*cmd:
        command

.. _`qcom_scm_get_command_buffer.description`:

Description
-----------

Returns a pointer to the command buffer of a command.

.. _`qcom_scm_get_response_buffer`:

qcom_scm_get_response_buffer
============================

.. c:function:: void *qcom_scm_get_response_buffer(const struct qcom_scm_response *rsp)

    Get a pointer to a response buffer

    :param const struct qcom_scm_response \*rsp:
        response

.. _`qcom_scm_get_response_buffer.description`:

Description
-----------

Returns a pointer to a response buffer of a response.

.. _`qcom_scm_call`:

qcom_scm_call
=============

.. c:function:: int qcom_scm_call(u32 svc_id, u32 cmd_id, const void *cmd_buf, size_t cmd_len, void *resp_buf, size_t resp_len)

    Send an SCM command

    :param u32 svc_id:
        service identifier

    :param u32 cmd_id:
        command identifier

    :param const void \*cmd_buf:
        command buffer

    :param size_t cmd_len:
        length of the command buffer

    :param void \*resp_buf:
        response buffer

    :param size_t resp_len:
        length of the response buffer

.. _`qcom_scm_call.description`:

Description
-----------

Sends a command to the SCM and waits for the command to finish processing.

.. _`qcom_scm_call.a-note-on-cache-maintenance`:

A note on cache maintenance
---------------------------

Note that any buffers that are expected to be accessed by the secure world
must be flushed before invoking qcom_scm_call and invalidated in the cache
immediately after qcom_scm_call returns. Cache maintenance on the command
and response buffers is taken care of by qcom_scm_call; however, callers are
responsible for any other cached buffers passed over to the secure world.

.. _`qcom_scm_call_atomic1`:

qcom_scm_call_atomic1
=====================

.. c:function:: s32 qcom_scm_call_atomic1(u32 svc, u32 cmd, u32 arg1)

    Send an atomic SCM command with one argument

    :param u32 svc:
        *undescribed*

    :param u32 cmd:
        *undescribed*

    :param u32 arg1:
        first argument

.. _`qcom_scm_call_atomic1.description`:

Description
-----------

This shall only be used with commands that are guaranteed to be
uninterruptable, atomic and SMP safe.

.. _`__qcom_scm_set_cold_boot_addr`:

__qcom_scm_set_cold_boot_addr
=============================

.. c:function:: int __qcom_scm_set_cold_boot_addr(void *entry, const cpumask_t *cpus)

    Set the cold boot address for cpus

    :param void \*entry:
        Entry point function for the cpus

    :param const cpumask_t \*cpus:
        The cpumask of cpus that will use the entry point

.. _`__qcom_scm_set_cold_boot_addr.description`:

Description
-----------

Set the cold boot address of the cpus. Any cpu outside the supported
range would be removed from the cpu present mask.

.. _`__qcom_scm_set_warm_boot_addr`:

__qcom_scm_set_warm_boot_addr
=============================

.. c:function:: int __qcom_scm_set_warm_boot_addr(void *entry, const cpumask_t *cpus)

    Set the warm boot address for cpus

    :param void \*entry:
        Entry point function for the cpus

    :param const cpumask_t \*cpus:
        The cpumask of cpus that will use the entry point

.. _`__qcom_scm_set_warm_boot_addr.description`:

Description
-----------

Set the Linux entry point for the SCM to transfer control to when coming
out of a power down. CPU power down may be executed on cpuidle or hotplug.

.. _`__qcom_scm_cpu_power_down`:

__qcom_scm_cpu_power_down
=========================

.. c:function:: void __qcom_scm_cpu_power_down(u32 flags)

    Power down the cpu \ ``flags``\  - Flags to flush cache

    :param u32 flags:
        *undescribed*

.. _`__qcom_scm_cpu_power_down.description`:

Description
-----------

This is an end point to power down cpu. If there was a pending interrupt,
the control would return from this function, otherwise, the cpu jumps to the
warm boot entry point set for this cpu upon reset.

.. This file was automatic generated / don't edit.

