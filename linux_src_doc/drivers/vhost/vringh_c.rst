.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/vhost/vringh.c

.. _`vringh_init_user`:

vringh_init_user
================

.. c:function:: int vringh_init_user(struct vringh *vrh, u64 features, unsigned int num, bool weak_barriers, struct vring_desc __user *desc, struct vring_avail __user *avail, struct vring_used __user *used)

    initialize a vringh for a userspace vring.

    :param struct vringh \*vrh:
        the vringh to initialize.

    :param u64 features:
        the feature bits for this ring.

    :param unsigned int num:
        the number of elements.

    :param bool weak_barriers:
        true if we only need memory barriers, not I/O.

    :param struct vring_desc __user \*desc:
        the userpace descriptor pointer.

    :param struct vring_avail __user \*avail:
        the userpace avail pointer.

    :param struct vring_used __user \*used:
        the userpace used pointer.

.. _`vringh_init_user.returns-an-error-if-num-is-invalid`:

Returns an error if num is invalid
----------------------------------

you should check pointers
yourself!

.. _`vringh_getdesc_user`:

vringh_getdesc_user
===================

.. c:function:: int vringh_getdesc_user(struct vringh *vrh, struct vringh_iov *riov, struct vringh_iov *wiov, bool (*getrange)(struct vringh *vrh, u64 addr, struct vringh_range *r), u16 *head)

    get next available descriptor from userspace ring.

    :param struct vringh \*vrh:
        the userspace vring.

    :param struct vringh_iov \*riov:
        where to put the readable descriptors (or NULL)

    :param struct vringh_iov \*wiov:
        where to put the writable descriptors (or NULL)

    :param bool (\*getrange)(struct vringh \*vrh, u64 addr, struct vringh_range \*r):
        function to call to check ranges.

    :param u16 \*head:
        head index we received, for passing to \ :c:func:`vringh_complete_user`\ .

.. _`vringh_getdesc_user.description`:

Description
-----------

Returns 0 if there was no descriptor, 1 if there was, or -errno.

Note that on error return, you can tell the difference between an

.. _`vringh_getdesc_user.invalid-ring-and-a-single-invalid-descriptor`:

invalid ring and a single invalid descriptor
--------------------------------------------

in the former case,
\*head will be vrh->vring.num.  You may be able to ignore an invalid
descriptor, but there's not much you can do with an invalid ring.

Note that you may need to clean up riov and wiov, even on error!

.. _`vringh_iov_pull_user`:

vringh_iov_pull_user
====================

.. c:function:: ssize_t vringh_iov_pull_user(struct vringh_iov *riov, void *dst, size_t len)

    copy bytes from vring_iov.

    :param struct vringh_iov \*riov:
        the riov as passed to \ :c:func:`vringh_getdesc_user`\  (updated as we consume)

    :param void \*dst:
        the place to copy.

    :param size_t len:
        the maximum length to copy.

.. _`vringh_iov_pull_user.description`:

Description
-----------

Returns the bytes copied <= len or a negative errno.

.. _`vringh_iov_push_user`:

vringh_iov_push_user
====================

.. c:function:: ssize_t vringh_iov_push_user(struct vringh_iov *wiov, const void *src, size_t len)

    copy bytes into vring_iov.

    :param struct vringh_iov \*wiov:
        the wiov as passed to \ :c:func:`vringh_getdesc_user`\  (updated as we consume)

    :param const void \*src:
        *undescribed*

    :param size_t len:
        the maximum length to copy.

.. _`vringh_iov_push_user.description`:

Description
-----------

Returns the bytes copied <= len or a negative errno.

.. _`vringh_abandon_user`:

vringh_abandon_user
===================

.. c:function:: void vringh_abandon_user(struct vringh *vrh, unsigned int num)

    we've decided not to handle the descriptor(s).

    :param struct vringh \*vrh:
        the vring.

    :param unsigned int num:
        the number of descriptors to put back (ie. num
        \ :c:func:`vringh_get_user`\  to undo).

.. _`vringh_abandon_user.description`:

Description
-----------

The next \ :c:func:`vringh_get_user`\  will return the old descriptor(s) again.

.. _`vringh_complete_user`:

vringh_complete_user
====================

.. c:function:: int vringh_complete_user(struct vringh *vrh, u16 head, u32 len)

    we've finished with descriptor, publish it.

    :param struct vringh \*vrh:
        the vring.

    :param u16 head:
        the head as filled in by vringh_getdesc_user.

    :param u32 len:
        the length of data we have written.

.. _`vringh_complete_user.description`:

Description
-----------

You should check \ :c:func:`vringh_need_notify_user`\  after one or more calls
to this function.

.. _`vringh_complete_multi_user`:

vringh_complete_multi_user
==========================

.. c:function:: int vringh_complete_multi_user(struct vringh *vrh, const struct vring_used_elem used[], unsigned num_used)

    we've finished with many descriptors.

    :param struct vringh \*vrh:
        the vring.

    :param const struct vring_used_elem used:
        the head, length pairs.

    :param unsigned num_used:
        the number of used elements.

.. _`vringh_complete_multi_user.description`:

Description
-----------

You should check \ :c:func:`vringh_need_notify_user`\  after one or more calls
to this function.

.. _`vringh_notify_enable_user`:

vringh_notify_enable_user
=========================

.. c:function:: bool vringh_notify_enable_user(struct vringh *vrh)

    we want to know if something changes.

    :param struct vringh \*vrh:
        the vring.

.. _`vringh_notify_enable_user.description`:

Description
-----------

This always enables notifications, but returns false if there are
now more buffers available in the vring.

.. _`vringh_notify_disable_user`:

vringh_notify_disable_user
==========================

.. c:function:: void vringh_notify_disable_user(struct vringh *vrh)

    don't tell us if something changes.

    :param struct vringh \*vrh:
        the vring.

.. _`vringh_notify_disable_user.this-is-our-normal-running-state`:

This is our normal running state
--------------------------------

we disable and then only enable when
we're going to sleep.

.. _`vringh_need_notify_user`:

vringh_need_notify_user
=======================

.. c:function:: int vringh_need_notify_user(struct vringh *vrh)

    must we tell the other side about used buffers?

    :param struct vringh \*vrh:
        the vring we've called \ :c:func:`vringh_complete_user`\  on.

.. _`vringh_need_notify_user.description`:

Description
-----------

Returns -errno or 0 if we don't need to tell the other side, 1 if we do.

.. _`vringh_init_kern`:

vringh_init_kern
================

.. c:function:: int vringh_init_kern(struct vringh *vrh, u64 features, unsigned int num, bool weak_barriers, struct vring_desc *desc, struct vring_avail *avail, struct vring_used *used)

    initialize a vringh for a kernelspace vring.

    :param struct vringh \*vrh:
        the vringh to initialize.

    :param u64 features:
        the feature bits for this ring.

    :param unsigned int num:
        the number of elements.

    :param bool weak_barriers:
        true if we only need memory barriers, not I/O.

    :param struct vring_desc \*desc:
        the userpace descriptor pointer.

    :param struct vring_avail \*avail:
        the userpace avail pointer.

    :param struct vring_used \*used:
        the userpace used pointer.

.. _`vringh_init_kern.description`:

Description
-----------

Returns an error if num is invalid.

.. _`vringh_getdesc_kern`:

vringh_getdesc_kern
===================

.. c:function:: int vringh_getdesc_kern(struct vringh *vrh, struct vringh_kiov *riov, struct vringh_kiov *wiov, u16 *head, gfp_t gfp)

    get next available descriptor from kernelspace ring.

    :param struct vringh \*vrh:
        the kernelspace vring.

    :param struct vringh_kiov \*riov:
        where to put the readable descriptors (or NULL)

    :param struct vringh_kiov \*wiov:
        where to put the writable descriptors (or NULL)

    :param u16 \*head:
        head index we received, for passing to \ :c:func:`vringh_complete_kern`\ .

    :param gfp_t gfp:
        flags for allocating larger riov/wiov.

.. _`vringh_getdesc_kern.description`:

Description
-----------

Returns 0 if there was no descriptor, 1 if there was, or -errno.

Note that on error return, you can tell the difference between an

.. _`vringh_getdesc_kern.invalid-ring-and-a-single-invalid-descriptor`:

invalid ring and a single invalid descriptor
--------------------------------------------

in the former case,
\*head will be vrh->vring.num.  You may be able to ignore an invalid
descriptor, but there's not much you can do with an invalid ring.

Note that you may need to clean up riov and wiov, even on error!

.. _`vringh_iov_pull_kern`:

vringh_iov_pull_kern
====================

.. c:function:: ssize_t vringh_iov_pull_kern(struct vringh_kiov *riov, void *dst, size_t len)

    copy bytes from vring_iov.

    :param struct vringh_kiov \*riov:
        the riov as passed to \ :c:func:`vringh_getdesc_kern`\  (updated as we consume)

    :param void \*dst:
        the place to copy.

    :param size_t len:
        the maximum length to copy.

.. _`vringh_iov_pull_kern.description`:

Description
-----------

Returns the bytes copied <= len or a negative errno.

.. _`vringh_iov_push_kern`:

vringh_iov_push_kern
====================

.. c:function:: ssize_t vringh_iov_push_kern(struct vringh_kiov *wiov, const void *src, size_t len)

    copy bytes into vring_iov.

    :param struct vringh_kiov \*wiov:
        the wiov as passed to \ :c:func:`vringh_getdesc_kern`\  (updated as we consume)

    :param const void \*src:
        *undescribed*

    :param size_t len:
        the maximum length to copy.

.. _`vringh_iov_push_kern.description`:

Description
-----------

Returns the bytes copied <= len or a negative errno.

.. _`vringh_abandon_kern`:

vringh_abandon_kern
===================

.. c:function:: void vringh_abandon_kern(struct vringh *vrh, unsigned int num)

    we've decided not to handle the descriptor(s).

    :param struct vringh \*vrh:
        the vring.

    :param unsigned int num:
        the number of descriptors to put back (ie. num
        \ :c:func:`vringh_get_kern`\  to undo).

.. _`vringh_abandon_kern.description`:

Description
-----------

The next \ :c:func:`vringh_get_kern`\  will return the old descriptor(s) again.

.. _`vringh_complete_kern`:

vringh_complete_kern
====================

.. c:function:: int vringh_complete_kern(struct vringh *vrh, u16 head, u32 len)

    we've finished with descriptor, publish it.

    :param struct vringh \*vrh:
        the vring.

    :param u16 head:
        the head as filled in by vringh_getdesc_kern.

    :param u32 len:
        the length of data we have written.

.. _`vringh_complete_kern.description`:

Description
-----------

You should check \ :c:func:`vringh_need_notify_kern`\  after one or more calls
to this function.

.. _`vringh_notify_enable_kern`:

vringh_notify_enable_kern
=========================

.. c:function:: bool vringh_notify_enable_kern(struct vringh *vrh)

    we want to know if something changes.

    :param struct vringh \*vrh:
        the vring.

.. _`vringh_notify_enable_kern.description`:

Description
-----------

This always enables notifications, but returns false if there are
now more buffers available in the vring.

.. _`vringh_notify_disable_kern`:

vringh_notify_disable_kern
==========================

.. c:function:: void vringh_notify_disable_kern(struct vringh *vrh)

    don't tell us if something changes.

    :param struct vringh \*vrh:
        the vring.

.. _`vringh_notify_disable_kern.this-is-our-normal-running-state`:

This is our normal running state
--------------------------------

we disable and then only enable when
we're going to sleep.

.. _`vringh_need_notify_kern`:

vringh_need_notify_kern
=======================

.. c:function:: int vringh_need_notify_kern(struct vringh *vrh)

    must we tell the other side about used buffers?

    :param struct vringh \*vrh:
        the vring we've called \ :c:func:`vringh_complete_kern`\  on.

.. _`vringh_need_notify_kern.description`:

Description
-----------

Returns -errno or 0 if we don't need to tell the other side, 1 if we do.

.. This file was automatic generated / don't edit.

