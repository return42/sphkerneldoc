.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/dmabuf.h

.. _`intel_vgpu_dmabuf_obj`:

struct intel_vgpu_dmabuf_obj
============================

.. c:type:: struct intel_vgpu_dmabuf_obj

    Intel vGPU device buffer object

.. _`intel_vgpu_dmabuf_obj.definition`:

Definition
----------

.. code-block:: c

    struct intel_vgpu_dmabuf_obj {
        struct intel_vgpu *vgpu;
        struct intel_vgpu_fb_info *info;
        __u32 dmabuf_id;
        struct kref kref;
        bool initref;
        struct list_head list;
    }

.. _`intel_vgpu_dmabuf_obj.members`:

Members
-------

vgpu
    *undescribed*

info
    *undescribed*

dmabuf_id
    *undescribed*

kref
    *undescribed*

initref
    *undescribed*

list
    *undescribed*

.. This file was automatic generated / don't edit.

