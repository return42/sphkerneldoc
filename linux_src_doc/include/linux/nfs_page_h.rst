.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/nfs_page.h

.. _`nfs_list_add_request`:

nfs_list_add_request
====================

.. c:function:: void nfs_list_add_request(struct nfs_page *req, struct list_head *head)

    Insert a request into a list

    :param req:
        request
    :type req: struct nfs_page \*

    :param head:
        head of list into which to insert the request.
    :type head: struct list_head \*

.. _`nfs_list_remove_request`:

nfs_list_remove_request
=======================

.. c:function:: void nfs_list_remove_request(struct nfs_page *req)

    Remove a request from its wb_list

    :param req:
        request
    :type req: struct nfs_page \*

.. This file was automatic generated / don't edit.

