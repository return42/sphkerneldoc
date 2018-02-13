.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/intel.h

.. _`sdw_intel_link_res`:

struct sdw_intel_link_res
=========================

.. c:type:: struct sdw_intel_link_res

    Soundwire link resources

.. _`sdw_intel_link_res.definition`:

Definition
----------

.. code-block:: c

    struct sdw_intel_link_res {
        void __iomem *registers;
        void __iomem *shim;
        void __iomem *alh;
        int irq;
    }

.. _`sdw_intel_link_res.members`:

Members
-------

registers
    Link IO registers base

shim
    Audio shim pointer

alh
    ALH (Audio Link Hub) pointer

irq
    Interrupt line

.. _`sdw_intel_link_res.description`:

Description
-----------

This is set as pdata for each link instance.

.. This file was automatic generated / don't edit.

