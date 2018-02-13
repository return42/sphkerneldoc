.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-helper-loop.h

.. _`__cvmx_helper_loop_probe`:

\__cvmx_helper_loop_probe
=========================

.. c:function:: int __cvmx_helper_loop_probe(int interface)

    connected to it. The LOOP interface should still be down after this call.

    :param int interface:
        Interface to probe

.. _`__cvmx_helper_loop_probe.description`:

Description
-----------

Returns Number of ports on the interface. Zero to disable.

.. _`__cvmx_helper_loop_enable`:

\__cvmx_helper_loop_enable
==========================

.. c:function:: int __cvmx_helper_loop_enable(int interface)

    I/O should be fully functional. This is called with IPD enabled but PKO disabled.

    :param int interface:
        Interface to bring up

.. _`__cvmx_helper_loop_enable.description`:

Description
-----------

Returns Zero on success, negative on failure

.. This file was automatic generated / don't edit.

