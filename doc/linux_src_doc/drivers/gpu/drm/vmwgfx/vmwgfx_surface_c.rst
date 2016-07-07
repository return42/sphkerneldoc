.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_surface.c

.. _`vmw_user_surface`:

struct vmw_user_surface
=======================

.. c:type:: struct vmw_user_surface

    User-space visible surface resource

.. _`vmw_user_surface.definition`:

Definition
----------

.. code-block:: c

    struct vmw_user_surface {
        struct ttm_prime_object prime;
        struct vmw_surface srf;
        uint32_t size;
        struct drm_master *master;
        struct ttm_base_object *backup_base;
    }

.. _`vmw_user_surface.members`:

Members
-------

prime
    *undescribed*

srf
    The surface metadata.

size
    TTM accounting size for the surface.

master
    master of the creating client. Used for security check.

backup_base
    *undescribed*

.. _`vmw_surface_offset`:

struct vmw_surface_offset
=========================

.. c:type:: struct vmw_surface_offset

    Backing store mip level offset info

.. _`vmw_surface_offset.definition`:

Definition
----------

.. code-block:: c

    struct vmw_surface_offset {
        uint32_t face;
        uint32_t mip;
        uint32_t bo_offset;
    }

.. _`vmw_surface_offset.members`:

Members
-------

face
    Surface face.

mip
    Mip level.

bo_offset
    Offset into backing store of this mip level.

.. _`vmw_surface_dma`:

struct vmw_surface_dma
======================

.. c:type:: struct vmw_surface_dma

    SVGA3D DMA command

.. _`vmw_surface_dma.definition`:

Definition
----------

.. code-block:: c

    struct vmw_surface_dma {
        SVGA3dCmdHeader header;
        SVGA3dCmdSurfaceDMA body;
        SVGA3dCopyBox cb;
        SVGA3dCmdSurfaceDMASuffix suffix;
    }

.. _`vmw_surface_dma.members`:

Members
-------

header
    *undescribed*

body
    *undescribed*

cb
    *undescribed*

suffix
    *undescribed*

.. _`vmw_surface_define`:

struct vmw_surface_define
=========================

.. c:type:: struct vmw_surface_define

    SVGA3D Surface Define command

.. _`vmw_surface_define.definition`:

Definition
----------

.. code-block:: c

    struct vmw_surface_define {
        SVGA3dCmdHeader header;
        SVGA3dCmdDefineSurface body;
    }

.. _`vmw_surface_define.members`:

Members
-------

header
    *undescribed*

body
    *undescribed*

.. _`vmw_surface_destroy`:

struct vmw_surface_destroy
==========================

.. c:type:: struct vmw_surface_destroy

    SVGA3D Surface Destroy command

.. _`vmw_surface_destroy.definition`:

Definition
----------

.. code-block:: c

    struct vmw_surface_destroy {
        SVGA3dCmdHeader header;
        SVGA3dCmdDestroySurface body;
    }

.. _`vmw_surface_destroy.members`:

Members
-------

header
    *undescribed*

body
    *undescribed*

.. _`vmw_surface_dma_size`:

vmw_surface_dma_size
====================

.. c:function:: uint32_t vmw_surface_dma_size(const struct vmw_surface *srf)

    Compute fifo size for a dma command.

    :param const struct vmw_surface \*srf:
        Pointer to a struct vmw_surface

.. _`vmw_surface_dma_size.description`:

Description
-----------

Computes the required size for a surface dma command for backup or
restoration of the surface represented by \ ``srf``\ .

.. _`vmw_surface_define_size`:

vmw_surface_define_size
=======================

.. c:function:: uint32_t vmw_surface_define_size(const struct vmw_surface *srf)

    Compute fifo size for a surface define command.

    :param const struct vmw_surface \*srf:
        Pointer to a struct vmw_surface

.. _`vmw_surface_define_size.description`:

Description
-----------

Computes the required size for a surface define command for the definition
of the surface represented by \ ``srf``\ .

.. _`vmw_surface_destroy_size`:

vmw_surface_destroy_size
========================

.. c:function:: uint32_t vmw_surface_destroy_size( void)

    Compute fifo size for a surface destroy command.

    :param  void:
        no arguments

.. _`vmw_surface_destroy_size.description`:

Description
-----------

Computes the required size for a surface destroy command for the destruction
of a hw surface.

.. _`vmw_surface_destroy_encode`:

vmw_surface_destroy_encode
==========================

.. c:function:: void vmw_surface_destroy_encode(uint32_t id, void *cmd_space)

    Encode a surface_destroy command.

    :param uint32_t id:
        The surface id

    :param void \*cmd_space:
        Pointer to memory area in which the commands should be encoded.

.. _`vmw_surface_define_encode`:

vmw_surface_define_encode
=========================

.. c:function:: void vmw_surface_define_encode(const struct vmw_surface *srf, void *cmd_space)

    Encode a surface_define command.

    :param const struct vmw_surface \*srf:
        Pointer to a struct vmw_surface object.

    :param void \*cmd_space:
        Pointer to memory area in which the commands should be encoded.

.. _`vmw_surface_dma_encode`:

vmw_surface_dma_encode
======================

.. c:function:: void vmw_surface_dma_encode(struct vmw_surface *srf, void *cmd_space, const SVGAGuestPtr *ptr, bool to_surface)

    Encode a surface_dma command.

    :param struct vmw_surface \*srf:
        Pointer to a struct vmw_surface object.

    :param void \*cmd_space:
        Pointer to memory area in which the commands should be encoded.

    :param const SVGAGuestPtr \*ptr:
        Pointer to an SVGAGuestPtr indicating where the surface contents
        should be placed or read from.

    :param bool to_surface:
        Boolean whether to DMA to the surface or from the surface.

.. _`vmw_hw_surface_destroy`:

vmw_hw_surface_destroy
======================

.. c:function:: void vmw_hw_surface_destroy(struct vmw_resource *res)

    destroy a Device surface

    :param struct vmw_resource \*res:
        Pointer to a struct vmw_resource embedded in a struct
        vmw_surface.

.. _`vmw_hw_surface_destroy.description`:

Description
-----------

Destroys a the device surface associated with a struct vmw_surface if
any, and adjusts accounting and resource count accordingly.

.. _`vmw_legacy_srf_create`:

vmw_legacy_srf_create
=====================

.. c:function:: int vmw_legacy_srf_create(struct vmw_resource *res)

    Create a device surface as part of the resource validation process.

    :param struct vmw_resource \*res:
        Pointer to a struct vmw_surface.

.. _`vmw_legacy_srf_create.description`:

Description
-----------

If the surface doesn't have a hw id.

Returns -EBUSY if there wasn't sufficient device resources to
complete the validation. Retry after freeing up resources.

May return other errors if the kernel is out of guest resources.

.. _`vmw_legacy_srf_dma`:

vmw_legacy_srf_dma
==================

.. c:function:: int vmw_legacy_srf_dma(struct vmw_resource *res, struct ttm_validate_buffer *val_buf, bool bind)

    Copy backup data to or from a legacy surface.

    :param struct vmw_resource \*res:
        Pointer to a struct vmw_res embedded in a struct
        vmw_surface.

    :param struct ttm_validate_buffer \*val_buf:
        Pointer to a struct ttm_validate_buffer containing
        information about the backup buffer.

    :param bool bind:
        Boolean wether to DMA to the surface.

.. _`vmw_legacy_srf_dma.description`:

Description
-----------

Transfer backup data to or from a legacy surface as part of the
validation process.
May return other errors if the kernel is out of guest resources.
The backup buffer will be fenced or idle upon successful completion,
and if the surface needs persistent backup storage, the backup buffer
will also be returned reserved iff \ ``bind``\  is true.

.. _`vmw_legacy_srf_bind`:

vmw_legacy_srf_bind
===================

.. c:function:: int vmw_legacy_srf_bind(struct vmw_resource *res, struct ttm_validate_buffer *val_buf)

    Perform a legacy surface bind as part of the surface validation process.

    :param struct vmw_resource \*res:
        Pointer to a struct vmw_res embedded in a struct
        vmw_surface.

    :param struct ttm_validate_buffer \*val_buf:
        Pointer to a struct ttm_validate_buffer containing
        information about the backup buffer.

.. _`vmw_legacy_srf_bind.description`:

Description
-----------

This function will copy backup data to the surface if the
backup buffer is dirty.

.. _`vmw_legacy_srf_unbind`:

vmw_legacy_srf_unbind
=====================

.. c:function:: int vmw_legacy_srf_unbind(struct vmw_resource *res, bool readback, struct ttm_validate_buffer *val_buf)

    Perform a legacy surface unbind as part of the surface eviction process.

    :param struct vmw_resource \*res:
        Pointer to a struct vmw_res embedded in a struct
        vmw_surface.

    :param bool readback:
        *undescribed*

    :param struct ttm_validate_buffer \*val_buf:
        Pointer to a struct ttm_validate_buffer containing
        information about the backup buffer.

.. _`vmw_legacy_srf_unbind.description`:

Description
-----------

This function will copy backup data from the surface.

.. _`vmw_legacy_srf_destroy`:

vmw_legacy_srf_destroy
======================

.. c:function:: int vmw_legacy_srf_destroy(struct vmw_resource *res)

    Destroy a device surface as part of a resource eviction process.

    :param struct vmw_resource \*res:
        Pointer to a struct vmw_res embedded in a struct
        vmw_surface.

.. _`vmw_surface_init`:

vmw_surface_init
================

.. c:function:: int vmw_surface_init(struct vmw_private *dev_priv, struct vmw_surface *srf, void (*) res_free (struct vmw_resource *res)

    initialize a struct vmw_surface

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_surface \*srf:
        Pointer to the struct vmw_surface to initialize.

    :param (void (\*) res_free (struct vmw_resource \*res):
        Pointer to a resource destructor used to free
        the object.

.. _`vmw_user_surface_base_to_res`:

vmw_user_surface_base_to_res
============================

.. c:function:: struct vmw_resource *vmw_user_surface_base_to_res(struct ttm_base_object *base)

    TTM base object to resource converter for user visible surfaces

    :param struct ttm_base_object \*base:
        Pointer to a TTM base object

.. _`vmw_user_surface_base_to_res.description`:

Description
-----------

Returns the struct vmw_resource embedded in a struct vmw_surface
for the user-visible object identified by the TTM base object \ ``base``\ .

.. _`vmw_user_surface_free`:

vmw_user_surface_free
=====================

.. c:function:: void vmw_user_surface_free(struct vmw_resource *res)

    User visible surface resource destructor

    :param struct vmw_resource \*res:
        A struct vmw_resource embedded in a struct vmw_surface.

.. _`vmw_user_surface_base_release`:

vmw_user_surface_base_release
=============================

.. c:function:: void vmw_user_surface_base_release(struct ttm_base_object **p_base)

    User visible surface TTM base object destructor

    :param struct ttm_base_object \*\*p_base:
        Pointer to a pointer to a TTM base object
        embedded in a struct vmw_user_surface.

.. _`vmw_user_surface_base_release.description`:

Description
-----------

Drops the base object's reference on its resource, and the
pointer pointed to by \*p_base is set to NULL.

.. _`vmw_surface_destroy_ioctl`:

vmw_surface_destroy_ioctl
=========================

.. c:function:: int vmw_surface_destroy_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Ioctl function implementing the user surface destroy functionality.

    :param struct drm_device \*dev:
        Pointer to a struct drm_device.

    :param void \*data:
        Pointer to data copied from / to user-space.

    :param struct drm_file \*file_priv:
        Pointer to a drm file private structure.

.. _`vmw_surface_define_ioctl`:

vmw_surface_define_ioctl
========================

.. c:function:: int vmw_surface_define_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Ioctl function implementing the user surface define functionality.

    :param struct drm_device \*dev:
        Pointer to a struct drm_device.

    :param void \*data:
        Pointer to data copied from / to user-space.

    :param struct drm_file \*file_priv:
        Pointer to a drm file private structure.

.. _`vmw_surface_reference_ioctl`:

vmw_surface_reference_ioctl
===========================

.. c:function:: int vmw_surface_reference_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Ioctl function implementing the user surface reference functionality.

    :param struct drm_device \*dev:
        Pointer to a struct drm_device.

    :param void \*data:
        Pointer to data copied from / to user-space.

    :param struct drm_file \*file_priv:
        Pointer to a drm file private structure.

.. _`vmw_gb_surface_create`:

vmw_gb_surface_create
=====================

.. c:function:: int vmw_gb_surface_create(struct vmw_resource *res)

    Encode a surface_define command.

    :param struct vmw_resource \*res:
        *undescribed*

.. _`vmw_gb_surface_define_ioctl`:

vmw_gb_surface_define_ioctl
===========================

.. c:function:: int vmw_gb_surface_define_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Ioctl function implementing the user surface define functionality.

    :param struct drm_device \*dev:
        Pointer to a struct drm_device.

    :param void \*data:
        Pointer to data copied from / to user-space.

    :param struct drm_file \*file_priv:
        Pointer to a drm file private structure.

.. _`vmw_gb_surface_reference_ioctl`:

vmw_gb_surface_reference_ioctl
==============================

.. c:function:: int vmw_gb_surface_reference_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Ioctl function implementing the user surface reference functionality.

    :param struct drm_device \*dev:
        Pointer to a struct drm_device.

    :param void \*data:
        Pointer to data copied from / to user-space.

    :param struct drm_file \*file_priv:
        Pointer to a drm file private structure.

.. _`vmw_surface_gb_priv_define`:

vmw_surface_gb_priv_define
==========================

.. c:function:: int vmw_surface_gb_priv_define(struct drm_device *dev, uint32_t user_accounting_size, uint32_t svga3d_flags, SVGA3dSurfaceFormat format, bool for_scanout, uint32_t num_mip_levels, uint32_t multisample_count, uint32_t array_size, struct drm_vmw_size size, struct vmw_surface **srf_out)

    Define a private GB surface

    :param struct drm_device \*dev:
        Pointer to a struct drm_device

    :param uint32_t user_accounting_size:
        Used to track user-space memory usage, set
        to 0 for kernel mode only memory

    :param uint32_t svga3d_flags:
        SVGA3d surface flags for the device

    :param SVGA3dSurfaceFormat format:
        requested surface format

    :param bool for_scanout:
        true if inteded to be used for scanout buffer

    :param uint32_t num_mip_levels:
        number of MIP levels

    :param uint32_t multisample_count:
        *undescribed*

    :param uint32_t array_size:
        Surface array size.

    :param struct drm_vmw_size size:
        width, heigh, depth of the surface requested

    :param struct vmw_surface \*\*srf_out:
        *undescribed*

.. _`vmw_surface_gb_priv_define.description`:

Description
-----------

GB surfaces allocated by this function will not have a user mode handle, and
thus will only be visible to vmwgfx.  For optimization reasons the
surface may later be given a user mode handle by another function to make
it available to user mode drivers.

.. This file was automatic generated / don't edit.

