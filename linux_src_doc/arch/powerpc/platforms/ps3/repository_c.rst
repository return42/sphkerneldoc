.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/ps3/repository.c

.. _`make_first_field`:

make_first_field
================

.. c:function:: u64 make_first_field(const char *text, u64 index)

    Make the first field of a repository node name.

    :param const char \*text:
        Text portion of the field.

    :param u64 index:
        Numeric index portion of the field.  Use zero for 'don't care'.

.. _`make_first_field.description`:

Description
-----------

This routine sets the vendor id to zero (non-vendor specific).
Returns field value.

.. _`make_field`:

make_field
==========

.. c:function:: u64 make_field(const char *text, u64 index)

    Make subsequent fields of a repository node name.

    :param const char \*text:
        Text portion of the field.  Use "" for 'don't care'.

    :param u64 index:
        Numeric index portion of the field.  Use zero for 'don't care'.

.. _`make_field.description`:

Description
-----------

Returns field value.

.. _`read_node`:

read_node
=========

.. c:function:: int read_node(unsigned int lpar_id, u64 n1, u64 n2, u64 n3, u64 n4, u64 *_v1, u64 *_v2)

    Read a repository node from raw fields.

    :param unsigned int lpar_id:
        *undescribed*

    :param u64 n1:
        First field of node name.

    :param u64 n2:
        Second field of node name.  Use zero for 'don't care'.

    :param u64 n3:
        Third field of node name.  Use zero for 'don't care'.

    :param u64 n4:
        Fourth field of node name.  Use zero for 'don't care'.

    :param u64 \*_v1:
        *undescribed*

    :param u64 \*_v2:
        *undescribed*

.. _`ps3_repository_read_num_pu`:

ps3_repository_read_num_pu
==========================

.. c:function:: int ps3_repository_read_num_pu(u64 *num_pu)

    Number of logical PU processors for this lpar.

    :param u64 \*num_pu:
        *undescribed*

.. _`ps3_repository_read_pu_id`:

ps3_repository_read_pu_id
=========================

.. c:function:: int ps3_repository_read_pu_id(unsigned int pu_index, u64 *pu_id)

    Read the logical PU id.

    :param unsigned int pu_index:
        Zero based index.

    :param u64 \*pu_id:
        The logical PU id.

.. _`ps3_repository_read_mm_info`:

ps3_repository_read_mm_info
===========================

.. c:function:: int ps3_repository_read_mm_info(u64 *rm_base, u64 *rm_size, u64 *region_total)

    Read mm info for single pu system.

    :param u64 \*rm_base:
        Real mode memory base address.

    :param u64 \*rm_size:
        Real mode memory size.

    :param u64 \*region_total:
        Maximum memory region size.

.. _`ps3_repository_read_highmem_region_count`:

ps3_repository_read_highmem_region_count
========================================

.. c:function:: int ps3_repository_read_highmem_region_count(unsigned int *region_count)

    Read the number of highmem regions

    :param unsigned int \*region_count:
        *undescribed*

.. _`ps3_repository_read_highmem_region_count.description`:

Description
-----------

Bootloaders must arrange the repository nodes such that regions are indexed
with a region_index from 0 to region_count-1.

.. _`ps3_repository_read_highmem_info`:

ps3_repository_read_highmem_info
================================

.. c:function:: int ps3_repository_read_highmem_info(unsigned int region_index, u64 *highmem_base, u64 *highmem_size)

    Read high memory region info

    :param unsigned int region_index:
        Region index, {0,..,region_count-1}.

    :param u64 \*highmem_base:
        High memory base address.

    :param u64 \*highmem_size:
        High memory size.

.. _`ps3_repository_read_highmem_info.description`:

Description
-----------

Bootloaders that preallocate highmem regions must place the
region info into the repository at these well known nodes.

.. _`ps3_repository_read_num_spu_reserved`:

ps3_repository_read_num_spu_reserved
====================================

.. c:function:: int ps3_repository_read_num_spu_reserved(unsigned int *num_spu_reserved)

    Number of physical spus reserved.

    :param unsigned int \*num_spu_reserved:
        *undescribed*

.. _`ps3_repository_read_num_spu_resource_id`:

ps3_repository_read_num_spu_resource_id
=======================================

.. c:function:: int ps3_repository_read_num_spu_resource_id(unsigned int *num_resource_id)

    Number of spu resource reservations.

    :param unsigned int \*num_resource_id:
        Number of spu resource ids.

.. _`ps3_repository_read_spu_resource_id`:

ps3_repository_read_spu_resource_id
===================================

.. c:function:: int ps3_repository_read_spu_resource_id(unsigned int res_index, enum ps3_spu_resource_type *resource_type, unsigned int *resource_id)

    spu resource reservation id value.

    :param unsigned int res_index:
        Resource reservation index.

    :param enum ps3_spu_resource_type \*resource_type:
        Resource reservation type.

    :param unsigned int \*resource_id:
        Resource reservation id.

.. _`ps3_repository_read_boot_dat_info`:

ps3_repository_read_boot_dat_info
=================================

.. c:function:: int ps3_repository_read_boot_dat_info(u64 *lpar_addr, unsigned int *size)

    Get address and size of cell_ext_os_area.

    :param u64 \*lpar_addr:
        *undescribed*

    :param unsigned int \*size:
        size of cell_ext_os_area

.. _`ps3_repository_read_boot_dat_info.address`:

address
-------

lpar address of cell_ext_os_area

.. _`ps3_repository_read_num_be`:

ps3_repository_read_num_be
==========================

.. c:function:: int ps3_repository_read_num_be(unsigned int *num_be)

    Number of physical BE processors in the system.

    :param unsigned int \*num_be:
        *undescribed*

.. _`ps3_repository_read_be_node_id`:

ps3_repository_read_be_node_id
==============================

.. c:function:: int ps3_repository_read_be_node_id(unsigned int be_index, u64 *node_id)

    Read the physical BE processor node id.

    :param unsigned int be_index:
        Zero based index.

    :param u64 \*node_id:
        The BE processor node id.

.. _`ps3_repository_read_be_id`:

ps3_repository_read_be_id
=========================

.. c:function:: int ps3_repository_read_be_id(u64 node_id, u64 *be_id)

    Read the physical BE processor id.

    :param u64 node_id:
        The BE processor node id.

    :param u64 \*be_id:
        The BE processor id.

.. This file was automatic generated / don't edit.

