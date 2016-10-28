.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/mst.c

.. _`post_read_mst_fixup`:

post_read_mst_fixup
===================

.. c:function:: int post_read_mst_fixup(NTFS_RECORD *b, const u32 size)

    deprotect multi sector transfer protected data

    :param NTFS_RECORD \*b:
        pointer to the data to deprotect

    :param const u32 size:
        size in bytes of \ ``b``\ 

.. _`post_read_mst_fixup.description`:

Description
-----------

Perform the necessary post read multi sector transfer fixup and detect the
presence of incomplete multi sector transfers. - In that case, overwrite the
magic of the ntfs record header being processed with "BAAD" (in memory only!)
and abort processing.

Return 0 on success and -EINVAL on error ("BAAD" magic will be present).

.. _`post_read_mst_fixup.note`:

NOTE
----

We consider the absence / invalidity of an update sequence array to
mean that the structure is not protected at all and hence doesn't need to
be fixed up. Thus, we return success and not failure in this case. This is
in contrast to \ :c:func:`pre_write_mst_fixup`\ , see below.

.. _`pre_write_mst_fixup`:

pre_write_mst_fixup
===================

.. c:function:: int pre_write_mst_fixup(NTFS_RECORD *b, const u32 size)

    apply multi sector transfer protection

    :param NTFS_RECORD \*b:
        pointer to the data to protect

    :param const u32 size:
        size in bytes of \ ``b``\ 

.. _`pre_write_mst_fixup.description`:

Description
-----------

Perform the necessary pre write multi sector transfer fixup on the data
pointer to by \ ``b``\  of \ ``size``\ .

Return 0 if fixup applied (success) or -EINVAL if no fixup was performed
(assumed not needed). This is in contrast to \ :c:func:`post_read_mst_fixup`\  above.

.. _`pre_write_mst_fixup.note`:

NOTE
----

We consider the absence / invalidity of an update sequence array to
mean that the structure is not subject to protection and hence doesn't need
to be fixed up. This means that you have to create a valid update sequence
array header in the ntfs record before calling this function, otherwise it
will fail (the header needs to contain the position of the update sequence
array together with the number of elements in the array). You also need to
initialise the update sequence number before calling this function
otherwise a random word will be used (whatever was in the record at that
position at that time).

.. _`post_write_mst_fixup`:

post_write_mst_fixup
====================

.. c:function:: void post_write_mst_fixup(NTFS_RECORD *b)

    fast deprotect multi sector transfer protected data

    :param NTFS_RECORD \*b:
        pointer to the data to deprotect

.. _`post_write_mst_fixup.description`:

Description
-----------

Perform the necessary post write multi sector transfer fixup, not checking
for any errors, because we assume we have just used \ :c:func:`pre_write_mst_fixup`\ ,
thus the data will be fine or we would never have gotten here.

.. This file was automatic generated / don't edit.

