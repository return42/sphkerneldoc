
.. _API-idr-for-each:

============
idr_for_each
============

*man idr_for_each(9)*

*4.6.0-rc1*

iterate through all stored pointers


Synopsis
========

.. c:function:: int idr_for_each( struct idr * idp, int (*fn) int id, void *p, void *data, void * data )

Arguments
=========

``idp``
    idr handle

``fn``
    function to be called for each pointer

``data``
    data passed back to callback function


Description
===========

Iterate over the pointers registered with the given idr. The callback function will be called for each pointer currently registered, passing the id, the pointer and the data
pointer passed to this function. It is not safe to modify the idr tree while in the callback, so functions such as idr_get_new and idr_remove are not allowed.

We check the return of ``fn`` each time. If it returns anything other than ``0``, we break out and return that value.

The caller must serialize ``idr_for_each`` vs ``idr_get_new`` and ``idr_remove``.
