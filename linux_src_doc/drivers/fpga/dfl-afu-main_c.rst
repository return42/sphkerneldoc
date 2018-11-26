.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/dfl-afu-main.c

.. _`port_enable`:

port_enable
===========

.. c:function:: void port_enable(struct platform_device *pdev)

    enable a port

    :param pdev:
        port platform device.
    :type pdev: struct platform_device \*

.. _`port_enable.description`:

Description
-----------

Enable Port by clear the port soft reset bit, which is set by default.
The AFU is unable to respond to any MMIO access while in reset.
port_enable function should only be used after port_disable function.

.. _`port_disable`:

port_disable
============

.. c:function:: int port_disable(struct platform_device *pdev)

    disable a port

    :param pdev:
        port platform device.
    :type pdev: struct platform_device \*

.. _`port_disable.description`:

Description
-----------

Disable Port by setting the port soft reset bit, it puts the port into
reset.

.. This file was automatic generated / don't edit.

