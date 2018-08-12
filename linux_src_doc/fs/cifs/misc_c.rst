.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/cifs/misc.c

.. _`cifs_alloc_hash`:

cifs_alloc_hash
===============

.. c:function:: int cifs_alloc_hash(const char *name, struct crypto_shash **shash, struct sdesc **sdesc)

    allocate hash and hash context together

    :param const char \*name:
        *undescribed*

    :param struct crypto_shash \*\*shash:
        *undescribed*

    :param struct sdesc \*\*sdesc:
        *undescribed*

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

    :param struct crypto_shash \*\*shash:
        *undescribed*

    :param struct sdesc \*\*sdesc:
        *undescribed*

.. _`cifs_free_hash.description`:

Description
-----------

Freeing a NULL hash or context is safe.

.. _`rqst_page_get_length`:

rqst_page_get_length
====================

.. c:function:: void rqst_page_get_length(struct smb_rqst *rqst, unsigned int page, unsigned int *len, unsigned int *offset)

    obtain the length and offset for a page in smb_rqst

    :param struct smb_rqst \*rqst:
        *undescribed*

    :param unsigned int page:
        *undescribed*

    :param unsigned int \*len:
        *undescribed*

    :param unsigned int \*offset:
        *undescribed*

.. _`rqst_page_get_length.input`:

Input
-----

rqst - a smb_rqst, page - a page index for rqst

.. _`rqst_page_get_length.output`:

Output
------

\*len - the length for this page, \*offset - the offset for this page

.. This file was automatic generated / don't edit.

