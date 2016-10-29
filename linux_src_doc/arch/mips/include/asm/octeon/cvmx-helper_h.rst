.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-helper.h

.. _`void`:

void
====

.. c:function::  void(*cvmx_override_pko_queue_priority)

    priorities[16]) is a function pointer. It is meant to allow customization of the PKO queue priorities based on the port number. Users should set this pointer to a function before calling any cvmx-helper operations.

    :param \*cvmx_override_pko_queue_priority:
        *undescribed*

.. _`void`:

void
====

.. c:function::  void(*cvmx_override_ipd_port_setup)

    pointer. It is meant to allow customization of the IPD port setup before packet input/output comes online. It is called after cvmx-helper does the default IPD configuration, but before IPD is enabled. Users should set this pointer to a function before calling any cvmx-helper operations.

    :param \*cvmx_override_ipd_port_setup:
        *undescribed*

.. _`cvmx_helper_ipd_and_packet_input_enable`:

cvmx_helper_ipd_and_packet_input_enable
=======================================

.. c:function:: int cvmx_helper_ipd_and_packet_input_enable( void)

    The packet interfaces (RGMII and SPI) must be enabled after the IPD.  This should be called by the user program after any additional IPD configuration changes are made if CVMX_HELPER_ENABLE_IPD is not set in the executive-config.h file.

    :param  void:
        no arguments

.. _`cvmx_helper_ipd_and_packet_input_enable.description`:

Description
-----------

Returns 0 on success
-1 on failure

.. _`cvmx_helper_initialize_packet_io_global`:

cvmx_helper_initialize_packet_io_global
=======================================

.. c:function:: int cvmx_helper_initialize_packet_io_global( void)

    simple priority based queues for the ethernet ports. Each port is configured with a number of priority queues based on CVMX_PKO_QUEUES_PER_PORT\_\* where each queue is lower priority than the previous.

    :param  void:
        no arguments

.. _`cvmx_helper_initialize_packet_io_global.description`:

Description
-----------

Returns Zero on success, non-zero on failure

.. _`cvmx_helper_initialize_packet_io_local`:

cvmx_helper_initialize_packet_io_local
======================================

.. c:function:: int cvmx_helper_initialize_packet_io_local( void)

    :param  void:
        no arguments

.. _`cvmx_helper_initialize_packet_io_local.description`:

Description
-----------

Returns Zero on success, non-zero on failure

.. _`cvmx_helper_ports_on_interface`:

cvmx_helper_ports_on_interface
==============================

.. c:function:: int cvmx_helper_ports_on_interface(int interface)

    The interface must be initialized before the port count can be returned.

    :param int interface:
        Which interface to return port count for.

.. _`cvmx_helper_ports_on_interface.description`:

Description
-----------

Returns Port count for interface
-1 for uninitialized interface

.. _`cvmx_helper_get_number_of_interfaces`:

cvmx_helper_get_number_of_interfaces
====================================

.. c:function:: int cvmx_helper_get_number_of_interfaces( void)

    may have multiple ports. Most chips support two interfaces, but the CNX0XX and CNX1XX are exceptions. These only support one interface.

    :param  void:
        no arguments

.. _`cvmx_helper_get_number_of_interfaces.description`:

Description
-----------

Returns Number of interfaces on chip

.. _`cvmx_helper_interface_get_mode`:

cvmx_helper_interface_get_mode
==============================

.. c:function:: cvmx_helper_interface_mode_t cvmx_helper_interface_get_mode(int interface)

    chip and configuration, this function returns an enumeration of the type of packet I/O supported by an interface.

    :param int interface:
        Interface to probe

.. _`cvmx_helper_interface_get_mode.description`:

Description
-----------

Returns Mode of the interface. Unknown or unsupported interfaces return
DISABLED.

.. _`cvmx_helper_link_autoconf`:

cvmx_helper_link_autoconf
=========================

.. c:function:: cvmx_helper_link_info_t cvmx_helper_link_autoconf(int ipd_port)

    :param int ipd_port:
        IPD/PKO port to auto configure

.. _`cvmx_helper_link_autoconf.function-basically-does-the-equivalent-of`:

function basically does the equivalent of
-----------------------------------------

cvmx_helper_link_set(ipd_port, cvmx_helper_link_get(ipd_port));

.. _`cvmx_helper_link_autoconf.description`:

Description
-----------

Returns Link state after configure

.. _`cvmx_helper_link_get`:

cvmx_helper_link_get
====================

.. c:function:: cvmx_helper_link_info_t cvmx_helper_link_get(int ipd_port)

    auto negotiation. The result of this function may not match Octeon's link config if auto negotiation has changed since the last call to \ :c:func:`cvmx_helper_link_set`\ .

    :param int ipd_port:
        IPD/PKO port to query

.. _`cvmx_helper_link_get.description`:

Description
-----------

Returns Link state

.. _`cvmx_helper_link_set`:

cvmx_helper_link_set
====================

.. c:function:: int cvmx_helper_link_set(int ipd_port, cvmx_helper_link_info_t link_info)

    function does not influence auto negotiation at the PHY level. The passed link state must always match the link state returned by \ :c:func:`cvmx_helper_link_get`\ . It is normally best to use \ :c:func:`cvmx_helper_link_autoconf`\  instead.

    :param int ipd_port:
        IPD/PKO port to configure

    :param cvmx_helper_link_info_t link_info:
        The new link state

.. _`cvmx_helper_link_set.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`cvmx_helper_interface_probe`:

cvmx_helper_interface_probe
===========================

.. c:function:: int cvmx_helper_interface_probe(int interface)

    number of hardware ports connected to it. It doesn't setup the ports or enable them. The main goal here is to set the global interface_port_count[interface] correctly. Hardware setup of the ports will be performed later.

    :param int interface:
        Interface to probe

.. _`cvmx_helper_interface_probe.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`cvmx_helper_configure_loopback`:

cvmx_helper_configure_loopback
==============================

.. c:function:: int cvmx_helper_configure_loopback(int ipd_port, int enable_internal, int enable_external)

    causes packets sent by the port to be received by Octeon. External loopback causes packets received from the wire to sent out again.

    :param int ipd_port:
        IPD/PKO port to loopback.

    :param int enable_internal:
        Non zero if you want internal loopback

    :param int enable_external:
        Non zero if you want external loopback

.. _`cvmx_helper_configure_loopback.description`:

Description
-----------

Returns Zero on success, negative on failure.

.. This file was automatic generated / don't edit.
