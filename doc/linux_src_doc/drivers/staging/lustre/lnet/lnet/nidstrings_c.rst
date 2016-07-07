.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lnet/lnet/nidstrings.c

.. _`parse_addrange`:

parse_addrange
==============

.. c:function:: int parse_addrange(const struct cfs_lstr *src, struct nidrange *nidrange)

    :param const struct cfs_lstr \*src:
        *undescribed*

    :param struct nidrange \*nidrange:
        *undescribed*

.. _`parse_addrange.description`:

Description
-----------

Allocates struct addrrange and links to \a nidrange via
(nidrange::nr_addrranges)

\retval 0 if \a src parses to '\*' \| \<ipaddr_range\> \| \<cfs_expr_list\>
\retval -errno otherwise

.. _`add_nidrange`:

add_nidrange
============

.. c:function:: struct nidrange *add_nidrange(const struct cfs_lstr *src, struct list_head *nidlist)

    :param const struct cfs_lstr \*src:
        *undescribed*

    :param struct list_head \*nidlist:
        *undescribed*

.. _`add_nidrange.description`:

Description
-----------

Checks if \a src is a valid network name, looks for corresponding
nidrange on the ist of nidranges (\a nidlist), creates new struct
nidrange if it is not found.

\retval pointer to struct nidrange matching network specified via \a src
\retval NULL if \a src does not match any network

.. _`parse_nidrange`:

parse_nidrange
==============

.. c:function:: int parse_nidrange(struct cfs_lstr *src, struct list_head *nidlist)

    :param struct cfs_lstr \*src:
        *undescribed*

    :param struct list_head \*nidlist:
        *undescribed*

.. _`parse_nidrange.description`:

Description
-----------

\retval 1 if \a src parses to \<addrrange\> '@' \<net\>
\retval 0 otherwise

.. _`free_addrranges`:

free_addrranges
===============

.. c:function:: void free_addrranges(struct list_head *list)

    :param struct list_head \*list:
        *undescribed*

.. _`free_addrranges.description`:

Description
-----------

For each struct addrrange structure found on \a list it frees
cfs_expr_list list attached to it and frees the addrrange itself.

\retval none

.. _`cfs_free_nidlist`:

cfs_free_nidlist
================

.. c:function:: void cfs_free_nidlist(struct list_head *list)

    :param struct list_head \*list:
        *undescribed*

.. _`cfs_free_nidlist.description`:

Description
-----------

For each struct nidrange structure found on \a list it frees
addrrange list attached to it and frees the nidrange itself.

\retval none

.. _`cfs_parse_nidlist`:

cfs_parse_nidlist
=================

.. c:function:: int cfs_parse_nidlist(char *str, int len, struct list_head *nidlist)

    :param char \*str:
        *undescribed*

    :param int len:
        *undescribed*

    :param struct list_head \*nidlist:
        *undescribed*

.. _`cfs_parse_nidlist.description`:

Description
-----------

Parses with rigorous syntax and overflow checking \a str into
\<nidrange\> [ ' ' \<nidrange\> ], compiles \a str into set of
structures and links that structure to \a nidlist. The resulting
list can be used to match a NID againts set of NIDS defined by \a
str.
\see cfs_match_nid

\retval 1 on success
\retval 0 otherwise

.. _`cfs_match_nid`:

cfs_match_nid
=============

.. c:function:: int cfs_match_nid(lnet_nid_t nid, struct list_head *nidlist)

    :param lnet_nid_t nid:
        *undescribed*

    :param struct list_head \*nidlist:
        *undescribed*

.. _`cfs_match_nid.description`:

Description
-----------

\see \ :c:func:`cfs_parse_nidlist`\ 

\retval 1 on match
\retval 0  otherwises

.. _`cfs_print_network`:

cfs_print_network
=================

.. c:function:: int cfs_print_network(char *buffer, int count, struct nidrange *nr)

    :param char \*buffer:
        *undescribed*

    :param int count:
        *undescribed*

    :param struct nidrange \*nr:
        *undescribed*

.. _`cfs_print_network.description`:

Description
-----------

\retval number of characters written

.. _`cfs_print_addrranges`:

cfs_print_addrranges
====================

.. c:function:: int cfs_print_addrranges(char *buffer, int count, struct list_head *addrranges, struct nidrange *nr)

    At max \a count characters can be printed into \a buffer.

    :param char \*buffer:
        *undescribed*

    :param int count:
        *undescribed*

    :param struct list_head \*addrranges:
        *undescribed*

    :param struct nidrange \*nr:
        *undescribed*

.. _`cfs_print_addrranges.description`:

Description
-----------

\retval number of characters written

.. _`cfs_print_nidlist`:

cfs_print_nidlist
=================

.. c:function:: int cfs_print_nidlist(char *buffer, int count, struct list_head *nidlist)

    At max \a count characters can be printed into \a buffer. Nidranges are separated by a space character.

    :param char \*buffer:
        *undescribed*

    :param int count:
        *undescribed*

    :param struct list_head \*nidlist:
        *undescribed*

.. _`cfs_print_nidlist.description`:

Description
-----------

\retval number of characters written

.. _`cfs_ip_ar_min_max`:

cfs_ip_ar_min_max
=================

.. c:function:: void cfs_ip_ar_min_max(struct addrrange *ar, __u32 *min_nid, __u32 *max_nid)

    numeric address range

    :param struct addrrange \*ar:
        *undescribed*

    :param __u32 \*min_nid:
        *undescribed*

    :param __u32 \*max_nid:
        *undescribed*

.. _`cfs_ip_ar_min_max.description`:

Description
-----------

\param       ar
\param       min_nid
\param       max_nid

.. _`cfs_num_ar_min_max`:

cfs_num_ar_min_max
==================

.. c:function:: void cfs_num_ar_min_max(struct addrrange *ar, __u32 *min_nid, __u32 *max_nid)

    numeric address range

    :param struct addrrange \*ar:
        *undescribed*

    :param __u32 \*min_nid:
        *undescribed*

    :param __u32 \*max_nid:
        *undescribed*

.. _`cfs_num_ar_min_max.description`:

Description
-----------

\param       ar
\param       min_nid
\param       max_nid

.. _`cfs_nidrange_is_contiguous`:

cfs_nidrange_is_contiguous
==========================

.. c:function:: bool cfs_nidrange_is_contiguous(struct list_head *nidlist)

    one contiguous address range. Calls the correct netstrfns for the LND

    :param struct list_head \*nidlist:
        *undescribed*

.. _`cfs_nidrange_is_contiguous.description`:

Description
-----------

\param       \*nidlist

\retval      true if contiguous
\retval      false if not contiguous

.. _`cfs_num_is_contiguous`:

cfs_num_is_contiguous
=====================

.. c:function:: bool cfs_num_is_contiguous(struct list_head *nidlist)

    one contiguous address range.

    :param struct list_head \*nidlist:
        *undescribed*

.. _`cfs_num_is_contiguous.description`:

Description
-----------

\param       \*nidlist

\retval      true if contiguous
\retval      false if not contiguous

.. _`cfs_ip_is_contiguous`:

cfs_ip_is_contiguous
====================

.. c:function:: bool cfs_ip_is_contiguous(struct list_head *nidlist)

    one contiguous address range.

    :param struct list_head \*nidlist:
        *undescribed*

.. _`cfs_ip_is_contiguous.description`:

Description
-----------

\param       \*nidlist

\retval      true if contiguous
\retval      false if not contiguous

.. _`cfs_nidrange_find_min_max`:

cfs_nidrange_find_min_max
=========================

.. c:function:: void cfs_nidrange_find_min_max(struct list_head *nidlist, char *min_nid, char *max_nid, size_t nidstr_length)

    and maximum nid and creates appropriate nid structures

    :param struct list_head \*nidlist:
        *undescribed*

    :param char \*min_nid:
        *undescribed*

    :param char \*max_nid:
        *undescribed*

    :param size_t nidstr_length:
        *undescribed*

.. _`cfs_nidrange_find_min_max.description`:

Description
-----------

\param       \*nidlist
\param       \*min_nid
\param       \*max_nid

.. _`cfs_num_min_max`:

cfs_num_min_max
===============

.. c:function:: void cfs_num_min_max(struct list_head *nidlist, __u32 *min_nid, __u32 *max_nid)

    :param struct list_head \*nidlist:
        *undescribed*

    :param __u32 \*min_nid:
        *undescribed*

    :param __u32 \*max_nid:
        *undescribed*

.. _`cfs_num_min_max.description`:

Description
-----------

\param       \*nidlist
\param       \*min_nid
\param       \*max_nid

.. _`cfs_ip_min_max`:

cfs_ip_min_max
==============

.. c:function:: void cfs_ip_min_max(struct list_head *nidlist, __u32 *min_nid, __u32 *max_nid)

    ip addresses.

    :param struct list_head \*nidlist:
        *undescribed*

    :param __u32 \*min_nid:
        *undescribed*

    :param __u32 \*max_nid:
        *undescribed*

.. _`cfs_ip_min_max.description`:

Description
-----------

\param       \*nidlist
\param       \*min_nid
\param       \*max_nid

.. _`cfs_ip_addr_match`:

cfs_ip_addr_match
=================

.. c:function:: int cfs_ip_addr_match(__u32 addr, struct list_head *list)

    :param __u32 addr:
        *undescribed*

    :param struct list_head \*list:
        *undescribed*

.. _`cfs_ip_addr_match.description`:

Description
-----------

\retval 1 if \a addr matches
\retval 0 otherwise

.. _`libcfs_num_parse`:

libcfs_num_parse
================

.. c:function:: int libcfs_num_parse(char *str, int len, struct list_head *list)

    :param char \*str:
        *undescribed*

    :param int len:
        *undescribed*

    :param struct list_head \*list:
        *undescribed*

.. _`libcfs_num_parse.description`:

Description
-----------

Examples of such networks are gm and elan.

\retval 0 if \a str parsed to numeric address
\retval errno otherwise

.. This file was automatic generated / don't edit.

