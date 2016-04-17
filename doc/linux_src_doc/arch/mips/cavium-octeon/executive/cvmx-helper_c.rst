.. -*- coding: utf-8; mode: rst -*-

=============
cvmx-helper.c
=============


.. _`cvmx_override_pko_queue_priority`:

cvmx_override_pko_queue_priority
================================

.. c:function:: void cvmx_override_pko_queue_priority (int pko_port, uint64_t priorities[16])

    :param int pko_port:

        *undescribed*

    :param uint64_t priorities:

        *undescribed*



.. _`cvmx_override_pko_queue_priority.description`:

Description
-----------

priorities[16]) is a function pointer. It is meant to allow
customization of the PKO queue priorities based on the port
number. Users should set this pointer to a function before
calling any cvmx-helper operations.



.. _`cvmx_override_ipd_port_setup`:

cvmx_override_ipd_port_setup
============================

.. c:function:: void cvmx_override_ipd_port_setup (int ipd_port)

    :param int ipd_port:

        *undescribed*



.. _`cvmx_override_ipd_port_setup.description`:

Description
-----------

pointer. It is meant to allow customization of the IPD port
setup before packet input/output comes online. It is called
after cvmx-helper does the default IPD configuration, but
before IPD is enabled. Users should set this pointer to a
function before calling any cvmx-helper operations.



.. _`cvmx_helper_get_number_of_interfaces`:

cvmx_helper_get_number_of_interfaces
====================================

.. c:function:: int cvmx_helper_get_number_of_interfaces ( void)

    :param void:
        no arguments



.. _`cvmx_helper_get_number_of_interfaces.description`:

Description
-----------

may have multiple ports. Most chips support two interfaces,
but the CNX0XX and CNX1XX are exceptions. These only support
one interface.

Returns Number of interfaces on chip



.. _`cvmx_helper_ports_on_interface`:

cvmx_helper_ports_on_interface
==============================

.. c:function:: int cvmx_helper_ports_on_interface (int interface)

    :param int interface:
        Interface to get the port count for



.. _`cvmx_helper_ports_on_interface.description`:

Description
-----------

Returns Number of ports on interface. Can be Zero.



.. _`cvmx_helper_ports_on_interface.description`:

Description
-----------

Returns Number of ports on interface. Can be Zero.



.. _`cvmx_helper_interface_get_mode`:

cvmx_helper_interface_get_mode
==============================

.. c:function:: cvmx_helper_interface_mode_t cvmx_helper_interface_get_mode (int interface)

    :param int interface:
        Interface to probe



.. _`cvmx_helper_interface_get_mode.description`:

Description
-----------

Returns Mode of the interface. Unknown or unsupported interfaces return
DISABLED.



.. _`cvmx_helper_interface_get_mode.description`:

Description
-----------

Returns Mode of the interface. Unknown or unsupported interfaces return
DISABLED.



.. _`__cvmx_helper_port_setup_ipd`:

__cvmx_helper_port_setup_ipd
============================

.. c:function:: int __cvmx_helper_port_setup_ipd (int ipd_port)

    :param int ipd_port:
        Port to configure. This follows the IPD numbering, not the
        per interface numbering



.. _`__cvmx_helper_port_setup_ipd.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`__cvmx_helper_port_setup_ipd.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`cvmx_helper_interface_enumerate`:

cvmx_helper_interface_enumerate
===============================

.. c:function:: int cvmx_helper_interface_enumerate (int interface)

    :param int interface:
        Interface to probe



.. _`cvmx_helper_interface_enumerate.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`cvmx_helper_interface_enumerate.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`cvmx_helper_interface_probe`:

cvmx_helper_interface_probe
===========================

.. c:function:: int cvmx_helper_interface_probe (int interface)

    :param int interface:
        Interface to probe



.. _`cvmx_helper_interface_probe.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`cvmx_helper_interface_probe.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`__cvmx_helper_interface_setup_ipd`:

__cvmx_helper_interface_setup_ipd
=================================

.. c:function:: int __cvmx_helper_interface_setup_ipd (int interface)

    :param int interface:
        Interface to setup IPD/PIP for



.. _`__cvmx_helper_interface_setup_ipd.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`__cvmx_helper_interface_setup_ipd.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`__cvmx_helper_global_setup_ipd`:

__cvmx_helper_global_setup_ipd
==============================

.. c:function:: int __cvmx_helper_global_setup_ipd ( void)

    :param void:
        no arguments



.. _`__cvmx_helper_global_setup_ipd.description`:

Description
-----------

interface or port. This must be called before IPD is enabled.

Returns Zero on success, negative on failure.



.. _`__cvmx_helper_interface_setup_pko`:

__cvmx_helper_interface_setup_pko
=================================

.. c:function:: int __cvmx_helper_interface_setup_pko (int interface)

    :param int interface:
        Interface to setup PKO for



.. _`__cvmx_helper_interface_setup_pko.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`__cvmx_helper_interface_setup_pko.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`__cvmx_helper_global_setup_pko`:

__cvmx_helper_global_setup_pko
==============================

.. c:function:: int __cvmx_helper_global_setup_pko ( void)

    :param void:
        no arguments



.. _`__cvmx_helper_global_setup_pko.description`:

Description
-----------

interface or port. This must be called before PKO is enabled.

Returns Zero on success, negative on failure.



.. _`__cvmx_helper_global_setup_backpressure`:

__cvmx_helper_global_setup_backpressure
=======================================

.. c:function:: int __cvmx_helper_global_setup_backpressure ( void)

    :param void:
        no arguments



.. _`__cvmx_helper_global_setup_backpressure.description`:

Description
-----------


Returns Zero on success, negative on failure



.. _`__cvmx_helper_packet_hardware_enable`:

__cvmx_helper_packet_hardware_enable
====================================

.. c:function:: int __cvmx_helper_packet_hardware_enable (int interface)

    :param int interface:
        Interface to enable



.. _`__cvmx_helper_packet_hardware_enable.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`__cvmx_helper_packet_hardware_enable.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`__cvmx_helper_errata_fix_ipd_ptr_alignment`:

__cvmx_helper_errata_fix_ipd_ptr_alignment
==========================================

.. c:function:: int __cvmx_helper_errata_fix_ipd_ptr_alignment ( void)

    :param void:
        no arguments



.. _`__cvmx_helper_errata_fix_ipd_ptr_alignment.description`:

Description
-----------


Returns 0 on success
!0 on failure



.. _`cvmx_helper_ipd_and_packet_input_enable`:

cvmx_helper_ipd_and_packet_input_enable
=======================================

.. c:function:: int cvmx_helper_ipd_and_packet_input_enable ( void)

    :param void:
        no arguments



.. _`cvmx_helper_ipd_and_packet_input_enable.description`:

Description
-----------

function enables IPD/PIP and begins packet input and output.

Returns Zero on success, negative on failure



.. _`cvmx_helper_initialize_packet_io_global`:

cvmx_helper_initialize_packet_io_global
=======================================

.. c:function:: int cvmx_helper_initialize_packet_io_global ( void)

    :param void:
        no arguments



.. _`cvmx_helper_initialize_packet_io_global.description`:

Description
-----------

simple priority based queues for the ethernet ports. Each
port is configured with a number of priority queues based
on CVMX_PKO_QUEUES_PER_PORT\_\* where each queue is lower
priority than the previous.

Returns Zero on success, non-zero on failure



.. _`cvmx_helper_initialize_packet_io_local`:

cvmx_helper_initialize_packet_io_local
======================================

.. c:function:: int cvmx_helper_initialize_packet_io_local ( void)

    :param void:
        no arguments



.. _`cvmx_helper_initialize_packet_io_local.description`:

Description
-----------


Returns Zero on success, non-zero on failure



.. _`cvmx_helper_link_autoconf`:

cvmx_helper_link_autoconf
=========================

.. c:function:: cvmx_helper_link_info_t cvmx_helper_link_autoconf (int ipd_port)

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

.. c:function:: cvmx_helper_link_info_t cvmx_helper_link_get (int ipd_port)

    :param int ipd_port:
        IPD/PKO port to query



.. _`cvmx_helper_link_get.description`:

Description
-----------

Returns Link state



.. _`cvmx_helper_link_get.description`:

Description
-----------

Returns Link state



.. _`cvmx_helper_link_set`:

cvmx_helper_link_set
====================

.. c:function:: int cvmx_helper_link_set (int ipd_port, cvmx_helper_link_info_t link_info)

    :param int ipd_port:
        IPD/PKO port to configure

    :param cvmx_helper_link_info_t link_info:
        The new link state



.. _`cvmx_helper_link_set.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`cvmx_helper_link_set.description`:

Description
-----------

Returns Zero on success, negative on failure



.. _`cvmx_helper_configure_loopback`:

cvmx_helper_configure_loopback
==============================

.. c:function:: int cvmx_helper_configure_loopback (int ipd_port, int enable_internal, int enable_external)

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



.. _`cvmx_helper_configure_loopback.description`:

Description
-----------

Returns Zero on success, negative on failure.

