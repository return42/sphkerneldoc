.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/percpu-refcount.h

.. _`percpu_ref_kill`:

percpu_ref_kill
===============

.. c:function:: void percpu_ref_kill(struct percpu_ref *ref)

    drop the initial ref

    :param ref:
        percpu_ref to kill
    :type ref: struct percpu_ref \*

.. _`percpu_ref_kill.description`:

Description
-----------

Must be used to drop the initial ref on a percpu refcount; must be called
precisely once before shutdown.

Switches \ ``ref``\  into atomic mode before gathering up the percpu counters
and dropping the initial ref.

There are no implied RCU grace periods between kill and release.

.. _`percpu_ref_get_many`:

percpu_ref_get_many
===================

.. c:function:: void percpu_ref_get_many(struct percpu_ref *ref, unsigned long nr)

    increment a percpu refcount

    :param ref:
        percpu_ref to get
    :type ref: struct percpu_ref \*

    :param nr:
        number of references to get
    :type nr: unsigned long

.. _`percpu_ref_get_many.description`:

Description
-----------

Analogous to \ :c:func:`atomic_long_add`\ .

This function is safe to call as long as \ ``ref``\  is between init and exit.

.. _`percpu_ref_get`:

percpu_ref_get
==============

.. c:function:: void percpu_ref_get(struct percpu_ref *ref)

    increment a percpu refcount

    :param ref:
        percpu_ref to get
    :type ref: struct percpu_ref \*

.. _`percpu_ref_get.description`:

Description
-----------

Analagous to \ :c:func:`atomic_long_inc`\ .

This function is safe to call as long as \ ``ref``\  is between init and exit.

.. _`percpu_ref_tryget`:

percpu_ref_tryget
=================

.. c:function:: bool percpu_ref_tryget(struct percpu_ref *ref)

    try to increment a percpu refcount

    :param ref:
        percpu_ref to try-get
    :type ref: struct percpu_ref \*

.. _`percpu_ref_tryget.description`:

Description
-----------

Increment a percpu refcount unless its count already reached zero.
Returns \ ``true``\  on success; \ ``false``\  on failure.

This function is safe to call as long as \ ``ref``\  is between init and exit.

.. _`percpu_ref_tryget_live`:

percpu_ref_tryget_live
======================

.. c:function:: bool percpu_ref_tryget_live(struct percpu_ref *ref)

    try to increment a live percpu refcount

    :param ref:
        percpu_ref to try-get
    :type ref: struct percpu_ref \*

.. _`percpu_ref_tryget_live.description`:

Description
-----------

Increment a percpu refcount unless it has already been killed.  Returns
\ ``true``\  on success; \ ``false``\  on failure.

Completion of \ :c:func:`percpu_ref_kill`\  in itself doesn't guarantee that this
function will fail.  For such guarantee, \ :c:func:`percpu_ref_kill_and_confirm`\ 
should be used.  After the confirm_kill callback is invoked, it's
guaranteed that no new reference will be given out by
\ :c:func:`percpu_ref_tryget_live`\ .

This function is safe to call as long as \ ``ref``\  is between init and exit.

.. _`percpu_ref_put_many`:

percpu_ref_put_many
===================

.. c:function:: void percpu_ref_put_many(struct percpu_ref *ref, unsigned long nr)

    decrement a percpu refcount

    :param ref:
        percpu_ref to put
    :type ref: struct percpu_ref \*

    :param nr:
        number of references to put
    :type nr: unsigned long

.. _`percpu_ref_put_many.description`:

Description
-----------

Decrement the refcount, and if 0, call the release function (which was passed
to \ :c:func:`percpu_ref_init`\ )

This function is safe to call as long as \ ``ref``\  is between init and exit.

.. _`percpu_ref_put`:

percpu_ref_put
==============

.. c:function:: void percpu_ref_put(struct percpu_ref *ref)

    decrement a percpu refcount

    :param ref:
        percpu_ref to put
    :type ref: struct percpu_ref \*

.. _`percpu_ref_put.description`:

Description
-----------

Decrement the refcount, and if 0, call the release function (which was passed
to \ :c:func:`percpu_ref_init`\ )

This function is safe to call as long as \ ``ref``\  is between init and exit.

.. _`percpu_ref_is_dying`:

percpu_ref_is_dying
===================

.. c:function:: bool percpu_ref_is_dying(struct percpu_ref *ref)

    test whether a percpu refcount is dying or dead

    :param ref:
        percpu_ref to test
    :type ref: struct percpu_ref \*

.. _`percpu_ref_is_dying.description`:

Description
-----------

Returns \ ``true``\  if \ ``ref``\  is dying or dead.

This function is safe to call as long as \ ``ref``\  is between init and exit
and the caller is responsible for synchronizing against state changes.

.. _`percpu_ref_is_zero`:

percpu_ref_is_zero
==================

.. c:function:: bool percpu_ref_is_zero(struct percpu_ref *ref)

    test whether a percpu refcount reached zero

    :param ref:
        percpu_ref to test
    :type ref: struct percpu_ref \*

.. _`percpu_ref_is_zero.description`:

Description
-----------

Returns \ ``true``\  if \ ``ref``\  reached zero.

This function is safe to call as long as \ ``ref``\  is between init and exit.

.. This file was automatic generated / don't edit.

