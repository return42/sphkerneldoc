.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/arm-cci.c

.. _`__cci_ace_get_port`:

__cci_ace_get_port
==================

.. c:function:: int __cci_ace_get_port(struct device_node *dn, int type)

    Function to retrieve the port index connected to a cpu or device.

    :param struct device_node \*dn:
        device node of the device to look-up

    :param int type:
        port type

.. _`__cci_ace_get_port.return-value`:

Return value
------------

- CCI port index if success
- -ENODEV if failure

.. _`cci_port_control`:

cci_port_control
================

.. c:function:: void notrace cci_port_control(unsigned int port, bool enable)

    function to control a CCI port

    :param unsigned int port:
        index of the port to setup

    :param bool enable:
        if true enables the port, if false disables it

.. _`cci_disable_port_by_cpu`:

cci_disable_port_by_cpu
=======================

.. c:function:: int notrace cci_disable_port_by_cpu(u64 mpidr)

    function to disable a CCI port by CPU reference

    :param u64 mpidr:
        mpidr of the CPU whose CCI port should be disabled

.. _`cci_disable_port_by_cpu.description`:

Description
-----------

Disabling a CCI port for a CPU implies disabling the CCI port
controlling that CPU cluster. Code disabling CPU CCI ports
must make sure that the CPU running the code is the last active CPU
in the cluster ie all other CPUs are quiescent in a low power state.

.. _`cci_disable_port_by_cpu.return`:

Return
------

0 on success
-ENODEV on port look-up failure

.. _`cci_enable_port_for_self`:

cci_enable_port_for_self
========================

.. c:function:: void __naked cci_enable_port_for_self( void)

    enable a CCI port for calling CPU

    :param  void:
        no arguments

.. _`cci_enable_port_for_self.description`:

Description
-----------

Enabling a CCI port for the calling CPU implies enabling the CCI
port controlling that CPU's cluster. Caller must make sure that the
CPU running the code is the first active CPU in the cluster and all
other CPUs are quiescent in a low power state  or waiting for this CPU
to complete the CCI initialization.

Because this is called when the MMU is still off and with no stack,
the code must be position independent and ideally rely on callee
clobbered registers only.  To achieve this we must code this function
entirely in assembler.

On success this returns with the proper CCI port enabled.  In case of
any failure this never returns as the inability to enable the CCI is
fatal and there is no possible recovery at this stage.

.. _`__cci_control_port_by_device`:

__cci_control_port_by_device
============================

.. c:function:: int notrace __cci_control_port_by_device(struct device_node *dn, bool enable)

    function to control a CCI port by device reference

    :param struct device_node \*dn:
        device node pointer of the device whose CCI port should be
        controlled

    :param bool enable:
        if true enables the port, if false disables it

.. _`__cci_control_port_by_device.return`:

Return
------

0 on success
-ENODEV on port look-up failure

.. _`__cci_control_port_by_index`:

__cci_control_port_by_index
===========================

.. c:function:: int notrace __cci_control_port_by_index(u32 port, bool enable)

    function to control a CCI port by port index

    :param u32 port:
        port index previously retrieved with \ :c:func:`cci_ace_get_port`\ 

    :param bool enable:
        if true enables the port, if false disables it

.. _`__cci_control_port_by_index.return`:

Return
------

0 on success
-ENODEV on port index out of range
-EPERM if operation carried out on an ACE PORT

.. This file was automatic generated / don't edit.

