.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/core/firmware.c

.. _`nvkm_firmware_get`:

nvkm_firmware_get
=================

.. c:function:: int nvkm_firmware_get(struct nvkm_device *device, const char *fwname, const struct firmware **fw)

    load firmware from the official nvidia/chip/ directory \ ``device``\       device that will use that firmware \ ``fwname``\       name of firmware file to load \ ``fw``\           firmware structure to load to

    :param device:
        *undescribed*
    :type device: struct nvkm_device \*

    :param fwname:
        *undescribed*
    :type fwname: const char \*

    :param fw:
        *undescribed*
    :type fw: const struct firmware \*\*

.. _`nvkm_firmware_get.description`:

Description
-----------

Use this function to load firmware files in the form nvidia/chip/fwname.bin.
Firmware files released by NVIDIA will always follow this format.

.. _`nvkm_firmware_put`:

nvkm_firmware_put
=================

.. c:function:: void nvkm_firmware_put(const struct firmware *fw)

    release firmware loaded with nvkm_firmware_get

    :param fw:
        *undescribed*
    :type fw: const struct firmware \*

.. This file was automatic generated / don't edit.

