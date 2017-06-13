.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/ls_ucode_gr.c

.. _`ls_ucode_img_build`:

ls_ucode_img_build
==================

.. c:function:: void *ls_ucode_img_build(const struct firmware *bl, const struct firmware *code, const struct firmware *data, struct ls_ucode_img_desc *desc)

    :param const struct firmware \*bl:
        bootloader image, including 16-bytes descriptor

    :param const struct firmware \*code:
        LS firmware code segment

    :param const struct firmware \*data:
        LS firmware data segment

    :param struct ls_ucode_img_desc \*desc:
        ucode descriptor to be written

.. _`ls_ucode_img_build.return`:

Return
------

allocated ucode image with corresponding descriptor information. desc
is also updated to contain the right offsets within returned image.

.. _`ls_ucode_img_load_gr`:

ls_ucode_img_load_gr
====================

.. c:function:: int ls_ucode_img_load_gr(const struct nvkm_subdev *subdev, struct ls_ucode_img *img, const char *falcon_name)

    load and prepare a LS GR ucode image

    :param const struct nvkm_subdev \*subdev:
        *undescribed*

    :param struct ls_ucode_img \*img:
        *undescribed*

    :param const char \*falcon_name:
        *undescribed*

.. _`ls_ucode_img_load_gr.description`:

Description
-----------

Load the LS microcode, bootloader and signature and pack them into a single
blob. Also generate the corresponding ucode descriptor.

.. This file was automatic generated / don't edit.

