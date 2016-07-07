.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/kref.h

.. _`kref_init`:

kref_init
=========

.. c:function:: void kref_init(struct kref *kref)

    initialize object.

    :param struct kref \*kref:
        object in question.

.. _`kref_get`:

kref_get
========

.. c:function:: void kref_get(struct kref *kref)

    increment refcount for object.

    :param struct kref \*kref:
        object.

.. _`kref_sub`:

kref_sub
========

.. c:function:: int kref_sub(struct kref *kref, unsigned int count, void (*) release (struct kref *kref)

    subtract a number of refcounts for object.

    :param struct kref \*kref:
        object.

    :param unsigned int count:
        Number of recounts to subtract.

    :param (void (\*) release (struct kref \*kref):
        pointer to the function that will clean up the object when the
        last reference to the object is released.
        This pointer is required, and it is not acceptable to pass kfree
        in as this function.  If the caller does pass kfree to this
        function, you will be publicly mocked mercilessly by the kref
        maintainer, and anyone else who happens to notice it.  You have
        been warned.

.. _`kref_sub.description`:

Description
-----------

Subtract \ ``count``\  from the refcount, and if 0, call \ :c:func:`release`\ .
Return 1 if the object was removed, otherwise return 0.  Beware, if this
function returns 0, you still can not count on the kref from remaining in
memory.  Only use the return value if you want to see if the kref is now
gone, not present.

.. _`kref_put`:

kref_put
========

.. c:function:: int kref_put(struct kref *kref, void (*) release (struct kref *kref)

    decrement refcount for object.

    :param struct kref \*kref:
        object.

    :param (void (\*) release (struct kref \*kref):
        pointer to the function that will clean up the object when the
        last reference to the object is released.
        This pointer is required, and it is not acceptable to pass kfree
        in as this function.  If the caller does pass kfree to this
        function, you will be publicly mocked mercilessly by the kref
        maintainer, and anyone else who happens to notice it.  You have
        been warned.

.. _`kref_put.description`:

Description
-----------

Decrement the refcount, and if 0, call \ :c:func:`release`\ .
Return 1 if the object was removed, otherwise return 0.  Beware, if this
function returns 0, you still can not count on the kref from remaining in
memory.  Only use the return value if you want to see if the kref is now
gone, not present.

.. _`kref_get_unless_zero`:

kref_get_unless_zero
====================

.. c:function:: int kref_get_unless_zero(struct kref *kref)

    Increment refcount for object unless it is zero.

    :param struct kref \*kref:
        object.

.. _`kref_get_unless_zero.description`:

Description
-----------

Return non-zero if the increment succeeded. Otherwise return 0.

This function is intended to simplify locking around refcounting for
objects that can be looked up from a lookup structure, and which are
removed from that lookup structure in the object destructor.
Operations on such objects require at least a read lock around
lookup + kref_get, and a write lock around kref_put + remove from lookup
structure. Furthermore, RCU implementations become extremely tricky.
With a lookup followed by a kref_get_unless_zero \*with return value check\*
locking in the kref_put path can be deferred to the actual removal from
the lookup structure and RCU lookups become trivial.

.. This file was automatic generated / don't edit.

