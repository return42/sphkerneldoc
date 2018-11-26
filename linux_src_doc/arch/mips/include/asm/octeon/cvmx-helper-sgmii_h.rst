.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-helper-sgmii.h

.. _`__cvmx_helper_sgmii_probe`:

\__cvmx_helper_sgmii_probe
==========================

.. c:function:: int __cvmx_helper_sgmii_probe(int interface)

    connected to it. The SGMII interface should still be down after this call.

    :param interface:
        Interface to probe
    :type interface: int

.. _`__cvmx_helper_sgmii_probe.description`:

Description
-----------

Returns Number of ports on the interface. Zero to disable.

.. _`__cvmx_helper_sgmii_enable`:

\__cvmx_helper_sgmii_enable
===========================

.. c:function:: int __cvmx_helper_sgmii_enable(int interface)

    I/O should be fully functional. This is called with IPD enabled but PKO disabled.

    :param interface:
        Interface to bring up
    :type interface: int

.. _`__cvmx_helper_sgmii_enable.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_sgmii_link_get`:

\__cvmx_helper_sgmii_link_get
=============================

.. c:function:: cvmx_helper_link_info_t __cvmx_helper_sgmii_link_get(int ipd_port)

    auto negotiation. The result of this function may not match Octeon's link config if auto negotiation has changed since the last call to \ :c:func:`cvmx_helper_link_set`\ .

    :param ipd_port:
        IPD/PKO port to query
    :type ipd_port: int

.. _`__cvmx_helper_sgmii_link_get.description`:

Description
-----------

Returns Link state

.. _`__cvmx_helper_sgmii_link_set`:

\__cvmx_helper_sgmii_link_set
=============================

.. c:function:: int __cvmx_helper_sgmii_link_set(int ipd_port, cvmx_helper_link_info_t link_info)

    function does not influence auto negotiation at the PHY level. The passed link state must always match the link state returned by \ :c:func:`cvmx_helper_link_get`\ .

    :param ipd_port:
        IPD/PKO port to configure
    :type ipd_port: int

    :param link_info:
        The new link state
    :type link_info: cvmx_helper_link_info_t

.. _`__cvmx_helper_sgmii_link_set.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_sgmii_configure_loopback`:

\__cvmx_helper_sgmii_configure_loopback
=======================================

.. c:function:: int __cvmx_helper_sgmii_configure_loopback(int ipd_port, int enable_internal, int enable_external)

    causes packets sent by the port to be received by Octeon. External loopback causes packets received from the wire to sent out again.

    :param ipd_port:
        IPD/PKO port to loopback.
    :type ipd_port: int

    :param enable_internal:
        Non zero if you want internal loopback
    :type enable_internal: int

    :param enable_external:
        Non zero if you want external loopback
    :type enable_external: int

.. _`__cvmx_helper_sgmii_configure_loopback.description`:

Description
-----------

Returns Zero on success, negative on failure.

.. This file was automatic generated / don't edit.

