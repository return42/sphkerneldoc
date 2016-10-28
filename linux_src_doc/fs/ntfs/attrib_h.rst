.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/attrib.h

.. _`ntfs_attr_search_ctx`:

typedef ntfs_attr_search_ctx
============================

.. c:type:: typedef ntfs_attr_search_ctx

    used in attribute search functions

.. _`ntfs_attr_search_ctx.description`:

Description
-----------

Structure must be initialized to zero before the first call to one of the
attribute search functions. Initialize \ ``mrec``\  to point to the mft record to
search, and \ ``attr``\  to point to the first attribute within \ ``mrec``\  (not necessary
if calling the \\ :c:func:`_first`\  functions), and set \ ``is_first``\  to 'true' (not necessary
if calling the \\ :c:func:`_first`\  functions).

If \ ``is_first``\  is 'true', the search begins with \ ``attr``\ . If \ ``is_first``\  is 'false',
the search begins after \ ``attr``\ . This is so that, after the first call to one
of the search attribute functions, we can call the function again, without
any modification of the search context, to automagically get the next
matching attribute.

.. This file was automatic generated / don't edit.

