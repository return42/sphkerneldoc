.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/cifs/file.c

.. _`cifs_readdata_to_iov`:

cifs_readdata_to_iov
====================

.. c:function:: int cifs_readdata_to_iov(struct cifs_readdata *rdata, struct iov_iter *iter)

    copy data from pages in response to an iovec

    :param rdata:
        the readdata response with list of pages holding data
    :type rdata: struct cifs_readdata \*

    :param iter:
        destination for our data
    :type iter: struct iov_iter \*

.. _`cifs_readdata_to_iov.description`:

Description
-----------

This function copies data from a list of pages in a readdata response into
an array of iovecs. It will first calculate where the data should go
based on the info in the readdata and then copy the data into that spot.

.. This file was automatic generated / don't edit.

