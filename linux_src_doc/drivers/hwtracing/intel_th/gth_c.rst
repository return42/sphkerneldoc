.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/intel_th/gth.c

.. _`gth_output`:

struct gth_output
=================

.. c:type:: struct gth_output

    GTH view on an output port

.. _`gth_output.definition`:

Definition
----------

.. code-block:: c

    struct gth_output {
        struct gth_device *gth;
        struct intel_th_output *output;
        unsigned int index;
        unsigned int port_type;
        unsigned long master[BITS_TO_LONGS(TH_CONFIGURABLE_MASTERS + 1)];
    }

.. _`gth_output.members`:

Members
-------

gth
    backlink to the GTH device

output
    link to output device's output descriptor

index
    output port number

port_type
    one of GTH\_\* port type values

master
    bitmap of masters configured for this output

.. _`gth_device`:

struct gth_device
=================

.. c:type:: struct gth_device

    GTH device

.. _`gth_device.definition`:

Definition
----------

.. code-block:: c

    struct gth_device {
        struct device *dev;
        void __iomem *base;
        struct attribute_group output_group;
        struct attribute_group master_group;
        struct gth_output output[TH_POSSIBLE_OUTPUTS];
        signed char master[TH_CONFIGURABLE_MASTERS + 1];
        spinlock_t gth_lock;
    }

.. _`gth_device.members`:

Members
-------

dev
    driver core's device

base
    register window base address

output_group
    attributes describing output ports

master_group
    attributes describing master assignments

output
    output ports

master
    master/output port assignments

gth_lock
    serializes accesses to GTH bits

.. _`intel_th_gth_disable`:

intel_th_gth_disable
====================

.. c:function:: void intel_th_gth_disable(struct intel_th_device *thdev, struct intel_th_output *output)

    disable tracing to an output device

    :param struct intel_th_device \*thdev:
        GTH device

    :param struct intel_th_output \*output:
        output device's descriptor

.. _`intel_th_gth_disable.description`:

Description
-----------

This will deconfigure all masters set to output to this device,
disable tracing using force storeEn off signal and wait for the
"pipeline empty" bit for corresponding output port.

.. _`intel_th_gth_enable`:

intel_th_gth_enable
===================

.. c:function:: void intel_th_gth_enable(struct intel_th_device *thdev, struct intel_th_output *output)

    enable tracing to an output device

    :param struct intel_th_device \*thdev:
        GTH device

    :param struct intel_th_output \*output:
        output device's descriptor

.. _`intel_th_gth_enable.description`:

Description
-----------

This will configure all masters set to output to this device and
enable tracing using force storeEn signal.

.. _`intel_th_gth_assign`:

intel_th_gth_assign
===================

.. c:function:: int intel_th_gth_assign(struct intel_th_device *thdev, struct intel_th_device *othdev)

    assign output device to a GTH output port

    :param struct intel_th_device \*thdev:
        GTH device

    :param struct intel_th_device \*othdev:
        output device

.. _`intel_th_gth_assign.description`:

Description
-----------

This will match a given output device parameters against present
output ports on the GTH and fill out relevant bits in output device's
descriptor.

.. _`intel_th_gth_assign.return`:

Return
------

0 on success, -errno on error.

.. _`intel_th_gth_unassign`:

intel_th_gth_unassign
=====================

.. c:function:: void intel_th_gth_unassign(struct intel_th_device *thdev, struct intel_th_device *othdev)

    deassociate an output device from its output port

    :param struct intel_th_device \*thdev:
        GTH device

    :param struct intel_th_device \*othdev:
        output device

.. This file was automatic generated / don't edit.

