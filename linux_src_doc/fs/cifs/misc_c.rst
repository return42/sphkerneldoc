.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/cifs/misc.c

.. _`cifs_alloc_hash`:

cifs_alloc_hash
===============

.. c:function:: int cifs_alloc_hash(const char *name, struct crypto_shash **shash, struct sdesc **sdesc)

    allocate hash and hash context together

    :param name:
        *undescribed*
    :type name: const char \*

    :param shash:
        *undescribed*
    :type shash: struct crypto_shash \*\*

    :param sdesc:
        *undescribed*
    :type sdesc: struct sdesc \*\*

.. _`cifs_alloc_hash.description`:

Description
-----------

The caller has to make sure \ ``sdesc``\  is initialized to either NULL or
a valid context. Both can be freed via \ :c:func:`cifs_free_hash`\ .

.. _`cifs_free_hash`:

cifs_free_hash
==============

.. c:function:: void cifs_free_hash(struct crypto_shash **shash, struct sdesc **sdesc)

    free hash and hash context together

    :param shash:
        *undescribed*
    :type shash: struct crypto_shash \*\*

    :param sdesc:
        *undescribed*
    :type sdesc: struct sdesc \*\*

.. _`cifs_free_hash.description`:

Description
-----------

Freeing a NULL hash or context is safe.

.. _`rqst_page_get_length`:

rqst_page_get_length
====================

.. c:function:: void rqst_page_get_length(struct smb_rqst *rqst, unsigned int page, unsigned int *len, unsigned int *offset)

    obtain the length and offset for a page in smb_rqst

    :param rqst:
        *undescribed*
    :type rqst: struct smb_rqst \*

    :param page:
        *undescribed*
    :type page: unsigned int

    :param len:
        *undescribed*
    :type len: unsigned int \*

    :param offset:
        *undescribed*
    :type offset: unsigned int \*

.. _`rqst_page_get_length.input`:

Input
-----

rqst - a smb_rqst, page - a page index for rqst

.. _`rqst_page_get_length.output`:

Output
------

\*len - the length for this page, \*offset - the offset for this page

.. This file was automatic generated / don't edit.

