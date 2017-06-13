.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/arm.c

.. _`kvm_arm_get_running_vcpu`:

kvm_arm_get_running_vcpu
========================

.. c:function:: struct kvm_vcpu *kvm_arm_get_running_vcpu( void)

    get the vcpu running on the current CPU. Must be called from non-preemptible context

    :param  void:
        no arguments

.. _`kvm_get_running_vcpus`:

kvm_get_running_vcpus
=====================

.. c:function:: struct kvm_vcpu * __percpu *kvm_get_running_vcpus( void)

    get the per-CPU array of currently running vcpus.

    :param  void:
        no arguments

.. _`kvm_arch_init_vm`:

kvm_arch_init_vm
================

.. c:function:: int kvm_arch_init_vm(struct kvm *kvm, unsigned long type)

    initializes a VM data structure

    :param struct kvm \*kvm:
        pointer to the KVM struct

    :param unsigned long type:
        *undescribed*

.. _`kvm_arch_destroy_vm`:

kvm_arch_destroy_vm
===================

.. c:function:: void kvm_arch_destroy_vm(struct kvm *kvm)

    destroy the VM data structure

    :param struct kvm \*kvm:
        pointer to the KVM struct

.. _`kvm_arch_vcpu_runnable`:

kvm_arch_vcpu_runnable
======================

.. c:function:: int kvm_arch_vcpu_runnable(struct kvm_vcpu *v)

    determine if the vcpu can be scheduled

    :param struct kvm_vcpu \*v:
        The VCPU pointer

.. _`kvm_arch_vcpu_runnable.description`:

Description
-----------

If the guest CPU is not waiting for interrupts or an interrupt line is
asserted, the CPU is by definition runnable.

.. _`need_new_vmid_gen`:

need_new_vmid_gen
=================

.. c:function:: bool need_new_vmid_gen(struct kvm *kvm)

    check that the VMID is still valid

    :param struct kvm \*kvm:
        The VM's VMID to check

.. _`need_new_vmid_gen.description`:

Description
-----------

return true if there is a new generation of VMIDs being used

The hardware supports only 256 values with the value zero reserved for the
host, so we check if an assigned value belongs to a previous generation,
which which requires us to assign a new value. If we're the first to use a
VMID for the new generation, we must flush necessary caches and TLBs on all
CPUs.

.. _`update_vttbr`:

update_vttbr
============

.. c:function:: void update_vttbr(struct kvm *kvm)

    Update the VTTBR with a valid VMID before the guest runs \ ``kvm``\  The guest that we are about to run

    :param struct kvm \*kvm:
        *undescribed*

.. _`update_vttbr.description`:

Description
-----------

Called from kvm_arch_vcpu_ioctl_run before entering the guest to ensure the
VM has a valid VMID, otherwise assigns a new one and flushes corresponding
caches and TLBs.

.. _`kvm_arch_vcpu_ioctl_run`:

kvm_arch_vcpu_ioctl_run
=======================

.. c:function:: int kvm_arch_vcpu_ioctl_run(struct kvm_vcpu *vcpu, struct kvm_run *run)

    the main VCPU run function to execute guest code

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

    :param struct kvm_run \*run:
        The kvm_run structure pointer used for userspace state exchange

.. _`kvm_arch_vcpu_ioctl_run.description`:

Description
-----------

This function is called through the VCPU_RUN ioctl called from user space. It
will execute VM code in a loop until the time slice for the process is used
or some emulation is needed from user space in which case the function will
return with return value 0 and with the kvm_run structure filled in with the
required data for the requested emulation.

.. _`kvm_vm_ioctl_get_dirty_log`:

kvm_vm_ioctl_get_dirty_log
==========================

.. c:function:: int kvm_vm_ioctl_get_dirty_log(struct kvm *kvm, struct kvm_dirty_log *log)

    get and clear the log of dirty pages in a slot

    :param struct kvm \*kvm:
        kvm instance

    :param struct kvm_dirty_log \*log:
        slot id and address to which we copy the log

.. _`kvm_vm_ioctl_get_dirty_log.description`:

Description
-----------

Steps 1-4 below provide general overview of dirty page logging. See
\ :c:func:`kvm_get_dirty_log_protect`\  function description for additional details.

We call \ :c:func:`kvm_get_dirty_log_protect`\  to handle steps 1-3, upon return we
always flush the TLB (step 4) even if previous step failed  and the dirty
bitmap may be corrupt. Regardless of previous outcome the KVM logging API
does not preclude user space subsequent dirty log read. Flushing TLB ensures
writes will be marked dirty for next log read.

1. Take a snapshot of the bit and clear it if needed.
2. Write protect the corresponding page.
3. Copy the snapshot to the userspace.
4. Flush TLB's if needed.

.. _`init_hyp_mode`:

init_hyp_mode
=============

.. c:function:: int init_hyp_mode( void)

    mode on all online CPUs

    :param  void:
        no arguments

.. _`kvm_arch_init`:

kvm_arch_init
=============

.. c:function:: int kvm_arch_init(void *opaque)

    mode and memory mappings on all CPUs.

    :param void \*opaque:
        *undescribed*

.. This file was automatic generated / don't edit.

