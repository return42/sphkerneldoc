.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/intel_th/core.c

.. _`intel_th_output_enable`:

intel_th_output_enable
======================

.. c:function:: int intel_th_output_enable(struct intel_th *th, unsigned int otype)

    find and enable a device for a given output type

    :param th:
        Intel TH instance
    :type th: struct intel_th \*

    :param otype:
        output type
    :type otype: unsigned int

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

    :param dev:
        parent device
    :type dev: struct device \*

    :param drvdata:
        *undescribed*
    :type drvdata: struct intel_th_drvdata \*

    :param devres:
        parent's resources
    :type devres: struct resource \*

    :param ndevres:
        number of resources
    :type ndevres: unsigned int

    :param irq:
        irq number
    :type irq: int

.. _`intel_th_trace_enable`:

intel_th_trace_enable
=====================

.. c:function:: int intel_th_trace_enable(struct intel_th_device *thdev)

    enable tracing for an output device

    :param thdev:
        output device that requests tracing be enabled
    :type thdev: struct intel_th_device \*

.. _`intel_th_trace_disable`:

intel_th_trace_disable
======================

.. c:function:: int intel_th_trace_disable(struct intel_th_device *thdev)

    disable tracing for an output device

    :param thdev:
        output device that requests tracing be disabled
    :type thdev: struct intel_th_device \*

.. This file was automatic generated / don't edit.

