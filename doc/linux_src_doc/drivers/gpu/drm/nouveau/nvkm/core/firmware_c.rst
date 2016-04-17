.. -*- coding: utf-8; mode: rst -*-

==========
firmware.c
==========


.. _`nvkm_firmware_get`:

nvkm_firmware_get
=================

.. c:function:: int nvkm_firmware_get (struct nvkm_device *device, const char *fwname, const struct firmware **fw)

    load firmware from the official nvidia/chip/ directory @device device that will use that firmware @fwname name of firmware file to load @fw firmware structure to load to

    :param struct nvkm_device \*device:

        *undescribed*

    :param const char \*fwname:

        *undescribed*

    :param const struct firmware \*\*fw:

        *undescribed*



.. _`nvkm_firmware_get.description`:

Description
-----------


Use this function to load firmware files in the form nvidia/chip/fwname.bin.
Firmware files released by NVIDIA will always follow this format.



.. _`nvkm_firmware_put`:

nvkm_firmware_put
=================

.. c:function:: void nvkm_firmware_put (const struct firmware *fw)

    release firmware loaded with nvkm_firmware_get

    :param const struct firmware \*fw:

        *undescribed*

