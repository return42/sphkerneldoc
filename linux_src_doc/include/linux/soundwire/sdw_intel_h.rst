.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/soundwire/sdw_intel.h

.. _`sdw_intel_ops`:

struct sdw_intel_ops
====================

.. c:type:: struct sdw_intel_ops

    Intel audio driver callback ops

.. _`sdw_intel_ops.definition`:

Definition
----------

.. code-block:: c

    struct sdw_intel_ops {
        int (*config_stream)(void *arg, void *substream, void *dai, void *hw_params, int stream_num);
    }

.. _`sdw_intel_ops.members`:

Members
-------

config_stream
    configure the stream with the hw_params

.. _`sdw_intel_res`:

struct sdw_intel_res
====================

.. c:type:: struct sdw_intel_res

    Soundwire Intel resource structure

.. _`sdw_intel_res.definition`:

Definition
----------

.. code-block:: c

    struct sdw_intel_res {
        void __iomem *mmio_base;
        int irq;
        acpi_handle handle;
        struct device *parent;
        const struct sdw_intel_ops *ops;
        void *arg;
    }

.. _`sdw_intel_res.members`:

Members
-------

mmio_base
    mmio base of SoundWire registers

irq
    interrupt number

handle
    ACPI parent handle

parent
    parent device

ops
    callback ops

arg
    callback arg

.. This file was automatic generated / don't edit.

