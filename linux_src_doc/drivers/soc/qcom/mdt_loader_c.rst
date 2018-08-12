.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/mdt_loader.c

.. _`qcom_mdt_get_size`:

qcom_mdt_get_size
=================

.. c:function:: ssize_t qcom_mdt_get_size(const struct firmware *fw)

    acquire size of the memory region needed to load mdt

    :param const struct firmware \*fw:
        firmware object for the mdt file

.. _`qcom_mdt_get_size.description`:

Description
-----------

Returns size of the loaded firmware blob, or -EINVAL on failure.

.. _`qcom_mdt_load`:

qcom_mdt_load
=============

.. c:function:: int qcom_mdt_load(struct device *dev, const struct firmware *fw, const char *firmware, int pas_id, void *mem_region, phys_addr_t mem_phys, size_t mem_size, phys_addr_t *reloc_base)

    load the firmware which header is loaded as fw

    :param struct device \*dev:
        device handle to associate resources with

    :param const struct firmware \*fw:
        firmware object for the mdt file

    :param const char \*firmware:
        name of the firmware, for construction of segment file names

    :param int pas_id:
        PAS identifier

    :param void \*mem_region:
        allocated memory region to load firmware into

    :param phys_addr_t mem_phys:
        physical address of allocated memory region

    :param size_t mem_size:
        size of the allocated memory region

    :param phys_addr_t \*reloc_base:
        adjusted physical address after relocation

.. _`qcom_mdt_load.description`:

Description
-----------

Returns 0 on success, negative errno otherwise.

.. This file was automatic generated / don't edit.

