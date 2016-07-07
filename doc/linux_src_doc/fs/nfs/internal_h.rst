.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/internal.h

.. _`nfs_fhandle_hash`:

nfs_fhandle_hash
================

.. c:function:: u32 nfs_fhandle_hash(const struct nfs_fh *fh)

    calculate the crc32 hash for the filehandle \ ``fh``\  - pointer to filehandle

    :param const struct nfs_fh \*fh:
        *undescribed*

.. _`nfs_fhandle_hash.description`:

Description
-----------

returns a crc32 hash for the filehandle that is compatible with
the one displayed by "wireshark".

.. This file was automatic generated / don't edit.

