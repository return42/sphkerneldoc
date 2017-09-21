.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/uapi/linux/lustre/lustre_fid.h

.. _`fid_seq_is_igif`:

fid_seq_is_igif
===============

.. c:function:: bool fid_seq_is_igif(__u64 seq)

    \param fid the fid to be tested. \return true if the fid is an igif; otherwise false.

    :param __u64 seq:
        *undescribed*

.. _`fid_seq_is_idif`:

fid_seq_is_idif
===============

.. c:function:: bool fid_seq_is_idif(__u64 seq)

    \param fid the fid to be tested. \return true if the fid is an idif; otherwise false.

    :param __u64 seq:
        *undescribed*

.. _`lu_igif_ino`:

lu_igif_ino
===========

.. c:function:: ino_t lu_igif_ino(const struct lu_fid *fid)

    \param fid an igif to get inode number from. \return inode number for the igif.

    :param const struct lu_fid \*fid:
        *undescribed*

.. _`lu_igif_gen`:

lu_igif_gen
===========

.. c:function:: __u32 lu_igif_gen(const struct lu_fid *fid)

    \param fid an igif to get inode generation from. \return inode generation for the igif.

    :param const struct lu_fid \*fid:
        *undescribed*

.. _`lu_igif_build`:

lu_igif_build
=============

.. c:function:: void lu_igif_build(struct lu_fid *fid, __u32 ino, __u32 gen)

    :param struct lu_fid \*fid:
        *undescribed*

    :param __u32 ino:
        *undescribed*

    :param __u32 gen:
        *undescribed*

.. This file was automatic generated / don't edit.

