.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-pko.h

.. _`cvmx_pko_lock_t`:

typedef cvmx_pko_lock_t
=======================

.. c:type:: typedef cvmx_pko_lock_t


.. _`cvmx_pko_doorbell_address_t`:

typedef cvmx_pko_doorbell_address_t
===================================

.. c:type:: typedef cvmx_pko_doorbell_address_t


.. _`cvmx_pko_command_word0_t`:

typedef cvmx_pko_command_word0_t
================================

.. c:type:: typedef cvmx_pko_command_word0_t


.. _`cvmx_pko_state_elem_t`:

typedef cvmx_pko_state_elem_t
=============================

.. c:type:: typedef cvmx_pko_state_elem_t


.. _`cvmx_pko_initialize_global`:

cvmx_pko_initialize_global
==========================

.. c:function:: void cvmx_pko_initialize_global( void)

    output system.

    :param void:
        no arguments
    :type void: 

.. _`cvmx_pko_enable`:

cvmx_pko_enable
===============

.. c:function:: void cvmx_pko_enable( void)

    configured.

    :param void:
        no arguments
    :type void: 

.. _`cvmx_pko_disable`:

cvmx_pko_disable
================

.. c:function:: void cvmx_pko_disable( void)

    :param void:
        no arguments
    :type void: 

.. _`cvmx_pko_shutdown`:

cvmx_pko_shutdown
=================

.. c:function:: void cvmx_pko_shutdown( void)

    :param void:
        no arguments
    :type void: 

.. _`cvmx_pko_config_port`:

cvmx_pko_config_port
====================

.. c:function:: cvmx_pko_status_t cvmx_pko_config_port(uint64_t port, uint64_t base_queue, uint64_t num_queues, const uint64_t priority)

    :param port:
        Port to configure.
    :type port: uint64_t

    :param base_queue:
        First queue number to associate with this port.
    :type base_queue: uint64_t

    :param num_queues:
        Number of queues t oassociate with this port
    :type num_queues: uint64_t

    :param priority:
        Array of priority levels for each queue. Values are
        allowed to be 1-8. A value of 8 get 8 times the traffic
        of a value of 1. There must be num_queues elements in the
        array.
    :type priority: const uint64_t

.. _`cvmx_pko_doorbell`:

cvmx_pko_doorbell
=================

.. c:function:: void cvmx_pko_doorbell(uint64_t port, uint64_t queue, uint64_t len)

    output hardware that "len" command words have been added to its pending list.  This command includes the required CVMX_SYNCWS before the doorbell ring.

    :param port:
        Port the packet is for
    :type port: uint64_t

    :param queue:
        Queue the packet is for
    :type queue: uint64_t

    :param len:
        Length of the command in 64 bit words
    :type len: uint64_t

.. _`cvmx_pko_send_packet_prepare`:

cvmx_pko_send_packet_prepare
============================

.. c:function:: void cvmx_pko_send_packet_prepare(uint64_t port, uint64_t queue, cvmx_pko_lock_t use_locking)

    get exclusive access to the output queue structure, and performs other prep work for the packet send operation.

    :param port:
        Port to send it on
    :type port: uint64_t

    :param queue:
        Queue to use
    :type queue: uint64_t

    :param use_locking:
        CVMX_PKO_LOCK_NONE, CVMX_PKO_LOCK_ATOMIC_TAG, or
        CVMX_PKO_LOCK_CMD_QUEUE
    :type use_locking: cvmx_pko_lock_t

.. _`cvmx_pko_send_packet_prepare.description`:

Description
-----------

\ :c:func:`cvmx_pko_send_packet_finish`\  MUST be called after this function is called,
and must be called with the same port/queue/use_locking arguments.

The use_locking parameter allows the caller to use three
possible locking modes.
- CVMX_PKO_LOCK_NONE
- PKO doesn't do any locking. It is the responsibility
of the application to make sure that no other core
is accessing the same queue at the same time.
- CVMX_PKO_LOCK_ATOMIC_TAG
- PKO performs an atomic tagswitch to insure exclusive
access to the output queue. This will maintain
packet ordering on output.
- CVMX_PKO_LOCK_CMD_QUEUE
- PKO uses the common command queue locks to insure
exclusive access to the output queue. This is a
memory based ll/sc. This is the most portable
locking mechanism.

.. _`cvmx_pko_send_packet_prepare.note`:

NOTE
----

If atomic locking is used, the POW entry CANNOT be
descheduled, as it does not contain a valid WQE pointer.

.. _`cvmx_pko_send_packet_finish`:

cvmx_pko_send_packet_finish
===========================

.. c:function:: cvmx_pko_status_t cvmx_pko_send_packet_finish(uint64_t port, uint64_t queue, cvmx_pko_command_word0_t pko_command, union cvmx_buf_ptr packet, cvmx_pko_lock_t use_locking)

    called exactly once before this, and the same parameters must be passed to both \ :c:func:`cvmx_pko_send_packet_prepare`\  and \ :c:func:`cvmx_pko_send_packet_finish`\ .

    :param port:
        Port to send it on
    :type port: uint64_t

    :param queue:
        Queue to use
    :type queue: uint64_t

    :param pko_command:
        PKO HW command word
    :type pko_command: cvmx_pko_command_word0_t

    :param packet:
        Packet to send
    :type packet: union cvmx_buf_ptr

    :param use_locking:
        CVMX_PKO_LOCK_NONE, CVMX_PKO_LOCK_ATOMIC_TAG, or
        CVMX_PKO_LOCK_CMD_QUEUE
    :type use_locking: cvmx_pko_lock_t

.. _`cvmx_pko_send_packet_finish.description`:

Description
-----------

Returns returns CVMX_PKO_SUCCESS on success, or error code on
failure of output

.. _`cvmx_pko_send_packet_finish3`:

cvmx_pko_send_packet_finish3
============================

.. c:function:: cvmx_pko_status_t cvmx_pko_send_packet_finish3(uint64_t port, uint64_t queue, cvmx_pko_command_word0_t pko_command, union cvmx_buf_ptr packet, uint64_t addr, cvmx_pko_lock_t use_locking)

    called exactly once before this, and the same parameters must be passed to both \ :c:func:`cvmx_pko_send_packet_prepare`\  and \ :c:func:`cvmx_pko_send_packet_finish`\ .

    :param port:
        Port to send it on
    :type port: uint64_t

    :param queue:
        Queue to use
    :type queue: uint64_t

    :param pko_command:
        PKO HW command word
    :type pko_command: cvmx_pko_command_word0_t

    :param packet:
        Packet to send
    :type packet: union cvmx_buf_ptr

    :param addr:
        Plysical address of a work queue entry or physical address
        to zero on complete.
    :type addr: uint64_t

    :param use_locking:
        CVMX_PKO_LOCK_NONE, CVMX_PKO_LOCK_ATOMIC_TAG, or
        CVMX_PKO_LOCK_CMD_QUEUE
    :type use_locking: cvmx_pko_lock_t

.. _`cvmx_pko_send_packet_finish3.description`:

Description
-----------

Returns returns CVMX_PKO_SUCCESS on success, or error code on
failure of output

.. _`cvmx_pko_get_base_queue_per_core`:

cvmx_pko_get_base_queue_per_core
================================

.. c:function:: int cvmx_pko_get_base_queue_per_core(int port, int core)

    In normal mode (PKO lockless operation is disabled), the value returned is the base queue.

    :param port:
        Port number
    :type port: int

    :param core:
        Core to get queue for
    :type core: int

.. _`cvmx_pko_get_base_queue_per_core.description`:

Description
-----------

Returns Core-specific output queue

.. _`cvmx_pko_get_base_queue`:

cvmx_pko_get_base_queue
=======================

.. c:function:: int cvmx_pko_get_base_queue(int port)

    for the port.

    :param port:
        Port number
        Returns Base output queue
    :type port: int

.. _`cvmx_pko_get_num_queues`:

cvmx_pko_get_num_queues
=======================

.. c:function:: int cvmx_pko_get_num_queues(int port)

    :param port:
        Port number
        Returns Number of output queues
    :type port: int

.. _`cvmx_pko_get_port_status`:

cvmx_pko_get_port_status
========================

.. c:function:: void cvmx_pko_get_port_status(uint64_t port_num, uint64_t clear, cvmx_pko_port_status_t *status)

    :param port_num:
        Port number to get statistics for.
    :type port_num: uint64_t

    :param clear:
        Set to 1 to clear the counters after they are read
    :type clear: uint64_t

    :param status:
        Where to put the results.
    :type status: cvmx_pko_port_status_t \*

.. _`cvmx_pko_rate_limit_packets`:

cvmx_pko_rate_limit_packets
===========================

.. c:function:: int cvmx_pko_rate_limit_packets(int port, int packets_s, int burst)

    supported on CN57XX, CN56XX, CN55XX, and CN54XX.

    :param port:
        Port to rate limit
    :type port: int

    :param packets_s:
        Maximum packet/sec
    :type packets_s: int

    :param burst:
        Maximum number of packets to burst in a row before rate
        limiting cuts in.
    :type burst: int

.. _`cvmx_pko_rate_limit_packets.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`cvmx_pko_rate_limit_bits`:

cvmx_pko_rate_limit_bits
========================

.. c:function:: int cvmx_pko_rate_limit_bits(int port, uint64_t bits_s, int burst)

    supported on CN57XX, CN56XX, CN55XX, and CN54XX.

    :param port:
        Port to rate limit
    :type port: int

    :param bits_s:
        PKO rate limit in bits/sec
    :type bits_s: uint64_t

    :param burst:
        Maximum number of bits to burst before rate
        limiting cuts in.
    :type burst: int

.. _`cvmx_pko_rate_limit_bits.description`:

Description
-----------

Returns Zero on success, negative on failure

.. This file was automatic generated / don't edit.

