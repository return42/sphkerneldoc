.. -*- coding: utf-8; mode: rst -*-

==========
nfs_page.h
==========


.. _`nfs_list_add_request`:

nfs_list_add_request
====================

.. c:function:: void nfs_list_add_request (struct nfs_page *req, struct list_head *head)

    Insert a request into a list

    :param struct nfs_page \*req:
        request

    :param struct list_head \*head:
        head of list into which to insert the request.



.. _`nfs_list_remove_request`:

nfs_list_remove_request
=======================

.. c:function:: void nfs_list_remove_request (struct nfs_page *req)

    Remove a request from its wb_list

    :param struct nfs_page \*req:
        request

