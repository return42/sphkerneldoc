.. -*- coding: utf-8; mode: rst -*-
.. src-file: xxx.h

.. _`xenbus_watch_pathfmt`:

xenbus_watch_pathfmt
====================

.. c:function:: int xenbus_watch_pathfmt(const char *pathfmt,  ...)

    register a watch on a sprintf-formatted path

    :param const char \*pathfmt:
        format of path to watch

    :param ellipsis ellipsis:
        foobar döadjakjsdlkjdl

.. _`xenbus_watch_pathfmt.description`:

Description
-----------

Register a watch on the given \ ``path``\ , using the given xenbus_watch
structure for storage, and the given \ ``callback``\  function as the callback.
Return 0 on success, or -errno on error.  On success, the watched path
(@path/@path2) will be saved as \ ``watch``\ ->node, and becomes the caller's to
\ :c:func:`kfree`\ .  On error, watch->node will be NULL, so the caller has nothing to
free, the device will switch to \ ``XenbusStateClosing``\ , and the error will be
saved in the store.

.. _`user_function`:

user_function
=============

.. c:function:: int user_function(int a,  ...)

    function that can only be called in user context

    :param int a:
        some argument

    :param ellipsis ellipsis:
        ellipsis operator

.. _`user_function.description`:

Description
-----------

This function makes no sense, it's only a kernel-doc demonstration.

.. _`user_function.example`:

Example
-------

.. code-block:: c

    x = user_function(22);


.. _`user_function.return`:

Return
------

Returns first argument

.. _`nested_foobar`:

struct nested_foobar
====================

.. c:type:: struct nested_foobar

    a struct with nested unions and structs

.. _`nested_foobar.definition`:

Definition
----------

.. code-block:: c

    struct nested_foobar {
        union {
            struct {
                int arg1;
                int arg2;
            } struct {
                void *arg3;
                int arg4;
            } } union {
                struct {
                    int arg1;
                    int arg2;
                } st1;
                struct {
                    void *arg1;
                    int arg2;
                } st2;
            } bar;
    }

.. _`nested_foobar.members`:

Members
-------

bar
    *undescribed*

.. This file was automatic generated / don't edit.

