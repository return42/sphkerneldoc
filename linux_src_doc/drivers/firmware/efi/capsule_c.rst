.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/efi/capsule.c

.. _`efi_capsule_pending`:

efi_capsule_pending
===================

.. c:function:: bool efi_capsule_pending(int *reset_type)

    has a capsule been passed to the firmware?

    :param int \*reset_type:
        store the type of EFI reset if capsule is pending

.. _`efi_capsule_pending.description`:

Description
-----------

To ensure that the registered capsule is processed correctly by the
firmware we need to perform a specific type of reset. If a capsule is
pending return the reset type in \ ``reset_type``\ .

This function will race with callers of \ :c:func:`efi_capsule_update`\ , for
example, calling this function while somebody else is in
\ :c:func:`efi_capsule_update`\  but hasn't reached \ :c:func:`efi_capsue_update_locked`\ 
will miss the updates to capsule_pending and efi_reset_type after
\ :c:func:`efi_capsule_update_locked`\  completes.

A non-racy use is from platform reboot code because we use
system_state to ensure no capsules can be sent to the firmware once
we're at SYSTEM_RESTART. See \ :c:func:`efi_capsule_update_locked`\ .

.. _`efi_capsule_supported`:

efi_capsule_supported
=====================

.. c:function:: int efi_capsule_supported(efi_guid_t guid, u32 flags, size_t size, int *reset)

    does the firmware support the capsule?

    :param efi_guid_t guid:
        vendor guid of capsule

    :param u32 flags:
        capsule flags

    :param size_t size:
        size of capsule data

    :param int \*reset:
        the reset type required for this capsule

.. _`efi_capsule_supported.description`:

Description
-----------

Check whether a capsule with \ ``flags``\  is supported by the firmware
and that \ ``size``\  doesn't exceed the maximum size for a capsule.

No attempt is made to check \ ``reset``\  against the reset type required
by any pending capsules because of the races involved.

.. _`efi_capsule_update_locked`:

efi_capsule_update_locked
=========================

.. c:function:: int efi_capsule_update_locked(efi_capsule_header_t *capsule, struct page **sg_pages, int reset)

    pass a single capsule to the firmware

    :param efi_capsule_header_t \*capsule:
        capsule to send to the firmware

    :param struct page \*\*sg_pages:
        array of scatter gather (block descriptor) pages

    :param int reset:
        the reset type required for \ ``capsule``\ 

.. _`efi_capsule_update_locked.description`:

Description
-----------

Since this function must be called under capsule_mutex check
whether efi_reset_type will conflict with \ ``reset``\ , and atomically
set it and capsule_pending if a capsule was successfully sent to
the firmware.

We also check to see if the system is about to restart, and if so,
abort. This avoids races between \ :c:func:`efi_capsule_update`\  and
\ :c:func:`efi_capsule_pending`\ .

.. _`efi_capsule_update`:

efi_capsule_update
==================

.. c:function:: int efi_capsule_update(efi_capsule_header_t *capsule, struct page **pages)

    send a capsule to the firmware

    :param efi_capsule_header_t \*capsule:
        capsule to send to firmware

    :param struct page \*\*pages:
        an array of capsule data pages

.. _`efi_capsule_update.description`:

Description
-----------

Build a scatter gather list with EFI capsule block descriptors to
map the capsule described by \ ``capsule``\  with its data in \ ``pages``\  and
send it to the firmware via the \ :c:func:`UpdateCapsule`\  runtime service.

\ ``capsule``\  must be a virtual mapping of the complete capsule update in the
kernel address space, as the capsule can be consumed immediately.
A capsule_header_t that describes the entire contents of the capsule
must be at the start of the first data page.

Even though this function will validate that the firmware supports
the capsule guid, users will likely want to check that
\ :c:func:`efi_capsule_supported`\  returns true before calling this function
because it makes it easier to print helpful error messages.

If the capsule is successfully submitted to the firmware, any
subsequent calls to \ :c:func:`efi_capsule_pending`\  will return true. \ ``pages``\ 
must not be released or modified if this function returns
successfully.

Callers must be prepared for this function to fail, which can
happen if we raced with system reboot or if there is already a
pending capsule that has a reset type that conflicts with the one
required by \ ``capsule``\ . Do NOT use \ :c:func:`efi_capsule_pending`\  to detect
this conflict since that would be racy. Instead, submit the capsule
to \ :c:func:`efi_capsule_update`\  and check the return value.

Return 0 on success, a converted EFI status code on failure.

.. This file was automatic generated / don't edit.

