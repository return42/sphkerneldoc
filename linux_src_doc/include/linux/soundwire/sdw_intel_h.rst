.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/soundwire/sdw_intel.h

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

.. This file was automatic generated / don't edit.

