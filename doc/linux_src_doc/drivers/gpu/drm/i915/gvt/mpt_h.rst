.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/mpt.h

.. _`intel_gvt_hypervisor_detect_host`:

intel_gvt_hypervisor_detect_host
================================

.. c:function:: int intel_gvt_hypervisor_detect_host( void)

    check if GVT-g is running within hypervisor host/privilged domain

    :param  void:
        no arguments

.. _`intel_gvt_hypervisor_detect_host.return`:

Return
------

Zero on success, -ENODEV if current kernel is running inside a VM

.. This file was automatic generated / don't edit.

