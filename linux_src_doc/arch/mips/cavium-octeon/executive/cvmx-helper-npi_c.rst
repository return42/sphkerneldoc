.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/cvmx-helper-npi.c

.. _`__cvmx_helper_npi_probe`:

\__cvmx_helper_npi_probe
========================

.. c:function:: int __cvmx_helper_npi_probe(int interface)

    connected to it. The NPI interface should still be down after this call.

    :param interface:
        Interface to probe
    :type interface: int

.. _`__cvmx_helper_npi_probe.description`:

Description
-----------

Returns Number of ports on the interface. Zero to disable.

.. _`__cvmx_helper_npi_enable`:

\__cvmx_helper_npi_enable
=========================

.. c:function:: int __cvmx_helper_npi_enable(int interface)

    I/O should be fully functional. This is called with IPD enabled but PKO disabled.

    :param interface:
        Interface to bring up
    :type interface: int

.. _`__cvmx_helper_npi_enable.description`:

Description
-----------

Returns Zero on success, negative on failure

.. This file was automatic generated / don't edit.

