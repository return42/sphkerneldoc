.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/cvmx-pko.c

.. _`__cvmx_pko_int`:

\__cvmx_pko_int
===============

.. c:function:: int __cvmx_pko_int(int interface, int index)

    :param interface:
        *undescribed*
    :type interface: int

    :param index:
        *undescribed*
    :type index: int

.. _`cvmx_pko_initialize_global`:

cvmx_pko_initialize_global
==========================

.. c:function:: void cvmx_pko_initialize_global( void)

    output system.  This does chip global config, and should only be done by one core.

    :param void:
        no arguments
    :type void: 

.. _`cvmx_pko_initialize_local`:

cvmx_pko_initialize_local
=========================

.. c:function:: int cvmx_pko_initialize_local( void)

    core initialization required by the PKO routines. This must be called on all cores that will do packet output, and must be called after the FPA has been initialized and filled with pages.

    :param void:
        no arguments
    :type void: 

.. _`cvmx_pko_initialize_local.description`:

Description
-----------

Returns 0 on success
!0 on failure

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

.. _`__cvmx_pko_reset`:

\__cvmx_pko_reset
=================

.. c:function:: void __cvmx_pko_reset( void)

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
        Number of queues to associate with this port
    :type num_queues: uint64_t

    :param priority:
        Array of priority levels for each queue. Values are
        allowed to be 0-8. A value of 8 get 8 times the traffic
        of a value of 1.  A value of 0 indicates that no rounds
        will be participated in. These priorities can be changed
        on the fly while the pko is enabled. A priority of 9
        indicates that static priority should be used.  If static
        priority is used all queues with static priority must be
        contiguous starting at the base_queue, and lower numbered
        queues have higher priority than higher numbered queues.
        There must be num_queues elements in the array.
    :type priority: const uint64_t

.. _`cvmx_pko_show_queue_map`:

cvmx_pko_show_queue_map
=======================

.. c:function:: void cvmx_pko_show_queue_map( void)

    > queues for different cores.

    :param void:
        no arguments
    :type void: 

.. _`cvmx_pko_rate_limit_packets`:

cvmx_pko_rate_limit_packets
===========================

.. c:function:: int cvmx_pko_rate_limit_packets(int port, int packets_s, int burst)

    supported on CN51XX and higher, excluding CN58XX.

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

    supported on CN51XX and higher, excluding CN58XX.

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

