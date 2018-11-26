.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/ps3/repository.c

.. _`make_first_field`:

make_first_field
================

.. c:function:: u64 make_first_field(const char *text, u64 index)

    Make the first field of a repository node name.

    :param text:
        Text portion of the field.
    :type text: const char \*

    :param index:
        Numeric index portion of the field.  Use zero for 'don't care'.
    :type index: u64

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

    :param text:
        Text portion of the field.  Use "" for 'don't care'.
    :type text: const char \*

    :param index:
        Numeric index portion of the field.  Use zero for 'don't care'.
    :type index: u64

.. _`make_field.description`:

Description
-----------

Returns field value.

.. _`read_node`:

read_node
=========

.. c:function:: int read_node(unsigned int lpar_id, u64 n1, u64 n2, u64 n3, u64 n4, u64 *_v1, u64 *_v2)

    Read a repository node from raw fields.

    :param lpar_id:
        *undescribed*
    :type lpar_id: unsigned int

    :param n1:
        First field of node name.
    :type n1: u64

    :param n2:
        Second field of node name.  Use zero for 'don't care'.
    :type n2: u64

    :param n3:
        Third field of node name.  Use zero for 'don't care'.
    :type n3: u64

    :param n4:
        Fourth field of node name.  Use zero for 'don't care'.
    :type n4: u64

    :param _v1:
        *undescribed*
    :type _v1: u64 \*

    :param _v2:
        *undescribed*
    :type _v2: u64 \*

.. _`ps3_repository_read_num_pu`:

ps3_repository_read_num_pu
==========================

.. c:function:: int ps3_repository_read_num_pu(u64 *num_pu)

    Number of logical PU processors for this lpar.

    :param num_pu:
        *undescribed*
    :type num_pu: u64 \*

.. _`ps3_repository_read_pu_id`:

ps3_repository_read_pu_id
=========================

.. c:function:: int ps3_repository_read_pu_id(unsigned int pu_index, u64 *pu_id)

    Read the logical PU id.

    :param pu_index:
        Zero based index.
    :type pu_index: unsigned int

    :param pu_id:
        The logical PU id.
    :type pu_id: u64 \*

.. _`ps3_repository_read_mm_info`:

ps3_repository_read_mm_info
===========================

.. c:function:: int ps3_repository_read_mm_info(u64 *rm_base, u64 *rm_size, u64 *region_total)

    Read mm info for single pu system.

    :param rm_base:
        Real mode memory base address.
    :type rm_base: u64 \*

    :param rm_size:
        Real mode memory size.
    :type rm_size: u64 \*

    :param region_total:
        Maximum memory region size.
    :type region_total: u64 \*

.. _`ps3_repository_read_highmem_region_count`:

ps3_repository_read_highmem_region_count
========================================

.. c:function:: int ps3_repository_read_highmem_region_count(unsigned int *region_count)

    Read the number of highmem regions

    :param region_count:
        *undescribed*
    :type region_count: unsigned int \*

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

    :param region_index:
        Region index, {0,..,region_count-1}.
    :type region_index: unsigned int

    :param highmem_base:
        High memory base address.
    :type highmem_base: u64 \*

    :param highmem_size:
        High memory size.
    :type highmem_size: u64 \*

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

    :param num_spu_reserved:
        *undescribed*
    :type num_spu_reserved: unsigned int \*

.. _`ps3_repository_read_num_spu_resource_id`:

ps3_repository_read_num_spu_resource_id
=======================================

.. c:function:: int ps3_repository_read_num_spu_resource_id(unsigned int *num_resource_id)

    Number of spu resource reservations.

    :param num_resource_id:
        Number of spu resource ids.
    :type num_resource_id: unsigned int \*

.. _`ps3_repository_read_spu_resource_id`:

ps3_repository_read_spu_resource_id
===================================

.. c:function:: int ps3_repository_read_spu_resource_id(unsigned int res_index, enum ps3_spu_resource_type *resource_type, unsigned int *resource_id)

    spu resource reservation id value.

    :param res_index:
        Resource reservation index.
    :type res_index: unsigned int

    :param resource_type:
        Resource reservation type.
    :type resource_type: enum ps3_spu_resource_type \*

    :param resource_id:
        Resource reservation id.
    :type resource_id: unsigned int \*

.. _`ps3_repository_read_boot_dat_info`:

ps3_repository_read_boot_dat_info
=================================

.. c:function:: int ps3_repository_read_boot_dat_info(u64 *lpar_addr, unsigned int *size)

    Get address and size of cell_ext_os_area.

    :param lpar_addr:
        *undescribed*
    :type lpar_addr: u64 \*

    :param size:
        size of cell_ext_os_area
    :type size: unsigned int \*

.. _`ps3_repository_read_boot_dat_info.address`:

address
-------

lpar address of cell_ext_os_area

.. _`ps3_repository_read_num_be`:

ps3_repository_read_num_be
==========================

.. c:function:: int ps3_repository_read_num_be(unsigned int *num_be)

    Number of physical BE processors in the system.

    :param num_be:
        *undescribed*
    :type num_be: unsigned int \*

.. _`ps3_repository_read_be_node_id`:

ps3_repository_read_be_node_id
==============================

.. c:function:: int ps3_repository_read_be_node_id(unsigned int be_index, u64 *node_id)

    Read the physical BE processor node id.

    :param be_index:
        Zero based index.
    :type be_index: unsigned int

    :param node_id:
        The BE processor node id.
    :type node_id: u64 \*

.. _`ps3_repository_read_be_id`:

ps3_repository_read_be_id
=========================

.. c:function:: int ps3_repository_read_be_id(u64 node_id, u64 *be_id)

    Read the physical BE processor id.

    :param node_id:
        The BE processor node id.
    :type node_id: u64

    :param be_id:
        The BE processor id.
    :type be_id: u64 \*

.. This file was automatic generated / don't edit.

