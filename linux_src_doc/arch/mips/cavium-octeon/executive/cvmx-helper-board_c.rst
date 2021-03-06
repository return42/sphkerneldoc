.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/cvmx-helper-board.c

.. _`cvmx_helper_board_get_mii_address`:

cvmx_helper_board_get_mii_address
=================================

.. c:function:: int cvmx_helper_board_get_mii_address(int ipd_port)

    port. A result of -1 means there isn't a MII capable PHY connected to this port. On chips supporting multiple MII busses the bus number is encoded in bits <15:8>.

    :param ipd_port:
        Octeon IPD port to get the MII address for.
    :type ipd_port: int

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

\__cvmx_helper_board_link_get
=============================

.. c:function:: cvmx_helper_link_info_t __cvmx_helper_board_link_get(int ipd_port)

    ethernet ports link speed. Most Octeon boards have Marvell PHYs and are handled by the fall through case. This function must be updated for boards that don't have the normal Marvell PHYs.

    :param ipd_port:
        IPD input port associated with the port we want to get link
        status for.
    :type ipd_port: int

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

.. _`__cvmx_helper_board_interface_probe`:

\__cvmx_helper_board_interface_probe
====================================

.. c:function:: int __cvmx_helper_board_interface_probe(int interface, int supported_ports)

    determines the number of ports Octeon can support on a specific interface. This function is the per board location to override this value. It is called with the number of ports Octeon might support and should return the number of actual ports on the board.

    :param interface:
        Interface to probe
    :type interface: int

    :param supported_ports:
        Number of ports Octeon supports.
    :type supported_ports: int

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

\__cvmx_helper_board_hardware_enable
====================================

.. c:function:: int __cvmx_helper_board_hardware_enable(int interface)

    called after by \ :c:func:`cvmx_helper_packet_hardware_enable`\  to perform board specific initialization. For most boards nothing is needed.

    :param interface:
        Interface to enable
    :type interface: int

.. _`__cvmx_helper_board_hardware_enable.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_board_usb_get_clock_type`:

\__cvmx_helper_board_usb_get_clock_type
=======================================

.. c:function:: enum cvmx_helper_board_usb_clock_types __cvmx_helper_board_usb_get_clock_type( void)

    Used by the USB code for auto configuration of clock type.

    :param void:
        no arguments
    :type void: 

.. _`__cvmx_helper_board_usb_get_clock_type.description`:

Description
-----------

Return USB clock type enumeration

.. This file was automatic generated / don't edit.

