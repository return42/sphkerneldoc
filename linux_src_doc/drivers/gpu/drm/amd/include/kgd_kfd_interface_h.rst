.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/include/kgd_kfd_interface.h

.. _`kfd2kgd_calls`:

struct kfd2kgd_calls
====================

.. c:type:: struct kfd2kgd_calls


.. _`kfd2kgd_calls.definition`:

Definition
----------

.. code-block:: c

    struct kfd2kgd_calls {
        int (*init_gtt_mem_allocation)(struct kgd_dev *kgd, size_t size,void **mem_obj, uint64_t *gpu_addr,void **cpu_ptr);
        void (*free_gtt_mem)(struct kgd_dev *kgd, void *mem_obj);
        uint64_t (*get_vmem_size)(struct kgd_dev *kgd);
        uint64_t (*get_gpu_clock_counter)(struct kgd_dev *kgd);
        uint32_t (*get_max_engine_clock_in_mhz)(struct kgd_dev *kgd);
        void (*program_sh_mem_settings)(struct kgd_dev *kgd, uint32_t vmid,uint32_t sh_mem_config, uint32_t sh_mem_ape1_base,uint32_t sh_mem_ape1_limit, uint32_t sh_mem_bases);
        int (*set_pasid_vmid_mapping)(struct kgd_dev *kgd, unsigned int pasid,unsigned int vmid);
        int (*init_pipeline)(struct kgd_dev *kgd, uint32_t pipe_id,uint32_t hpd_size, uint64_t hpd_gpu_addr);
        int (*init_interrupts)(struct kgd_dev *kgd, uint32_t pipe_id);
        int (*hqd_load)(struct kgd_dev *kgd, void *mqd, uint32_t pipe_id,uint32_t queue_id, uint32_t __user *wptr);
        int (*hqd_sdma_load)(struct kgd_dev *kgd, void *mqd);
        bool (*hqd_is_occupied)(struct kgd_dev *kgd, uint64_t queue_address,uint32_t pipe_id, uint32_t queue_id);
        int (*hqd_destroy)(struct kgd_dev *kgd, uint32_t reset_type,unsigned int timeout, uint32_t pipe_id,uint32_t queue_id);
        bool (*hqd_sdma_is_occupied)(struct kgd_dev *kgd, void *mqd);
        int (*hqd_sdma_destroy)(struct kgd_dev *kgd, void *mqd,unsigned int timeout);
        int (*address_watch_disable)(struct kgd_dev *kgd);
        int (*address_watch_execute)(struct kgd_dev *kgd,unsigned int watch_point_id,uint32_t cntl_val,uint32_t addr_hi,uint32_t addr_lo);
        int (*wave_control_execute)(struct kgd_dev *kgd,uint32_t gfx_index_val,uint32_t sq_cmd);
        uint32_t (*address_watch_get_offset)(struct kgd_dev *kgd,unsigned int watch_point_id,unsigned int reg_offset);
        bool (*get_atc_vmid_pasid_mapping_valid)(struct kgd_dev *kgd,uint8_t vmid);
        uint16_t (*get_atc_vmid_pasid_mapping_pasid)(struct kgd_dev *kgd,uint8_t vmid);
        void (*write_vmid_invalidate_request)(struct kgd_dev *kgd,uint8_t vmid);
        uint16_t (*get_fw_version)(struct kgd_dev *kgd,enum kgd_engine_type type);
    }

.. _`kfd2kgd_calls.members`:

Members
-------

init_gtt_mem_allocation
    Allocate a buffer on the gart aperture.
    The buffer can be used for mqds, hpds, kernel queue, fence and runlists

free_gtt_mem
    Frees a buffer that was allocated on the gart aperture

get_vmem_size
    Retrieves (physical) size of VRAM

get_gpu_clock_counter
    Retrieves GPU clock counter

get_max_engine_clock_in_mhz
    Retrieves maximum GPU clock in MHz

program_sh_mem_settings
    A function that should initiate the memory
    properties such as main aperture memory type (cache / non cached) and
    secondary aperture base address, size and memory type.
    This function is used only for no cp scheduling mode.

set_pasid_vmid_mapping
    Exposes pasid/vmid pair to the H/W for no cp
    scheduling mode. Only used for no cp scheduling mode.

init_pipeline
    Initialized the compute pipelines.

init_interrupts
    *undescribed*

hqd_load
    Loads the mqd structure to a H/W hqd slot. used only for no cp
    sceduling mode.

hqd_sdma_load
    Loads the SDMA mqd structure to a H/W SDMA hqd slot.
    used only for no HWS mode.

hqd_is_occupied
    *undescribed*

hqd_destroy
    Destructs and preempts the queue assigned to that hqd slot.

hqd_sdma_is_occupied
    Checks if an SDMA hqd slot is occupied.

hqd_sdma_destroy
    Destructs and preempts the SDMA queue assigned to that
    SDMA hqd slot.

address_watch_disable
    *undescribed*

address_watch_execute
    *undescribed*

wave_control_execute
    *undescribed*

address_watch_get_offset
    *undescribed*

get_atc_vmid_pasid_mapping_valid
    *undescribed*

get_atc_vmid_pasid_mapping_pasid
    *undescribed*

write_vmid_invalidate_request
    *undescribed*

get_fw_version
    Returns FW versions from the header

.. _`kfd2kgd_calls.description`:

Description
-----------

This structure contains function pointers to services that the kgd driver
provides to amdkfd driver.

.. _`kgd2kfd_calls`:

struct kgd2kfd_calls
====================

.. c:type:: struct kgd2kfd_calls


.. _`kgd2kfd_calls.definition`:

Definition
----------

.. code-block:: c

    struct kgd2kfd_calls {
        void (*exit)(void);
        struct kfd_dev* (*probe)(struct kgd_dev *kgd, struct pci_dev *pdev,const struct kfd2kgd_calls *f2g);
        bool (*device_init)(struct kfd_dev *kfd,const struct kgd2kfd_shared_resources *gpu_resources);
        void (*device_exit)(struct kfd_dev *kfd);
        void (*interrupt)(struct kfd_dev *kfd, const void *ih_ring_entry);
        void (*suspend)(struct kfd_dev *kfd);
        int (*resume)(struct kfd_dev *kfd);
    }

.. _`kgd2kfd_calls.members`:

Members
-------

exit
    Notifies amdkfd that kgd module is unloaded

probe
    Notifies amdkfd about a probe done on a device in the kgd driver.

device_init
    Initialize the newly probed device (if it is a device that
    amdkfd supports)

device_exit
    Notifies amdkfd about a removal of a kgd device

interrupt
    *undescribed*

suspend
    Notifies amdkfd about a suspend action done to a kgd device

resume
    Notifies amdkfd about a resume action done to a kgd device

.. _`kgd2kfd_calls.description`:

Description
-----------

This structure contains function callback pointers so the kgd driver
will notify to the amdkfd about certain status changes.

.. This file was automatic generated / don't edit.

