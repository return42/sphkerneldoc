.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/obdclass/linkea.c

.. _`linkea_entry_pack`:

linkea_entry_pack
=================

.. c:function:: int linkea_entry_pack(struct link_ea_entry *lee, const struct lu_name *lname, const struct lu_fid *pfid)

    All elements are stored as chars to avoid alignment issues. Numbers are always big-endian \retval record length

    :param struct link_ea_entry \*lee:
        *undescribed*

    :param const struct lu_name \*lname:
        *undescribed*

    :param const struct lu_fid \*pfid:
        *undescribed*

.. _`linkea_add_buf`:

linkea_add_buf
==============

.. c:function:: int linkea_add_buf(struct linkea_data *ldata, const struct lu_name *lname, const struct lu_fid *pfid)

    :param struct linkea_data \*ldata:
        *undescribed*

    :param const struct lu_name \*lname:
        *undescribed*

    :param const struct lu_fid \*pfid:
        *undescribed*

.. _`linkea_links_find`:

linkea_links_find
=================

.. c:function:: int linkea_links_find(struct linkea_data *ldata, const struct lu_name *lname, const struct lu_fid *pfid)

    :param struct linkea_data \*ldata:
        *undescribed*

    :param const struct lu_name \*lname:
        *undescribed*

    :param const struct lu_fid \*pfid:
        *undescribed*

.. _`linkea_links_find.description`:

Description
-----------

\param ldata link data the search to be done on
\param lname name in the parent's directory entry pointing to this object
\param pfid parent fid the link to be found for

\retval   0 success
\retval -ENOENT link does not exist
\retval -ve on error

.. This file was automatic generated / don't edit.

