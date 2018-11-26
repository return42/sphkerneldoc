.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfsd/nfsfh.h

.. _`knfsd_fh_hash`:

knfsd_fh_hash
=============

.. c:function:: u32 knfsd_fh_hash(struct knfsd_fh *fh)

    calculate the crc32 hash for the filehandle \ ``fh``\  - pointer to filehandle

    :param fh:
        *undescribed*
    :type fh: struct knfsd_fh \*

.. _`knfsd_fh_hash.description`:

Description
-----------

returns a crc32 hash for the filehandle that is compatible with
the one displayed by "wireshark".

.. This file was automatic generated / don't edit.

