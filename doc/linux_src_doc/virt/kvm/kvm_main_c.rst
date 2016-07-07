.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/kvm_main.c

.. _`kvm_get_dirty_log_protect`:

kvm_get_dirty_log_protect
=========================

.. c:function:: int kvm_get_dirty_log_protect(struct kvm *kvm, struct kvm_dirty_log *log, bool *is_dirty)

    get a snapshot of dirty pages, and if any pages are dirty write protect them for next write.

    :param struct kvm \*kvm:
        pointer to kvm instance

    :param struct kvm_dirty_log \*log:
        slot id and address to which we copy the log

    :param bool \*is_dirty:
        flag set if any page is dirty

.. _`kvm_get_dirty_log_protect.description`:

Description
-----------

We need to keep it in mind that VCPU threads can write to the bitmap
concurrently. So, to avoid losing track of dirty pages we keep the

.. _`kvm_get_dirty_log_protect.following-order`:

following order
---------------


1. Take a snapshot of the bit and clear it if needed.
2. Write protect the corresponding page.
3. Copy the snapshot to the userspace.
4. Upon return caller flushes TLB's if needed.

Between 2 and 4, the guest may write to the page using the remaining TLB
entry.  This is not a problem because the page is reported dirty using
the snapshot taken before and step 4 ensures that writes done after
exiting to userspace will be logged for the next call.

.. This file was automatic generated / don't edit.

