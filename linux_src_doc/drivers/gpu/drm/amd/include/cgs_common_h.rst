.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/include/cgs_common.h

.. _`cgs_ind_reg`:

enum cgs_ind_reg
================

.. c:type:: enum cgs_ind_reg

    Indirect register spaces

.. _`cgs_ind_reg.definition`:

Definition
----------

.. code-block:: c

    enum cgs_ind_reg {
        CGS_IND_REG__MMIO,
        CGS_IND_REG__PCIE,
        CGS_IND_REG__SMC,
        CGS_IND_REG__UVD_CTX,
        CGS_IND_REG__DIDT,
        CGS_IND_REG_GC_CAC,
        CGS_IND_REG_SE_CAC,
        CGS_IND_REG__AUDIO_ENDPT
    };

.. _`cgs_ind_reg.constants`:

Constants
---------

CGS_IND_REG__MMIO
    *undescribed*

CGS_IND_REG__PCIE
    *undescribed*

CGS_IND_REG__SMC
    *undescribed*

CGS_IND_REG__UVD_CTX
    *undescribed*

CGS_IND_REG__DIDT
    *undescribed*

CGS_IND_REG_GC_CAC
    *undescribed*

CGS_IND_REG_SE_CAC
    *undescribed*

CGS_IND_REG__AUDIO_ENDPT
    *undescribed*

.. _`cgs_firmware_info`:

struct cgs_firmware_info
========================

.. c:type:: struct cgs_firmware_info

    Firmware information

.. _`cgs_firmware_info.definition`:

Definition
----------

.. code-block:: c

    struct cgs_firmware_info {
        uint16_t version;
        uint16_t fw_version;
        uint16_t feature_version;
        uint32_t image_size;
        uint64_t mc_addr;
        uint32_t ucode_start_address;
        void *kptr;
        bool is_kicker;
    }

.. _`cgs_firmware_info.members`:

Members
-------

version
    *undescribed*

fw_version
    *undescribed*

feature_version
    *undescribed*

image_size
    *undescribed*

mc_addr
    *undescribed*

ucode_start_address
    *undescribed*

kptr
    *undescribed*

is_kicker
    *undescribed*

.. _`cgs_read_register_t`:

cgs_read_register_t
===================

.. c:function:: uint32_t cgs_read_register_t(struct cgs_device *cgs_device, unsigned offset)

    Read an MMIO register

    :param cgs_device:
        opaque device handle
    :type cgs_device: struct cgs_device \*

    :param offset:
        register offset
    :type offset: unsigned

.. _`cgs_read_register_t.return`:

Return
------

register value

.. _`cgs_write_register_t`:

cgs_write_register_t
====================

.. c:function:: void cgs_write_register_t(struct cgs_device *cgs_device, unsigned offset, uint32_t value)

    Write an MMIO register

    :param cgs_device:
        opaque device handle
    :type cgs_device: struct cgs_device \*

    :param offset:
        register offset
    :type offset: unsigned

    :param value:
        register value
    :type value: uint32_t

.. _`cgs_read_ind_register_t`:

cgs_read_ind_register_t
=======================

.. c:function:: uint32_t cgs_read_ind_register_t(struct cgs_device *cgs_device, enum cgs_ind_reg space, unsigned index)

    Read an indirect register

    :param cgs_device:
        opaque device handle
    :type cgs_device: struct cgs_device \*

    :param space:
        *undescribed*
    :type space: enum cgs_ind_reg

    :param index:
        *undescribed*
    :type index: unsigned

.. _`cgs_read_ind_register_t.return`:

Return
------

register value

.. _`cgs_write_ind_register_t`:

cgs_write_ind_register_t
========================

.. c:function:: void cgs_write_ind_register_t(struct cgs_device *cgs_device, enum cgs_ind_reg space, unsigned index, uint32_t value)

    Write an indirect register

    :param cgs_device:
        opaque device handle
    :type cgs_device: struct cgs_device \*

    :param space:
        *undescribed*
    :type space: enum cgs_ind_reg

    :param index:
        *undescribed*
    :type index: unsigned

    :param value:
        register value
    :type value: uint32_t

.. This file was automatic generated / don't edit.

