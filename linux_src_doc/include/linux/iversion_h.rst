.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iversion.h

.. _`inode_set_iversion_raw`:

inode_set_iversion_raw
======================

.. c:function:: void inode_set_iversion_raw(struct inode *inode, u64 val)

    set i_version to the specified raw value

    :param inode:
        inode to set
    :type inode: struct inode \*

    :param val:
        new i_version value to set
    :type val: u64

.. _`inode_set_iversion_raw.description`:

Description
-----------

Set \ ``inode``\ 's i_version field to \ ``val``\ . This function is for use by
filesystems that self-manage the i_version.

For example, the NFS client stores its NFSv4 change attribute in this way,
and the AFS client stores the data_version from the server here.

.. _`inode_peek_iversion_raw`:

inode_peek_iversion_raw
=======================

.. c:function:: u64 inode_peek_iversion_raw(const struct inode *inode)

    grab a "raw" iversion value

    :param inode:
        inode from which i_version should be read
    :type inode: const struct inode \*

.. _`inode_peek_iversion_raw.description`:

Description
-----------

Grab a "raw" inode->i_version value and return it. The i_version is not
flagged or converted in any way. This is mostly used to access a self-managed
i_version.

With those filesystems, we want to treat the i_version as an entirely
opaque value.

.. _`inode_set_iversion`:

inode_set_iversion
==================

.. c:function:: void inode_set_iversion(struct inode *inode, u64 val)

    set i_version to a particular value

    :param inode:
        inode to set
    :type inode: struct inode \*

    :param val:
        new i_version value to set
    :type val: u64

.. _`inode_set_iversion.description`:

Description
-----------

Set \ ``inode``\ 's i_version field to \ ``val``\ . This function is for filesystems with
a kernel-managed i_version, for initializing a newly-created inode from
scratch.

In this case, we do not set the QUERIED flag since we know that this value
has never been queried.

.. _`inode_set_iversion_queried`:

inode_set_iversion_queried
==========================

.. c:function:: void inode_set_iversion_queried(struct inode *inode, u64 val)

    set i_version to a particular value as quereied

    :param inode:
        inode to set
    :type inode: struct inode \*

    :param val:
        new i_version value to set
    :type val: u64

.. _`inode_set_iversion_queried.description`:

Description
-----------

Set \ ``inode``\ 's i_version field to \ ``val``\ , and flag it for increment on the next
change.

Filesystems that persistently store the i_version on disk should use this
when loading an existing inode from disk.

When loading in an i_version value from a backing store, we can't be certain
that it wasn't previously viewed before being stored. Thus, we must assume
that it was, to ensure that we don't end up handing out the same value for
different versions of the same inode.

.. _`inode_maybe_inc_iversion`:

inode_maybe_inc_iversion
========================

.. c:function:: bool inode_maybe_inc_iversion(struct inode *inode, bool force)

    increments i_version

    :param inode:
        inode with the i_version that should be updated
    :type inode: struct inode \*

    :param force:
        increment the counter even if it's not necessary?
    :type force: bool

.. _`inode_maybe_inc_iversion.description`:

Description
-----------

Every time the inode is modified, the i_version field must be seen to have
changed by any observer.

If "force" is set or the QUERIED flag is set, then ensure that we increment
the value, and clear the queried flag.

In the common case where neither is set, then we can return "false" without
updating i_version.

If this function returns false, and no other metadata has changed, then we
can avoid logging the metadata.

.. _`inode_inc_iversion`:

inode_inc_iversion
==================

.. c:function:: void inode_inc_iversion(struct inode *inode)

    forcibly increment i_version

    :param inode:
        inode that needs to be updated
    :type inode: struct inode \*

.. _`inode_inc_iversion.description`:

Description
-----------

Forcbily increment the i_version field. This always results in a change to
the observable value.

.. _`inode_iversion_need_inc`:

inode_iversion_need_inc
=======================

.. c:function:: bool inode_iversion_need_inc(struct inode *inode)

    is the i_version in need of being incremented?

    :param inode:
        inode to check
    :type inode: struct inode \*

.. _`inode_iversion_need_inc.description`:

Description
-----------

Returns whether the inode->i_version counter needs incrementing on the next
change. Just fetch the value and check the QUERIED flag.

.. _`inode_inc_iversion_raw`:

inode_inc_iversion_raw
======================

.. c:function:: void inode_inc_iversion_raw(struct inode *inode)

    forcibly increment raw i_version

    :param inode:
        inode that needs to be updated
    :type inode: struct inode \*

.. _`inode_inc_iversion_raw.description`:

Description
-----------

Forcbily increment the raw i_version field. This always results in a change
to the raw value.

NFS will use the i_version field to store the value from the server. It
mostly treats it as opaque, but in the case where it holds a write
delegation, it must increment the value itself. This function does that.

.. _`inode_peek_iversion`:

inode_peek_iversion
===================

.. c:function:: u64 inode_peek_iversion(const struct inode *inode)

    read i_version without flagging it to be incremented

    :param inode:
        inode from which i_version should be read
    :type inode: const struct inode \*

.. _`inode_peek_iversion.description`:

Description
-----------

Read the inode i_version counter for an inode without registering it as a
query.

This is typically used by local filesystems that need to store an i_version
on disk. In that situation, it's not necessary to flag it as having been
viewed, as the result won't be used to gauge changes from that point.

.. _`inode_query_iversion`:

inode_query_iversion
====================

.. c:function:: u64 inode_query_iversion(struct inode *inode)

    read i_version for later use

    :param inode:
        inode from which i_version should be read
    :type inode: struct inode \*

.. _`inode_query_iversion.description`:

Description
-----------

Read the inode i_version counter. This should be used by callers that wish
to store the returned i_version for later comparison. This will guarantee
that a later query of the i_version will result in a different value if
anything has changed.

In this implementation, we fetch the current value, set the QUERIED flag and
then try to swap it into place with a cmpxchg, if it wasn't already set. If
that fails, we try again with the newly fetched value from the cmpxchg.

.. _`inode_eq_iversion_raw`:

inode_eq_iversion_raw
=====================

.. c:function:: bool inode_eq_iversion_raw(const struct inode *inode, u64 old)

    check whether the raw i_version counter has changed

    :param inode:
        inode to check
    :type inode: const struct inode \*

    :param old:
        old value to check against its i_version
    :type old: u64

.. _`inode_eq_iversion_raw.description`:

Description
-----------

Compare the current raw i_version counter with a previous one. Returns true
if they are the same or false if they are different.

.. _`inode_eq_iversion`:

inode_eq_iversion
=================

.. c:function:: bool inode_eq_iversion(const struct inode *inode, u64 old)

    check whether the i_version counter has changed

    :param inode:
        inode to check
    :type inode: const struct inode \*

    :param old:
        old value to check against its i_version
    :type old: u64

.. _`inode_eq_iversion.description`:

Description
-----------

Compare an i_version counter with a previous one. Returns true if they are
the same, and false if they are different.

Note that we don't need to set the QUERIED flag in this case, as the value
in the inode is not being recorded for later use.

.. This file was automatic generated / don't edit.

