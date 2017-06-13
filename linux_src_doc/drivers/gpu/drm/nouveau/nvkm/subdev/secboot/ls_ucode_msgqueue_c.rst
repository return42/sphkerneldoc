.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/ls_ucode_msgqueue.c

.. _`acr_ls_ucode_load_msgqueue`:

acr_ls_ucode_load_msgqueue
==========================

.. c:function:: int acr_ls_ucode_load_msgqueue(const struct nvkm_subdev *subdev, const char *name, struct ls_ucode_img *img)

    load and prepare a ucode img for a msgqueue fw

    :param const struct nvkm_subdev \*subdev:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param struct ls_ucode_img \*img:
        *undescribed*

.. _`acr_ls_ucode_load_msgqueue.description`:

Description
-----------

Load the LS microcode, desc and signature and pack them into a single
blob.

.. This file was automatic generated / don't edit.

