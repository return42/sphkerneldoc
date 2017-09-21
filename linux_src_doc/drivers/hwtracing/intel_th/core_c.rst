.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/intel_th/core.c

.. _`intel_th_output_enable`:

intel_th_output_enable
======================

.. c:function:: int intel_th_output_enable(struct intel_th *th, unsigned int otype)

    find and enable a device for a given output type

    :param struct intel_th \*th:
        Intel TH instance

    :param unsigned int otype:
        output type

.. _`intel_th_output_enable.description`:

Description
-----------

Go through the unallocated output devices, find the first one whos type
matches \ ``otype``\  and instantiate it. These devices are removed when the hub
device is removed, see \ :c:func:`intel_th_remove`\ .

.. _`intel_th_alloc`:

intel_th_alloc
==============

.. c:function:: struct intel_th *intel_th_alloc(struct device *dev, struct intel_th_drvdata *drvdata, struct resource *devres, unsigned int ndevres, int irq)

    allocate a new Intel TH device and its subdevices

    :param struct device \*dev:
        parent device

    :param struct intel_th_drvdata \*drvdata:
        *undescribed*

    :param struct resource \*devres:
        parent's resources

    :param unsigned int ndevres:
        number of resources

    :param int irq:
        irq number

.. _`intel_th_trace_enable`:

intel_th_trace_enable
=====================

.. c:function:: int intel_th_trace_enable(struct intel_th_device *thdev)

    enable tracing for an output device

    :param struct intel_th_device \*thdev:
        output device that requests tracing be enabled

.. _`intel_th_trace_disable`:

intel_th_trace_disable
======================

.. c:function:: int intel_th_trace_disable(struct intel_th_device *thdev)

    disable tracing for an output device

    :param struct intel_th_device \*thdev:
        output device that requests tracing be disabled

.. This file was automatic generated / don't edit.

