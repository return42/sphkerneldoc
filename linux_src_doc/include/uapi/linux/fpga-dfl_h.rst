.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/fpga-dfl.h

.. _`dfl_fpga_get_api_version`:

DFL_FPGA_GET_API_VERSION
========================

.. c:function::  DFL_FPGA_GET_API_VERSION()

    \_IO(DFL_FPGA_MAGIC, DFL_FPGA_BASE + 0)

.. _`dfl_fpga_get_api_version.description`:

Description
-----------

Report the version of the driver API.

.. _`dfl_fpga_get_api_version.return`:

Return
------

Driver API Version.

.. _`dfl_fpga_check_extension`:

DFL_FPGA_CHECK_EXTENSION
========================

.. c:function::  DFL_FPGA_CHECK_EXTENSION()

    \_IO(DFL_FPGA_MAGIC, DFL_FPGA_BASE + 1)

.. _`dfl_fpga_check_extension.description`:

Description
-----------

Check whether an extension is supported.

.. _`dfl_fpga_check_extension.return`:

Return
------

0 if not supported, otherwise the extension is supported.

.. _`dfl_fpga_port_reset`:

DFL_FPGA_PORT_RESET
===================

.. c:function::  DFL_FPGA_PORT_RESET()

    \_IO(DFL_FPGA_MAGIC, DFL_PORT_BASE + 0)

.. _`dfl_fpga_port_reset.description`:

Description
-----------

Reset the FPGA Port and its AFU. No parameters are supported.
Userspace can do Port reset at any time, e.g. during DMA or PR. But
it should never cause any system level issue, only functional failure
(e.g. DMA or PR operation failure) and be recoverable from the failure.

.. _`dfl_fpga_port_reset.return`:

Return
------

0 on success, -errno of failure

.. This file was automatic generated / don't edit.

