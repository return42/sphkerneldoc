.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/intel-mid.h

.. _`intel_mid_ops`:

struct intel_mid_ops
====================

.. c:type:: struct intel_mid_ops

    Interface between intel-mid & sub archs

.. _`intel_mid_ops.definition`:

Definition
----------

.. code-block:: c

    struct intel_mid_ops {
        void (*arch_setup)(void);
    }

.. _`intel_mid_ops.members`:

Members
-------

arch_setup
    arch_setup function to re-initialize platform
    structures (x86_init, x86_platform_init)

.. _`intel_mid_ops.description`:

Description
-----------

This structure can be extended if any new interface is required
between intel-mid & its sub arch files.

.. This file was automatic generated / don't edit.

