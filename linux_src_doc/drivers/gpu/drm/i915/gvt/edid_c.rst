.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/edid.c

.. _`intel_gvt_i2c_handle_gmbus_read`:

intel_gvt_i2c_handle_gmbus_read
===============================

.. c:function:: int intel_gvt_i2c_handle_gmbus_read(struct intel_vgpu *vgpu, unsigned int offset, void *p_data, unsigned int bytes)

    emulate gmbus register mmio read

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param offset:
        reg offset
    :type offset: unsigned int

    :param p_data:
        data return buffer
    :type p_data: void \*

    :param bytes:
        access data length
    :type bytes: unsigned int

.. _`intel_gvt_i2c_handle_gmbus_read.description`:

Description
-----------

This function is used to emulate gmbus register mmio read

.. _`intel_gvt_i2c_handle_gmbus_read.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_i2c_handle_gmbus_write`:

intel_gvt_i2c_handle_gmbus_write
================================

.. c:function:: int intel_gvt_i2c_handle_gmbus_write(struct intel_vgpu *vgpu, unsigned int offset, void *p_data, unsigned int bytes)

    emulate gmbus register mmio write

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param offset:
        reg offset
    :type offset: unsigned int

    :param p_data:
        data return buffer
    :type p_data: void \*

    :param bytes:
        access data length
    :type bytes: unsigned int

.. _`intel_gvt_i2c_handle_gmbus_write.description`:

Description
-----------

This function is used to emulate gmbus register mmio write

.. _`intel_gvt_i2c_handle_gmbus_write.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_i2c_handle_aux_ch_write`:

intel_gvt_i2c_handle_aux_ch_write
=================================

.. c:function:: void intel_gvt_i2c_handle_aux_ch_write(struct intel_vgpu *vgpu, int port_idx, unsigned int offset, void *p_data)

    emulate AUX channel register write

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param port_idx:
        port index
    :type port_idx: int

    :param offset:
        reg offset
    :type offset: unsigned int

    :param p_data:
        write ptr
    :type p_data: void \*

.. _`intel_gvt_i2c_handle_aux_ch_write.description`:

Description
-----------

This function is used to emulate AUX channel register write

.. _`intel_vgpu_init_i2c_edid`:

intel_vgpu_init_i2c_edid
========================

.. c:function:: void intel_vgpu_init_i2c_edid(struct intel_vgpu *vgpu)

    initialize vGPU i2c edid emulation

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_init_i2c_edid.description`:

Description
-----------

This function is used to initialize vGPU i2c edid emulation stuffs

.. This file was automatic generated / don't edit.

