.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/cache.c

.. _`v9fs_random_cachetag`:

v9fs_random_cachetag
====================

.. c:function:: int v9fs_random_cachetag(struct v9fs_session_info *v9ses)

    Generate a random tag to be associated with a new cache session.

    :param struct v9fs_session_info \*v9ses:
        *undescribed*

.. _`v9fs_random_cachetag.description`:

Description
-----------

The value of jiffies is used for a fairly randomly cache tag.

.. _`__v9fs_readpage_from_fscache`:

\__v9fs_readpage_from_fscache
=============================

.. c:function:: int __v9fs_readpage_from_fscache(struct inode *inode, struct page *page)

    read a page from cache

    :param struct inode \*inode:
        *undescribed*

    :param struct page \*page:
        *undescribed*

.. _`__v9fs_readpage_from_fscache.description`:

Description
-----------

Returns 0 if the pages are in cache and a BIO is submitted,
1 if the pages are not in cache and -error otherwise.

.. _`__v9fs_readpages_from_fscache`:

\__v9fs_readpages_from_fscache
==============================

.. c:function:: int __v9fs_readpages_from_fscache(struct inode *inode, struct address_space *mapping, struct list_head *pages, unsigned *nr_pages)

    read multiple pages from cache

    :param struct inode \*inode:
        *undescribed*

    :param struct address_space \*mapping:
        *undescribed*

    :param struct list_head \*pages:
        *undescribed*

    :param unsigned \*nr_pages:
        *undescribed*

.. _`__v9fs_readpages_from_fscache.description`:

Description
-----------

Returns 0 if the pages are in cache and a BIO is submitted,
1 if the pages are not in cache and -error otherwise.

.. _`__v9fs_readpage_to_fscache`:

\__v9fs_readpage_to_fscache
===========================

.. c:function:: void __v9fs_readpage_to_fscache(struct inode *inode, struct page *page)

    write a page to the cache

    :param struct inode \*inode:
        *undescribed*

    :param struct page \*page:
        *undescribed*

.. This file was automatic generated / don't edit.

