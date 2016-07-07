.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/cvmx-helper-board.c

.. _`cvmx_helper_link_info_t`:

cvmx_helper_link_info_t
=======================

.. c:function::  cvmx_helper_link_info_t(*cvmx_override_board_link_get)

    pointer. It is meant to allow customization of the process of talking to a PHY to determine link speed. It is called every time a PHY must be polled for link status. Users should set this pointer to a function before calling any cvmx-helper operations.

    :param \*cvmx_override_board_link_get:
        *undescribed*

.. _`cvmx_helper_board_get_mii_address`:

cvmx_helper_board_get_mii_address
=================================

.. c:function:: int cvmx_helper_board_get_mii_address(int ipd_port)

    port. A result of -1 means there isn't a MII capable PHY connected to this port. On chips supporting multiple MII busses the bus number is encoded in bits <15:8>.

    :param int ipd_port:
        Octeon IPD port to get the MII address for.

.. _`cvmx_helper_board_get_mii_address.description`:

Description
-----------

This function must be modified for every new Octeon board.
Internally it uses switch statements based on the cvmx_sysinfo
data to determine board types and revisions. It replies on the
fact that every Octeon board receives a unique board type
enumeration from the bootloader.

Returns MII PHY address and bus number or -1.

.. _`__cvmx_helper_board_link_get`:

__cvmx_helper_board_link_get
============================

.. c:function:: cvmx_helper_link_info_t __cvmx_helper_board_link_get(int ipd_port)

    ethernet ports link speed. Most Octeon boards have Marvell PHYs and are handled by the fall through case. This function must be updated for boards that don't have the normal Marvell PHYs.

    :param int ipd_port:
        IPD input port associated with the port we want to get link
        status for.

.. _`__cvmx_helper_board_link_get.description`:

Description
-----------

This function must be modified for every new Octeon board.
Internally it uses switch statements based on the cvmx_sysinfo
data to determine board types and revisions. It relies on the
fact that every Octeon board receives a unique board type
enumeration from the bootloader.

Returns The ports link status. If the link isn't fully resolved, this must
return zero.

.. _`cvmx_helper_board_link_set_phy`:

cvmx_helper_board_link_set_phy
==============================

.. c:function:: int cvmx_helper_board_link_set_phy(int phy_addr, cvmx_helper_board_set_phy_link_flags_types_t link_flags, cvmx_helper_link_info_t link_info)

    speed, duplex, and auto-negotiation. This programs the PHY and not Octeon. This can be used to force Octeon's links to specific settings.

    :param int phy_addr:
        The address of the PHY to program

    :param cvmx_helper_board_set_phy_link_flags_types_t link_flags:
        *undescribed*

    :param cvmx_helper_link_info_t link_info:
        Link speed to program. If the speed is zero and auto-negotiation
        is enabled, all possible negotiation speeds are advertised.

.. _`cvmx_helper_board_link_set_phy.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_board_interface_probe`:

__cvmx_helper_board_interface_probe
===================================

.. c:function:: int __cvmx_helper_board_interface_probe(int interface, int supported_ports)

    determines the number of ports Octeon can support on a specific interface. This function is the per board location to override this value. It is called with the number of ports Octeon might support and should return the number of actual ports on the board.

    :param int interface:
        Interface to probe

    :param int supported_ports:
        Number of ports Octeon supports.

.. _`__cvmx_helper_board_interface_probe.description`:

Description
-----------

This function must be modifed for every new Octeon board.
Internally it uses switch statements based on the cvmx_sysinfo
data to determine board types and revisions. It relys on the
fact that every Octeon board receives a unique board type
enumeration from the bootloader.

Returns Number of ports the actual board supports. Many times this will
simple be "support_ports".

.. _`__cvmx_helper_board_hardware_enable`:

__cvmx_helper_board_hardware_enable
===================================

.. c:function:: int __cvmx_helper_board_hardware_enable(int interface)

    called after by \ :c:func:`cvmx_helper_packet_hardware_enable`\  to perform board specific initialization. For most boards nothing is needed.

    :param int interface:
        Interface to enable

.. _`__cvmx_helper_board_hardware_enable.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_board_usb_get_clock_type`:

__cvmx_helper_board_usb_get_clock_type
======================================

.. c:function:: enum cvmx_helper_board_usb_clock_types __cvmx_helper_board_usb_get_clock_type( void)

    Used by the USB code for auto configuration of clock type.

    :param  void:
        no arguments

.. _`__cvmx_helper_board_usb_get_clock_type.description`:

Description
-----------

Return USB clock type enumeration

.. This file was automatic generated / don't edit.

