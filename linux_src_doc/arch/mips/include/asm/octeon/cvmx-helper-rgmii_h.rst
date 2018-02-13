.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-helper-rgmii.h

.. _`__cvmx_helper_rgmii_probe`:

\__cvmx_helper_rgmii_probe
==========================

.. c:function:: int __cvmx_helper_rgmii_probe(int interface)

    :param int interface:
        Interface to probe

.. _`__cvmx_helper_rgmii_probe.description`:

Description
-----------

Returns Number of RGMII/GMII/MII ports (0-4).

.. _`cvmx_helper_rgmii_internal_loopback`:

cvmx_helper_rgmii_internal_loopback
===================================

.. c:function:: void cvmx_helper_rgmii_internal_loopback(int port)

    out will be received back again on the same port. Externally received packets will echo back out.

    :param int port:
        IPD port number to loop.

.. _`__cvmx_helper_rgmii_enable`:

\__cvmx_helper_rgmii_enable
===========================

.. c:function:: int __cvmx_helper_rgmii_enable(int interface)

    to get RGMII to function on the supplied interface.

    :param int interface:
        PKO Interface to configure (0 or 1)

.. _`__cvmx_helper_rgmii_enable.description`:

Description
-----------

Returns Zero on success

.. _`__cvmx_helper_rgmii_link_get`:

\__cvmx_helper_rgmii_link_get
=============================

.. c:function:: cvmx_helper_link_info_t __cvmx_helper_rgmii_link_get(int ipd_port)

    auto negotiation. The result of this function may not match Octeon's link config if auto negotiation has changed since the last call to \ :c:func:`cvmx_helper_link_set`\ .

    :param int ipd_port:
        IPD/PKO port to query

.. _`__cvmx_helper_rgmii_link_get.description`:

Description
-----------

Returns Link state

.. _`__cvmx_helper_rgmii_link_set`:

\__cvmx_helper_rgmii_link_set
=============================

.. c:function:: int __cvmx_helper_rgmii_link_set(int ipd_port, cvmx_helper_link_info_t link_info)

    function does not influence auto negotiation at the PHY level. The passed link state must always match the link state returned by \ :c:func:`cvmx_helper_link_get`\ .

    :param int ipd_port:
        IPD/PKO port to configure

    :param cvmx_helper_link_info_t link_info:
        The new link state

.. _`__cvmx_helper_rgmii_link_set.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_rgmii_configure_loopback`:

\__cvmx_helper_rgmii_configure_loopback
=======================================

.. c:function:: int __cvmx_helper_rgmii_configure_loopback(int ipd_port, int enable_internal, int enable_external)

    causes packets sent by the port to be received by Octeon. External loopback causes packets received from the wire to sent out again.

    :param int ipd_port:
        IPD/PKO port to loopback.

    :param int enable_internal:
        Non zero if you want internal loopback

    :param int enable_external:
        Non zero if you want external loopback

.. _`__cvmx_helper_rgmii_configure_loopback.description`:

Description
-----------

Returns Zero on success, negative on failure.

.. This file was automatic generated / don't edit.

