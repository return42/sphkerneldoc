.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/mips.c

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

.. This file was automatic generated / don't edit.

