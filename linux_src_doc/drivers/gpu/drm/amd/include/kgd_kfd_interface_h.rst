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
        int (*init_gtt_mem_allocation)(struct kgd_dev *kgd, size_t size,void **mem_obj, uint64_t *gpu_addr, void **cpu_ptr);
        void (*free_gtt_mem)(struct kgd_dev *kgd, void *mem_obj);
        void (*get_local_mem_info)(struct kgd_dev *kgd, struct kfd_local_mem_info *mem_info);
        uint64_t (*get_gpu_clock_counter)(struct kgd_dev *kgd);
        uint32_t (*get_max_engine_clock_in_mhz)(struct kgd_dev *kgd);
        int (*alloc_pasid)(unsigned int bits);
        void (*free_pasid)(unsigned int pasid);
        void (*program_sh_mem_settings)(struct kgd_dev *kgd, uint32_t vmid,uint32_t sh_mem_config, uint32_t sh_mem_ape1_base, uint32_t sh_mem_ape1_limit, uint32_t sh_mem_bases);
        int (*set_pasid_vmid_mapping)(struct kgd_dev *kgd, unsigned int pasid, unsigned int vmid);
        int (*init_interrupts)(struct kgd_dev *kgd, uint32_t pipe_id);
        int (*hqd_load)(struct kgd_dev *kgd, void *mqd, uint32_t pipe_id,uint32_t queue_id, uint32_t __user *wptr,uint32_t wptr_shift, uint32_t wptr_mask, struct mm_struct *mm);
        int (*hqd_sdma_load)(struct kgd_dev *kgd, void *mqd, uint32_t __user *wptr, struct mm_struct *mm);
        int (*hqd_dump)(struct kgd_dev *kgd,uint32_t pipe_id, uint32_t queue_id, uint32_t (**dump)[2], uint32_t *n_regs);
        int (*hqd_sdma_dump)(struct kgd_dev *kgd,uint32_t engine_id, uint32_t queue_id, uint32_t (**dump)[2], uint32_t *n_regs);
        bool (*hqd_is_occupied)(struct kgd_dev *kgd, uint64_t queue_address, uint32_t pipe_id, uint32_t queue_id);
        int (*hqd_destroy)(struct kgd_dev *kgd, void *mqd, uint32_t reset_type,unsigned int timeout, uint32_t pipe_id, uint32_t queue_id);
        bool (*hqd_sdma_is_occupied)(struct kgd_dev *kgd, void *mqd);
        int (*hqd_sdma_destroy)(struct kgd_dev *kgd, void *mqd, unsigned int timeout);
        int (*address_watch_disable)(struct kgd_dev *kgd);
        int (*address_watch_execute)(struct kgd_dev *kgd,unsigned int watch_point_id,uint32_t cntl_val,uint32_t addr_hi, uint32_t addr_lo);
        int (*wave_control_execute)(struct kgd_dev *kgd,uint32_t gfx_index_val, uint32_t sq_cmd);
        uint32_t (*address_watch_get_offset)(struct kgd_dev *kgd,unsigned int watch_point_id, unsigned int reg_offset);
        bool (*get_atc_vmid_pasid_mapping_valid)(struct kgd_dev *kgd, uint8_t vmid);
        uint16_t (*get_atc_vmid_pasid_mapping_pasid)(struct kgd_dev *kgd, uint8_t vmid);
        uint16_t (*get_fw_version)(struct kgd_dev *kgd, enum kgd_engine_type type);
        void (*set_scratch_backing_va)(struct kgd_dev *kgd, uint64_t va, uint32_t vmid);
        int (*get_tile_config)(struct kgd_dev *kgd, struct tile_config *config);
        void (*get_cu_info)(struct kgd_dev *kgd, struct kfd_cu_info *cu_info);
        uint64_t (*get_vram_usage)(struct kgd_dev *kgd);
        int (*create_process_vm)(struct kgd_dev *kgd, void **vm, void **process_info, struct dma_fence **ef);
        int (*acquire_process_vm)(struct kgd_dev *kgd, struct file *filp, void **vm, void **process_info, struct dma_fence **ef);
        void (*destroy_process_vm)(struct kgd_dev *kgd, void *vm);
        uint32_t (*get_process_page_dir)(void *vm);
        void (*set_vm_context_page_table_base)(struct kgd_dev *kgd, uint32_t vmid, uint32_t page_table_base);
        int (*alloc_memory_of_gpu)(struct kgd_dev *kgd, uint64_t va,uint64_t size, void *vm,struct kgd_mem **mem, uint64_t *offset, uint32_t flags);
        int (*free_memory_of_gpu)(struct kgd_dev *kgd, struct kgd_mem *mem);
        int (*map_memory_to_gpu)(struct kgd_dev *kgd, struct kgd_mem *mem, void *vm);
        int (*unmap_memory_to_gpu)(struct kgd_dev *kgd, struct kgd_mem *mem, void *vm);
        int (*sync_memory)(struct kgd_dev *kgd, struct kgd_mem *mem, bool intr);
        int (*map_gtt_bo_to_kernel)(struct kgd_dev *kgd, struct kgd_mem *mem, void **kptr, uint64_t *size);
        int (*restore_process_bos)(void *process_info, struct dma_fence **ef);
        int (*invalidate_tlbs)(struct kgd_dev *kgd, uint16_t pasid);
        int (*invalidate_tlbs_vmid)(struct kgd_dev *kgd, uint16_t vmid);
        int (*submit_ib)(struct kgd_dev *kgd, enum kgd_engine_type engine,uint32_t vmid, uint64_t gpu_addr, uint32_t *ib_cmd, uint32_t ib_len);
    }

.. _`kfd2kgd_calls.members`:

Members
-------

init_gtt_mem_allocation
    Allocate a buffer on the gart aperture.
    The buffer can be used for mqds, hpds, kernel queue, fence and runlists

free_gtt_mem
    Frees a buffer that was allocated on the gart aperture

get_local_mem_info
    Retrieves information about GPU local memory

get_gpu_clock_counter
    Retrieves GPU clock counter

get_max_engine_clock_in_mhz
    Retrieves maximum GPU clock in MHz

alloc_pasid
    Allocate a PASID

free_pasid
    Free a PASID

program_sh_mem_settings
    A function that should initiate the memory
    properties such as main aperture memory type (cache / non cached) and
    secondary aperture base address, size and memory type.
    This function is used only for no cp scheduling mode.

set_pasid_vmid_mapping
    Exposes pasid/vmid pair to the H/W for no cp
    scheduling mode. Only used for no cp scheduling mode.

init_interrupts
    *undescribed*

hqd_load
    Loads the mqd structure to a H/W hqd slot. used only for no cp
    sceduling mode.

hqd_sdma_load
    Loads the SDMA mqd structure to a H/W SDMA hqd slot.
    used only for no HWS mode.

hqd_dump
    Dumps CPC HQD registers to an array of address-value pairs.
    Array is allocated with kmalloc, needs to be freed with kfree by caller.

hqd_sdma_dump
    Dumps SDMA HQD registers to an array of address-value pairs.
    Array is allocated with kmalloc, needs to be freed with kfree by caller.

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

get_fw_version
    Returns FW versions from the header

set_scratch_backing_va
    Sets VA for scratch backing memory of a VMID.
    Only used for no cp scheduling mode

get_tile_config
    Returns GPU-specific tiling mode information

get_cu_info
    Retrieves activated cu info

get_vram_usage
    Returns current VRAM usage

create_process_vm
    Create a VM address space for a given process and GPU

acquire_process_vm
    *undescribed*

destroy_process_vm
    Destroy a VM

get_process_page_dir
    Get physical address of a VM page directory

set_vm_context_page_table_base
    Program page table base for a VMID

alloc_memory_of_gpu
    Allocate GPUVM memory

free_memory_of_gpu
    Free GPUVM memory

map_memory_to_gpu
    Map GPUVM memory into a specific VM address
    space. Allocates and updates page tables and page directories as
    needed. This function may return before all page table updates have
    completed. This allows multiple map operations (on multiple GPUs)
    to happen concurrently. Use sync_memory to synchronize with all
    pending updates.

unmap_memory_to_gpu
    *undescribed*

sync_memory
    Wait for pending page table updates to complete

map_gtt_bo_to_kernel
    Map a GTT BO for kernel access
    Pins the BO, maps it to kernel address space. Such BOs are never evicted.
    The kernel virtual address remains valid until the BO is freed.

restore_process_bos
    Restore all BOs that belong to the
    process. This is intended for restoring memory mappings after a TTM
    eviction.

invalidate_tlbs
    Invalidate TLBs for a specific PASID

invalidate_tlbs_vmid
    Invalidate TLBs for a specific VMID

submit_ib
    Submits an IB to the engine specified by inserting the
    IB to the corresponding ring (ring type). The IB is executed with the
    specified VMID in a user mode context.

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
        struct kfd_dev* (*probe)(struct kgd_dev *kgd, struct pci_dev *pdev, const struct kfd2kgd_calls *f2g);
        bool (*device_init)(struct kfd_dev *kfd, const struct kgd2kfd_shared_resources *gpu_resources);
        void (*device_exit)(struct kfd_dev *kfd);
        void (*interrupt)(struct kfd_dev *kfd, const void *ih_ring_entry);
        void (*suspend)(struct kfd_dev *kfd);
        int (*resume)(struct kfd_dev *kfd);
        int (*quiesce_mm)(struct mm_struct *mm);
        int (*resume_mm)(struct mm_struct *mm);
        int (*schedule_evict_and_restore_process)(struct mm_struct *mm, struct dma_fence *fence);
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

quiesce_mm
    Quiesce all user queue access to specified MM address space

resume_mm
    Resume user queue access to specified MM address space

schedule_evict_and_restore_process
    Schedules work queue that will prepare
    for safe eviction of KFD BOs that belong to the specified process.

.. _`kgd2kfd_calls.description`:

Description
-----------

This structure contains function callback pointers so the kgd driver
will notify to the amdkfd about certain status changes.

.. This file was automatic generated / don't edit.

