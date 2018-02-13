.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/cvmx-helper-spi.c

.. _`__cvmx_helper_spi_probe`:

\__cvmx_helper_spi_probe
========================

.. c:function:: int __cvmx_helper_spi_probe(int interface)

    connected to it. The SPI interface should still be down after this call.

    :param int interface:
        Interface to probe

.. _`__cvmx_helper_spi_probe.description`:

Description
-----------

Returns Number of ports on the interface. Zero to disable.

.. _`__cvmx_helper_spi_enable`:

\__cvmx_helper_spi_enable
=========================

.. c:function:: int __cvmx_helper_spi_enable(int interface)

    should be fully functional. This is called with IPD enabled but PKO disabled.

    :param int interface:
        Interface to bring up

.. _`__cvmx_helper_spi_enable.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`__cvmx_helper_spi_link_get`:

\__cvmx_helper_spi_link_get
===========================

.. c:function:: cvmx_helper_link_info_t __cvmx_helper_spi_link_get(int ipd_port)

    auto negotiation. The result of this function may not match Octeon's link config if auto negotiation has changed since the last call to \ :c:func:`cvmx_helper_link_set`\ .

    :param int ipd_port:
        IPD/PKO port to query

.. _`__cvmx_helper_spi_link_get.description`:

Description
-----------

Returns Link state

.. _`__cvmx_helper_spi_link_set`:

\__cvmx_helper_spi_link_set
===========================

.. c:function:: int __cvmx_helper_spi_link_set(int ipd_port, cvmx_helper_link_info_t link_info)

    function does not influence auto negotiation at the PHY level. The passed link state must always match the link state returned by \ :c:func:`cvmx_helper_link_get`\ .

    :param int ipd_port:
        IPD/PKO port to configure

    :param cvmx_helper_link_info_t link_info:
        The new link state

.. _`__cvmx_helper_spi_link_set.description`:

Description
-----------

Returns Zero on success, negative on failure

.. This file was automatic generated / don't edit.

