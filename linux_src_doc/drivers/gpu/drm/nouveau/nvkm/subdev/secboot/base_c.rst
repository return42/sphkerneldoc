.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/base.c

.. _`nvkm_secboot_reset`:

nvkm_secboot_reset
==================

.. c:function:: int nvkm_secboot_reset(struct nvkm_secboot *sb, unsigned long falcon_mask)

    reset specified falcon

    :param sb:
        *undescribed*
    :type sb: struct nvkm_secboot \*

    :param falcon_mask:
        *undescribed*
    :type falcon_mask: unsigned long

.. _`nvkm_secboot_is_managed`:

nvkm_secboot_is_managed
=======================

.. c:function:: bool nvkm_secboot_is_managed(struct nvkm_secboot *sb, enum nvkm_secboot_falcon fid)

    check whether a given falcon is securely-managed

    :param sb:
        *undescribed*
    :type sb: struct nvkm_secboot \*

    :param fid:
        *undescribed*
    :type fid: enum nvkm_secboot_falcon

.. This file was automatic generated / don't edit.

