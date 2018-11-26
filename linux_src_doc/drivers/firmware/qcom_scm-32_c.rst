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
you should always use the appropriate qcom_scm_get\_\*\_buffer() routines
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

.. _`qcom_scm_command_to_response`:

qcom_scm_command_to_response
============================

.. c:function:: struct qcom_scm_response *qcom_scm_command_to_response(const struct qcom_scm_command *cmd)

    Get a pointer to a qcom_scm_response

    :param cmd:
        command
    :type cmd: const struct qcom_scm_command \*

.. _`qcom_scm_command_to_response.description`:

Description
-----------

Returns a pointer to a response for a command.

.. _`qcom_scm_get_command_buffer`:

qcom_scm_get_command_buffer
===========================

.. c:function:: void *qcom_scm_get_command_buffer(const struct qcom_scm_command *cmd)

    Get a pointer to a command buffer

    :param cmd:
        command
    :type cmd: const struct qcom_scm_command \*

.. _`qcom_scm_get_command_buffer.description`:

Description
-----------

Returns a pointer to the command buffer of a command.

.. _`qcom_scm_get_response_buffer`:

qcom_scm_get_response_buffer
============================

.. c:function:: void *qcom_scm_get_response_buffer(const struct qcom_scm_response *rsp)

    Get a pointer to a response buffer

    :param rsp:
        response
    :type rsp: const struct qcom_scm_response \*

.. _`qcom_scm_get_response_buffer.description`:

Description
-----------

Returns a pointer to a response buffer of a response.

.. _`qcom_scm_call`:

qcom_scm_call
=============

.. c:function:: int qcom_scm_call(struct device *dev, u32 svc_id, u32 cmd_id, const void *cmd_buf, size_t cmd_len, void *resp_buf, size_t resp_len)

    Send an SCM command

    :param dev:
        struct device
    :type dev: struct device \*

    :param svc_id:
        service identifier
    :type svc_id: u32

    :param cmd_id:
        command identifier
    :type cmd_id: u32

    :param cmd_buf:
        command buffer
    :type cmd_buf: const void \*

    :param cmd_len:
        length of the command buffer
    :type cmd_len: size_t

    :param resp_buf:
        response buffer
    :type resp_buf: void \*

    :param resp_len:
        length of the response buffer
    :type resp_len: size_t

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

    :param svc:
        *undescribed*
    :type svc: u32

    :param cmd:
        *undescribed*
    :type cmd: u32

    :param arg1:
        first argument
    :type arg1: u32

.. _`qcom_scm_call_atomic1.description`:

Description
-----------

This shall only be used with commands that are guaranteed to be
uninterruptable, atomic and SMP safe.

.. _`qcom_scm_call_atomic2`:

qcom_scm_call_atomic2
=====================

.. c:function:: s32 qcom_scm_call_atomic2(u32 svc, u32 cmd, u32 arg1, u32 arg2)

    Send an atomic SCM command with two arguments

    :param svc:
        *undescribed*
    :type svc: u32

    :param cmd:
        *undescribed*
    :type cmd: u32

    :param arg1:
        first argument
    :type arg1: u32

    :param arg2:
        second argument
    :type arg2: u32

.. _`qcom_scm_call_atomic2.description`:

Description
-----------

This shall only be used with commands that are guaranteed to be
uninterruptable, atomic and SMP safe.

.. _`__qcom_scm_set_cold_boot_addr`:

\__qcom_scm_set_cold_boot_addr
==============================

.. c:function:: int __qcom_scm_set_cold_boot_addr(void *entry, const cpumask_t *cpus)

    Set the cold boot address for cpus

    :param entry:
        Entry point function for the cpus
    :type entry: void \*

    :param cpus:
        The cpumask of cpus that will use the entry point
    :type cpus: const cpumask_t \*

.. _`__qcom_scm_set_cold_boot_addr.description`:

Description
-----------

Set the cold boot address of the cpus. Any cpu outside the supported
range would be removed from the cpu present mask.

.. _`__qcom_scm_set_warm_boot_addr`:

\__qcom_scm_set_warm_boot_addr
==============================

.. c:function:: int __qcom_scm_set_warm_boot_addr(struct device *dev, void *entry, const cpumask_t *cpus)

    Set the warm boot address for cpus

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param entry:
        Entry point function for the cpus
    :type entry: void \*

    :param cpus:
        The cpumask of cpus that will use the entry point
    :type cpus: const cpumask_t \*

.. _`__qcom_scm_set_warm_boot_addr.description`:

Description
-----------

Set the Linux entry point for the SCM to transfer control to when coming
out of a power down. CPU power down may be executed on cpuidle or hotplug.

.. _`__qcom_scm_cpu_power_down`:

\__qcom_scm_cpu_power_down
==========================

.. c:function:: void __qcom_scm_cpu_power_down(u32 flags)

    Power down the cpu \ ``flags``\  - Flags to flush cache

    :param flags:
        *undescribed*
    :type flags: u32

.. _`__qcom_scm_cpu_power_down.description`:

Description
-----------

This is an end point to power down cpu. If there was a pending interrupt,
the control would return from this function, otherwise, the cpu jumps to the
warm boot entry point set for this cpu upon reset.

.. This file was automatic generated / don't edit.

