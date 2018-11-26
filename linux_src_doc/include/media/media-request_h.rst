.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/media-request.h

.. _`media_request_state`:

enum media_request_state
========================

.. c:type:: enum media_request_state

    media request state

.. _`media_request_state.definition`:

Definition
----------

.. code-block:: c

    enum media_request_state {
        MEDIA_REQUEST_STATE_IDLE,
        MEDIA_REQUEST_STATE_VALIDATING,
        MEDIA_REQUEST_STATE_QUEUED,
        MEDIA_REQUEST_STATE_COMPLETE,
        MEDIA_REQUEST_STATE_CLEANING,
        MEDIA_REQUEST_STATE_UPDATING,
        NR_OF_MEDIA_REQUEST_STATE
    };

.. _`media_request_state.constants`:

Constants
---------

MEDIA_REQUEST_STATE_IDLE
    Idle

MEDIA_REQUEST_STATE_VALIDATING
    Validating the request, no state changes
    allowed

MEDIA_REQUEST_STATE_QUEUED
    Queued

MEDIA_REQUEST_STATE_COMPLETE
    Completed, the request is done

MEDIA_REQUEST_STATE_CLEANING
    Cleaning, the request is being re-inited

MEDIA_REQUEST_STATE_UPDATING
    The request is being updated, i.e.
    request objects are being added,
    modified or removed

NR_OF_MEDIA_REQUEST_STATE
    The number of media request states, used
    internally for sanity check purposes

.. _`media_request`:

struct media_request
====================

.. c:type:: struct media_request

    Media device request

.. _`media_request.definition`:

Definition
----------

.. code-block:: c

    struct media_request {
        struct media_device *mdev;
        struct kref kref;
        char debug_str[TASK_COMM_LEN + 11];
        enum media_request_state state;
        unsigned int updating_count;
        unsigned int access_count;
        struct list_head objects;
        unsigned int num_incomplete_objects;
        struct wait_queue_head poll_wait;
        spinlock_t lock;
    }

.. _`media_request.members`:

Members
-------

mdev
    Media device this request belongs to

kref
    Reference count

debug_str
    Prefix for debug messages (process name:fd)

state
    The state of the request

updating_count
    count the number of request updates that are in progress

access_count
    count the number of request accesses that are in progress

objects
    List of \ ``struct``\  media_request_object request objects

num_incomplete_objects
    The number of incomplete objects in the request

poll_wait
    Wait queue for poll

lock
    Serializes access to this struct

.. _`media_request_lock_for_access`:

media_request_lock_for_access
=============================

.. c:function:: int media_request_lock_for_access(struct media_request *req)

    Lock the request to access its objects

    :param req:
        The media request
    :type req: struct media_request \*

.. _`media_request_lock_for_access.description`:

Description
-----------

Use before accessing a completed request. A reference to the request must
be held during the access. This usually takes place automatically through
a file handle. Use \ ``media_request_unlock_for_access``\  when done.

.. _`media_request_unlock_for_access`:

media_request_unlock_for_access
===============================

.. c:function:: void media_request_unlock_for_access(struct media_request *req)

    Unlock a request previously locked for access

    :param req:
        The media request
    :type req: struct media_request \*

.. _`media_request_unlock_for_access.description`:

Description
-----------

Unlock a request that has previously been locked using
\ ``media_request_lock_for_access``\ .

.. _`media_request_lock_for_update`:

media_request_lock_for_update
=============================

.. c:function:: int media_request_lock_for_update(struct media_request *req)

    Lock the request for updating its objects

    :param req:
        The media request
    :type req: struct media_request \*

.. _`media_request_lock_for_update.description`:

Description
-----------

Use before updating a request, i.e. adding, modifying or removing a request
object in it. A reference to the request must be held during the update. This
usually takes place automatically through a file handle. Use
\ ``media_request_unlock_for_update``\  when done.

.. _`media_request_unlock_for_update`:

media_request_unlock_for_update
===============================

.. c:function:: void media_request_unlock_for_update(struct media_request *req)

    Unlock a request previously locked for update

    :param req:
        The media request
    :type req: struct media_request \*

.. _`media_request_unlock_for_update.description`:

Description
-----------

Unlock a request that has previously been locked using
\ ``media_request_lock_for_update``\ .

.. _`media_request_get`:

media_request_get
=================

.. c:function:: void media_request_get(struct media_request *req)

    Get the media request

    :param req:
        The media request
    :type req: struct media_request \*

.. _`media_request_get.description`:

Description
-----------

Get the media request.

.. _`media_request_put`:

media_request_put
=================

.. c:function:: void media_request_put(struct media_request *req)

    Put the media request

    :param req:
        The media request
    :type req: struct media_request \*

.. _`media_request_put.description`:

Description
-----------

Put the media request. The media request will be released
when the refcount reaches 0.

.. _`media_request_get_by_fd`:

media_request_get_by_fd
=======================

.. c:function:: struct media_request *media_request_get_by_fd(struct media_device *mdev, int request_fd)

    Get a media request by fd

    :param mdev:
        Media device this request belongs to
    :type mdev: struct media_device \*

    :param request_fd:
        The file descriptor of the request
    :type request_fd: int

.. _`media_request_get_by_fd.description`:

Description
-----------

Get the request represented by \ ``request_fd``\  that is owned
by the media device.

Return a -EACCES error pointer if requests are not supported
by this driver. Return -EINVAL if the request was not found.
Return the pointer to the request if found: the caller will
have to call \ ``media_request_put``\  when it finished using the
request.

.. _`media_request_alloc`:

media_request_alloc
===================

.. c:function:: int media_request_alloc(struct media_device *mdev, int *alloc_fd)

    Allocate the media request

    :param mdev:
        Media device this request belongs to
    :type mdev: struct media_device \*

    :param alloc_fd:
        Store the request's file descriptor in this int
    :type alloc_fd: int \*

.. _`media_request_alloc.description`:

Description
-----------

Allocated the media request and put the fd in \ ``alloc_fd``\ .

.. _`media_request_object_ops`:

struct media_request_object_ops
===============================

.. c:type:: struct media_request_object_ops

    Media request object operations

.. _`media_request_object_ops.definition`:

Definition
----------

.. code-block:: c

    struct media_request_object_ops {
        int (*prepare)(struct media_request_object *object);
        void (*unprepare)(struct media_request_object *object);
        void (*queue)(struct media_request_object *object);
        void (*unbind)(struct media_request_object *object);
        void (*release)(struct media_request_object *object);
    }

.. _`media_request_object_ops.members`:

Members
-------

prepare
    Validate and prepare the request object, optional.

unprepare
    Unprepare the request object, optional.

queue
    Queue the request object, optional.

unbind
    Unbind the request object, optional.

release
    Release the request object, required.

.. _`media_request_object`:

struct media_request_object
===========================

.. c:type:: struct media_request_object

    An opaque object that belongs to a media request

.. _`media_request_object.definition`:

Definition
----------

.. code-block:: c

    struct media_request_object {
        const struct media_request_object_ops *ops;
        void *priv;
        struct media_request *req;
        struct list_head list;
        struct kref kref;
        bool completed;
    }

.. _`media_request_object.members`:

Members
-------

ops
    object's operations

priv
    object's priv pointer

req
    the request this object belongs to (can be NULL)

list
    List entry of the object for \ ``struct``\  media_request

kref
    Reference count of the object, acquire before releasing req->lock

completed
    If true, then this object was completed.

.. _`media_request_object.description`:

Description
-----------

An object related to the request. This struct is always embedded in
another struct that contains the actual data for this request object.

.. _`media_request_object_get`:

media_request_object_get
========================

.. c:function:: void media_request_object_get(struct media_request_object *obj)

    Get a media request object

    :param obj:
        The object
    :type obj: struct media_request_object \*

.. _`media_request_object_get.description`:

Description
-----------

Get a media request object.

.. _`media_request_object_put`:

media_request_object_put
========================

.. c:function:: void media_request_object_put(struct media_request_object *obj)

    Put a media request object

    :param obj:
        The object
    :type obj: struct media_request_object \*

.. _`media_request_object_put.description`:

Description
-----------

Put a media request object. Once all references are gone, the
object's memory is released.

.. _`media_request_object_find`:

media_request_object_find
=========================

.. c:function:: struct media_request_object *media_request_object_find(struct media_request *req, const struct media_request_object_ops *ops, void *priv)

    Find an object in a request

    :param req:
        The media request
    :type req: struct media_request \*

    :param ops:
        Find an object with this ops value
    :type ops: const struct media_request_object_ops \*

    :param priv:
        Find an object with this priv value
    :type priv: void \*

.. _`media_request_object_find.description`:

Description
-----------

Both \ ``ops``\  and \ ``priv``\  must be non-NULL.

Returns the object pointer or NULL if not found. The caller must
call \ :c:func:`media_request_object_put`\  once it finished using the object.

Since this function needs to walk the list of objects it takes
the \ ``req->lock``\  spin lock to make this safe.

.. _`media_request_object_init`:

media_request_object_init
=========================

.. c:function:: void media_request_object_init(struct media_request_object *obj)

    Initialise a media request object

    :param obj:
        The object
    :type obj: struct media_request_object \*

.. _`media_request_object_init.description`:

Description
-----------

Initialise a media request object. The object will be released using the
release callback of the ops once it has no references (this function
initialises references to one).

.. _`media_request_object_bind`:

media_request_object_bind
=========================

.. c:function:: int media_request_object_bind(struct media_request *req, const struct media_request_object_ops *ops, void *priv, bool is_buffer, struct media_request_object *obj)

    Bind a media request object to a request

    :param req:
        The media request
    :type req: struct media_request \*

    :param ops:
        The object ops for this object
    :type ops: const struct media_request_object_ops \*

    :param priv:
        A driver-specific priv pointer associated with this object
    :type priv: void \*

    :param is_buffer:
        Set to true if the object a buffer object.
    :type is_buffer: bool

    :param obj:
        The object
    :type obj: struct media_request_object \*

.. _`media_request_object_bind.description`:

Description
-----------

Bind this object to the request and set the ops and priv values of
the object so it can be found later with \ :c:func:`media_request_object_find`\ .

Every bound object must be unbound or completed by the kernel at some
point in time, otherwise the request will never complete. When the
request is released all completed objects will be unbound by the
request core code.

Buffer objects will be added to the end of the request's object
list, non-buffer objects will be added to the front of the list.
This ensures that all buffer objects are at the end of the list
and that all non-buffer objects that they depend on are processed
first.

.. _`media_request_object_unbind`:

media_request_object_unbind
===========================

.. c:function:: void media_request_object_unbind(struct media_request_object *obj)

    Unbind a media request object

    :param obj:
        The object
    :type obj: struct media_request_object \*

.. _`media_request_object_unbind.description`:

Description
-----------

Unbind the media request object from the request.

.. _`media_request_object_complete`:

media_request_object_complete
=============================

.. c:function:: void media_request_object_complete(struct media_request_object *obj)

    Mark the media request object as complete

    :param obj:
        The object
    :type obj: struct media_request_object \*

.. _`media_request_object_complete.description`:

Description
-----------

Mark the media request object as complete. Only bound objects can
be completed.

.. This file was automatic generated / don't edit.

