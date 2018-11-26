.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_device_info.c

.. _`intel_device_info_runtime_init`:

intel_device_info_runtime_init
==============================

.. c:function:: void intel_device_info_runtime_init(struct intel_device_info *info)

    initialize runtime info

    :param info:
        intel device info struct
    :type info: struct intel_device_info \*

.. _`intel_device_info_runtime_init.description`:

Description
-----------

Determine various intel_device_info fields at runtime.

.. _`intel_device_info_runtime_init.use-it-when-either`:

Use it when either
------------------

- it's judged too laborious to fill n static structures with the limit
when a simple if statement does the job,
- run-time checks (eg read fuse/strap registers) are needed.

.. _`intel_device_info_runtime_init.this-function-needs-to-be-called`:

This function needs to be called
--------------------------------

- after the MMIO has been setup as we are reading registers,
- after the PCH has been detected,
- before the first usage of the fields it can tweak.

.. This file was automatic generated / don't edit.

