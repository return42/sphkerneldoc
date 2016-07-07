.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/cvmx-helper-sgmii.c

.. _`__cvmx_helper_sgmii_hardware_init_one_time`:

__cvmx_helper_sgmii_hardware_init_one_time
==========================================

.. c:function:: int __cvmx_helper_sgmii_hardware_init_one_time(int interface, int index)

    :param int interface:
        Interface to init

    :param int index:
        Index of prot on the interface

.. _`__cvmx_helper_sgmii_hardware_init_one_time.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_sgmii_hardware_init_link`:

__cvmx_helper_sgmii_hardware_init_link
======================================

.. c:function:: int __cvmx_helper_sgmii_hardware_init_link(int interface, int index)

    of link.

    :param int interface:
        Interface to init

    :param int index:
        Index of prot on the interface

.. _`__cvmx_helper_sgmii_hardware_init_link.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_sgmii_hardware_init_link_speed`:

__cvmx_helper_sgmii_hardware_init_link_speed
============================================

.. c:function:: int __cvmx_helper_sgmii_hardware_init_link_speed(int interface, int index, cvmx_helper_link_info_t link_info)

    link is up.

    :param int interface:
        Interface to init

    :param int index:
        Index of prot on the interface

    :param cvmx_helper_link_info_t link_info:
        Link state to configure

.. _`__cvmx_helper_sgmii_hardware_init_link_speed.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_sgmii_hardware_init`:

__cvmx_helper_sgmii_hardware_init
=================================

.. c:function:: int __cvmx_helper_sgmii_hardware_init(int interface, int num_ports)

    leave I/O disabled using the GMX override. This function follows the bringup documented in 10.6.3 of the manual.

    :param int interface:
        Interface to bringup

    :param int num_ports:
        Number of ports on the interface

.. _`__cvmx_helper_sgmii_hardware_init.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_sgmii_probe`:

__cvmx_helper_sgmii_probe
=========================

.. c:function:: int __cvmx_helper_sgmii_probe(int interface)

    connected to it. The SGMII interface should still be down after this call.

    :param int interface:
        Interface to probe

.. _`__cvmx_helper_sgmii_probe.description`:

Description
-----------

Returns Number of ports on the interface. Zero to disable.

.. _`__cvmx_helper_sgmii_enable`:

__cvmx_helper_sgmii_enable
==========================

.. c:function:: int __cvmx_helper_sgmii_enable(int interface)

    I/O should be fully functional. This is called with IPD enabled but PKO disabled.

    :param int interface:
        Interface to bring up

.. _`__cvmx_helper_sgmii_enable.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_sgmii_link_get`:

__cvmx_helper_sgmii_link_get
============================

.. c:function:: cvmx_helper_link_info_t __cvmx_helper_sgmii_link_get(int ipd_port)

    auto negotiation. The result of this function may not match Octeon's link config if auto negotiation has changed since the last call to \ :c:func:`cvmx_helper_link_set`\ .

    :param int ipd_port:
        IPD/PKO port to query

.. _`__cvmx_helper_sgmii_link_get.description`:

Description
-----------

Returns Link state

.. _`__cvmx_helper_sgmii_link_set`:

__cvmx_helper_sgmii_link_set
============================

.. c:function:: int __cvmx_helper_sgmii_link_set(int ipd_port, cvmx_helper_link_info_t link_info)

    function does not influence auto negotiation at the PHY level. The passed link state must always match the link state returned by \ :c:func:`cvmx_helper_link_get`\ . It is normally best to use \ :c:func:`cvmx_helper_link_autoconf`\  instead.

    :param int ipd_port:
        IPD/PKO port to configure

    :param cvmx_helper_link_info_t link_info:
        The new link state

.. _`__cvmx_helper_sgmii_link_set.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_sgmii_configure_loopback`:

__cvmx_helper_sgmii_configure_loopback
======================================

.. c:function:: int __cvmx_helper_sgmii_configure_loopback(int ipd_port, int enable_internal, int enable_external)

    loopback causes packets sent by the port to be received by Octeon. External loopback causes packets received from the wire to sent out again.

    :param int ipd_port:
        IPD/PKO port to loopback.

    :param int enable_internal:
        Non zero if you want internal loopback

    :param int enable_external:
        Non zero if you want external loopback

.. _`__cvmx_helper_sgmii_configure_loopback.description`:

Description
-----------

Returns Zero on success, negative on failure.

.. This file was automatic generated / don't edit.

