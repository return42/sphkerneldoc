.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/remoteproc_elf_loader.c

.. _`rproc_elf_sanity_check`:

rproc_elf_sanity_check
======================

.. c:function:: int rproc_elf_sanity_check(struct rproc *rproc, const struct firmware *fw)

    Sanity Check ELF firmware image

    :param rproc:
        the remote processor handle
    :type rproc: struct rproc \*

    :param fw:
        the ELF firmware image
    :type fw: const struct firmware \*

.. _`rproc_elf_sanity_check.description`:

Description
-----------

Make sure this fw image is sane.

.. _`rproc_elf_get_boot_addr`:

rproc_elf_get_boot_addr
=======================

.. c:function:: u32 rproc_elf_get_boot_addr(struct rproc *rproc, const struct firmware *fw)

    Get rproc's boot address.

    :param rproc:
        the remote processor handle
    :type rproc: struct rproc \*

    :param fw:
        the ELF firmware image
    :type fw: const struct firmware \*

.. _`rproc_elf_get_boot_addr.description`:

Description
-----------

This function returns the entry point address of the ELF
image.

Note that the boot address is not a configurable property of all remote
processors. Some will always boot at a specific hard-coded address.

.. _`rproc_elf_load_segments`:

rproc_elf_load_segments
=======================

.. c:function:: int rproc_elf_load_segments(struct rproc *rproc, const struct firmware *fw)

    load firmware segments to memory

    :param rproc:
        remote processor which will be booted using these fw segments
    :type rproc: struct rproc \*

    :param fw:
        the ELF firmware image
    :type fw: const struct firmware \*

.. _`rproc_elf_load_segments.description`:

Description
-----------

This function loads the firmware segments to memory, where the remote
processor expects them.

Some remote processors will expect their code and data to be placed
in specific device addresses, and can't have them dynamically assigned.

We currently support only those kind of remote processors, and expect
the program header's paddr member to contain those addresses. We then go
through the physically contiguous "carveout" memory regions which we
allocated (and mapped) earlier on behalf of the remote processor,
and "translate" device address to kernel addresses, so we can copy the
segments where they are expected.

Currently we only support remote processors that required carveout
allocations and got them mapped onto their iommus. Some processors

.. _`rproc_elf_load_segments.might-be-different`:

might be different
------------------

they might not have iommus, and would prefer to
directly allocate memory for every segment/resource. This is not yet
supported, though.

.. _`rproc_elf_load_rsc_table`:

rproc_elf_load_rsc_table
========================

.. c:function:: int rproc_elf_load_rsc_table(struct rproc *rproc, const struct firmware *fw)

    load the resource table

    :param rproc:
        the rproc handle
    :type rproc: struct rproc \*

    :param fw:
        the ELF firmware image
    :type fw: const struct firmware \*

.. _`rproc_elf_load_rsc_table.description`:

Description
-----------

This function finds the resource table inside the remote processor's
firmware, load it into the \ ``cached_table``\  and update \ ``table_ptr``\ .

.. _`rproc_elf_load_rsc_table.return`:

Return
------

0 on success, negative errno on failure.

.. _`rproc_elf_find_loaded_rsc_table`:

rproc_elf_find_loaded_rsc_table
===============================

.. c:function:: struct resource_table *rproc_elf_find_loaded_rsc_table(struct rproc *rproc, const struct firmware *fw)

    find the loaded resource table

    :param rproc:
        the rproc handle
    :type rproc: struct rproc \*

    :param fw:
        the ELF firmware image
    :type fw: const struct firmware \*

.. _`rproc_elf_find_loaded_rsc_table.description`:

Description
-----------

This function finds the location of the loaded resource table. Don't
call this function if the table wasn't loaded yet - it's a bug if you do.

Returns the pointer to the resource table if it is found or NULL otherwise.
If the table wasn't loaded yet the result is unspecified.

.. This file was automatic generated / don't edit.

