.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/mdt_loader.c

.. _`qcom_mdt_get_size`:

qcom_mdt_get_size
=================

.. c:function:: ssize_t qcom_mdt_get_size(const struct firmware *fw)

    acquire size of the memory region needed to load mdt

    :param fw:
        firmware object for the mdt file
    :type fw: const struct firmware \*

.. _`qcom_mdt_get_size.description`:

Description
-----------

Returns size of the loaded firmware blob, or -EINVAL on failure.

.. _`qcom_mdt_load`:

qcom_mdt_load
=============

.. c:function:: int qcom_mdt_load(struct device *dev, const struct firmware *fw, const char *firmware, int pas_id, void *mem_region, phys_addr_t mem_phys, size_t mem_size, phys_addr_t *reloc_base)

    load the firmware which header is loaded as fw

    :param dev:
        device handle to associate resources with
    :type dev: struct device \*

    :param fw:
        firmware object for the mdt file
    :type fw: const struct firmware \*

    :param firmware:
        name of the firmware, for construction of segment file names
    :type firmware: const char \*

    :param pas_id:
        PAS identifier
    :type pas_id: int

    :param mem_region:
        allocated memory region to load firmware into
    :type mem_region: void \*

    :param mem_phys:
        physical address of allocated memory region
    :type mem_phys: phys_addr_t

    :param mem_size:
        size of the allocated memory region
    :type mem_size: size_t

    :param reloc_base:
        adjusted physical address after relocation
    :type reloc_base: phys_addr_t \*

.. _`qcom_mdt_load.description`:

Description
-----------

Returns 0 on success, negative errno otherwise.

.. _`qcom_mdt_load_no_init`:

qcom_mdt_load_no_init
=====================

.. c:function:: int qcom_mdt_load_no_init(struct device *dev, const struct firmware *fw, const char *firmware, int pas_id, void *mem_region, phys_addr_t mem_phys, size_t mem_size, phys_addr_t *reloc_base)

    load the firmware which header is loaded as fw

    :param dev:
        device handle to associate resources with
    :type dev: struct device \*

    :param fw:
        firmware object for the mdt file
    :type fw: const struct firmware \*

    :param firmware:
        name of the firmware, for construction of segment file names
    :type firmware: const char \*

    :param pas_id:
        PAS identifier
    :type pas_id: int

    :param mem_region:
        allocated memory region to load firmware into
    :type mem_region: void \*

    :param mem_phys:
        physical address of allocated memory region
    :type mem_phys: phys_addr_t

    :param mem_size:
        size of the allocated memory region
    :type mem_size: size_t

    :param reloc_base:
        adjusted physical address after relocation
    :type reloc_base: phys_addr_t \*

.. _`qcom_mdt_load_no_init.description`:

Description
-----------

Returns 0 on success, negative errno otherwise.

.. This file was automatic generated / don't edit.

