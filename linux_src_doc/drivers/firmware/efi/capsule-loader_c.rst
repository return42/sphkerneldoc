.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/efi/capsule-loader.c

.. _`efi_free_all_buff_pages`:

efi_free_all_buff_pages
=======================

.. c:function:: void efi_free_all_buff_pages(struct capsule_info *cap_info)

    free all previous allocated buffer pages

    :param cap_info:
        pointer to current instance of capsule_info structure
    :type cap_info: struct capsule_info \*

.. _`efi_free_all_buff_pages.description`:

Description
-----------

In addition to freeing buffer pages, it flags NO_FURTHER_WRITE_ACTION
to cease processing data in subsequent write(2) calls until close(2)
is called.

.. _`efi_capsule_setup_info`:

efi_capsule_setup_info
======================

.. c:function:: int efi_capsule_setup_info(struct capsule_info *cap_info, void *kbuff, size_t hdr_bytes)

    obtain the efi capsule header in the binary and setup capsule_info structure

    :param cap_info:
        pointer to current instance of capsule_info structure
    :type cap_info: struct capsule_info \*

    :param kbuff:
        a mapped first page buffer pointer
    :type kbuff: void \*

    :param hdr_bytes:
        the total received number of bytes for efi header
    :type hdr_bytes: size_t

.. _`efi_capsule_setup_info.description`:

Description
-----------

Platforms with non-standard capsule update mechanisms can override
this \__weak function so they can perform any required capsule
image munging. See \ :c:func:`quark_quirk_function`\  for an example.

.. _`efi_capsule_submit_update`:

efi_capsule_submit_update
=========================

.. c:function:: ssize_t efi_capsule_submit_update(struct capsule_info *cap_info)

    invoke the efi_capsule_update API once binary upload done

    :param cap_info:
        pointer to current instance of capsule_info structure
    :type cap_info: struct capsule_info \*

.. _`efi_capsule_write`:

efi_capsule_write
=================

.. c:function:: ssize_t efi_capsule_write(struct file *file, const char __user *buff, size_t count, loff_t *offp)

    store the capsule binary and pass it to \ :c:func:`efi_capsule_update`\  API

    :param file:
        file pointer
    :type file: struct file \*

    :param buff:
        buffer pointer
    :type buff: const char __user \*

    :param count:
        number of bytes in \ ``buff``\ 
    :type count: size_t

    :param offp:
        not used
    :type offp: loff_t \*

.. _`efi_capsule_write.expectation`:

Expectation
-----------

- A user space tool should start at the beginning of capsule binary and
pass data in sequentially.
- Users should close and re-open this file note in order to upload more
capsules.
- After an error returned, user should close the file and restart the
operation for the next try otherwise -EIO will be returned until the
file is closed.
- An EFI capsule header must be located at the beginning of capsule
binary file and passed in as first block data of write operation.

.. _`efi_capsule_flush`:

efi_capsule_flush
=================

.. c:function:: int efi_capsule_flush(struct file *file, fl_owner_t id)

    called by file close or file flush

    :param file:
        file pointer
    :type file: struct file \*

    :param id:
        not used
    :type id: fl_owner_t

.. _`efi_capsule_flush.description`:

Description
-----------

If a capsule is being partially uploaded then calling this function
will be treated as upload termination and will free those completed
buffer pages and -ECANCELED will be returned.

.. _`efi_capsule_release`:

efi_capsule_release
===================

.. c:function:: int efi_capsule_release(struct inode *inode, struct file *file)

    called by file close

    :param inode:
        not used
    :type inode: struct inode \*

    :param file:
        file pointer
    :type file: struct file \*

.. _`efi_capsule_release.description`:

Description
-----------

We will not free successfully submitted pages since efi update
requires data to be maintained across system reboot.

.. _`efi_capsule_open`:

efi_capsule_open
================

.. c:function:: int efi_capsule_open(struct inode *inode, struct file *file)

    called by file open

    :param inode:
        not used
    :type inode: struct inode \*

    :param file:
        file pointer
    :type file: struct file \*

.. _`efi_capsule_open.description`:

Description
-----------

Will allocate each capsule_info memory for each file open call.
This provided the capability to support multiple file open feature
where user is not needed to wait for others to finish in order to
upload their capsule binary.

.. This file was automatic generated / don't edit.

