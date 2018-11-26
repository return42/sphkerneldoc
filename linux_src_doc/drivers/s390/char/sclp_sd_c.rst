.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/sclp_sd.c

.. _`sclp_sd_data`:

struct sclp_sd_data
===================

.. c:type:: struct sclp_sd_data

    Result of a Store Data request

.. _`sclp_sd_data.definition`:

Definition
----------

.. code-block:: c

    struct sclp_sd_data {
        size_t esize_bytes;
        size_t dsize_bytes;
        void *data;
    }

.. _`sclp_sd_data.members`:

Members
-------

esize_bytes
    Resulting esize in bytes

dsize_bytes
    Resulting dsize in bytes

data
    Pointer to data - must be released using \ :c:func:`vfree`\ 

.. _`sclp_sd_listener`:

struct sclp_sd_listener
=======================

.. c:type:: struct sclp_sd_listener

    Listener for asynchronous Store Data response

.. _`sclp_sd_listener.definition`:

Definition
----------

.. code-block:: c

    struct sclp_sd_listener {
        struct list_head list;
        u32 id;
        struct completion completion;
        struct sclp_sd_evbuf evbuf;
    }

.. _`sclp_sd_listener.members`:

Members
-------

list
    For enqueueing this struct

id
    Event ID of response to listen for

completion
    Can be used to wait for response

evbuf
    Contains the resulting Store Data response after completion

.. _`sclp_sd_file`:

struct sclp_sd_file
===================

.. c:type:: struct sclp_sd_file

    Sysfs representation of a Store Data entity

.. _`sclp_sd_file.definition`:

Definition
----------

.. code-block:: c

    struct sclp_sd_file {
        struct kobject kobj;
        struct bin_attribute data_attr;
        struct mutex data_mutex;
        struct sclp_sd_data data;
        u8 di;
    }

.. _`sclp_sd_file.members`:

Members
-------

kobj
    Kobject

data_attr
    Attribute for accessing data contents

data_mutex
    Mutex to serialize access and updates to \ ``data``\ 

data
    Data associated with this entity

di
    DI value associated with this entity

.. _`sclp_sd_listener_add`:

sclp_sd_listener_add
====================

.. c:function:: void sclp_sd_listener_add(struct sclp_sd_listener *listener)

    Add listener for Store Data responses

    :param listener:
        Listener to add
    :type listener: struct sclp_sd_listener \*

.. _`sclp_sd_listener_remove`:

sclp_sd_listener_remove
=======================

.. c:function:: void sclp_sd_listener_remove(struct sclp_sd_listener *listener)

    Remove listener for Store Data responses

    :param listener:
        Listener to remove
    :type listener: struct sclp_sd_listener \*

.. _`sclp_sd_listener_init`:

sclp_sd_listener_init
=====================

.. c:function:: void sclp_sd_listener_init(struct sclp_sd_listener *listener, u32 id)

    Initialize a Store Data response listener

    :param listener:
        *undescribed*
    :type listener: struct sclp_sd_listener \*

    :param id:
        Event ID to listen for
    :type id: u32

.. _`sclp_sd_listener_init.description`:

Description
-----------

Initialize a listener for asynchronous Store Data responses. This listener
can afterwards be used to wait for a specific response and to retrieve
the associated response data.

.. _`sclp_sd_receiver`:

sclp_sd_receiver
================

.. c:function:: void sclp_sd_receiver(struct evbuf_header *evbuf_hdr)

    Receiver for Store Data events

    :param evbuf_hdr:
        Header of received events
    :type evbuf_hdr: struct evbuf_header \*

.. _`sclp_sd_receiver.description`:

Description
-----------

Process Store Data events and complete listeners with matching event IDs.

.. _`sclp_sd_sync`:

sclp_sd_sync
============

.. c:function:: int sclp_sd_sync(unsigned long page, u8 eq, u8 di, u64 sat, u64 sa, u32 *dsize_ptr, u32 *esize_ptr)

    Perform Store Data request synchronously

    :param page:
        Address of work page - must be below 2GB
    :type page: unsigned long

    :param eq:
        Input EQ value
    :type eq: u8

    :param di:
        Input DI value
    :type di: u8

    :param sat:
        Input SAT value
    :type sat: u64

    :param sa:
        Input SA value used to specify the address of the target buffer
    :type sa: u64

    :param dsize_ptr:
        Optional pointer to input and output DSIZE value
    :type dsize_ptr: u32 \*

    :param esize_ptr:
        Optional pointer to output ESIZE value
    :type esize_ptr: u32 \*

.. _`sclp_sd_sync.description`:

Description
-----------

Perform Store Data request with specified parameters and wait for completion.

Return \ ``0``\  on success and store resulting DSIZE and ESIZE values in
\ ``dsize_ptr``\  and \ ``esize_ptr``\  (if provided). Return non-zero on error.

.. _`sclp_sd_store_data`:

sclp_sd_store_data
==================

.. c:function:: int sclp_sd_store_data(struct sclp_sd_data *result, u8 di)

    Obtain data for specified Store Data entity

    :param result:
        Resulting data
    :type result: struct sclp_sd_data \*

    :param di:
        DI value associated with this entity
    :type di: u8

.. _`sclp_sd_store_data.description`:

Description
-----------

Perform a series of Store Data requests to obtain the size and contents of
the specified Store Data entity.

.. _`sclp_sd_store_data.return`:

Return
------

\ ``0``\ :       Success - result is stored in \ ``result``\ . \ ``result->data``\  must be
released using \ :c:func:`vfree`\  after use.
\ ``-ENOENT``\ : No data available for this entity
%<0:      Other error

.. _`sclp_sd_data_reset`:

sclp_sd_data_reset
==================

.. c:function:: void sclp_sd_data_reset(struct sclp_sd_data *data)

    Reset Store Data result buffer

    :param data:
        Data buffer to reset
    :type data: struct sclp_sd_data \*

.. _`sclp_sd_data_reset.description`:

Description
-----------

Reset \ ``data``\  to initial state and release associated memory.

.. _`sclp_sd_file_release`:

sclp_sd_file_release
====================

.. c:function:: void sclp_sd_file_release(struct kobject *kobj)

    Release function for sclp_sd_file object

    :param kobj:
        Kobject embedded in sclp_sd_file object
    :type kobj: struct kobject \*

.. _`sclp_sd_file_update`:

sclp_sd_file_update
===================

.. c:function:: int sclp_sd_file_update(struct sclp_sd_file *sd_file)

    Update contents of sclp_sd_file object

    :param sd_file:
        Object to update
    :type sd_file: struct sclp_sd_file \*

.. _`sclp_sd_file_update.description`:

Description
-----------

Obtain the current version of data associated with the Store Data entity
\ ``sd_file``\ .

On success, return \ ``0``\  and generate a KOBJ_CHANGE event to indicate that the
data may have changed. Return non-zero otherwise.

.. _`sclp_sd_file_update_async`:

sclp_sd_file_update_async
=========================

.. c:function:: void sclp_sd_file_update_async(void *data, async_cookie_t cookie)

    Wrapper for asynchronous update call

    :param data:
        Object to update
    :type data: void \*

    :param cookie:
        *undescribed*
    :type cookie: async_cookie_t

.. _`reload_store`:

reload_store
============

.. c:function:: ssize_t reload_store(struct kobject *kobj, struct kobj_attribute *attr, const char *buf, size_t count)

    Store function for "reload" sysfs attribute

    :param kobj:
        Kobject of sclp_sd_file object
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        *undescribed*
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`reload_store.description`:

Description
-----------

Initiate a reload of the data associated with an sclp_sd_file object.

.. _`data_read`:

data_read
=========

.. c:function:: ssize_t data_read(struct file *file, struct kobject *kobj, struct bin_attribute *attr, char *buffer, loff_t off, size_t size)

    Read function for "read" sysfs attribute

    :param file:
        *undescribed*
    :type file: struct file \*

    :param kobj:
        Kobject of sclp_sd_file object
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct bin_attribute \*

    :param buffer:
        Target buffer
    :type buffer: char \*

    :param off:
        Requested file offset
    :type off: loff_t

    :param size:
        Requested number of bytes
    :type size: size_t

.. _`data_read.description`:

Description
-----------

Store the requested portion of the Store Data entity contents into the
specified buffer. Return the number of bytes stored on success, or \ ``0``\ 
on EOF.

.. _`sclp_sd_file_create`:

sclp_sd_file_create
===================

.. c:function:: struct sclp_sd_file *sclp_sd_file_create(const char *name, u8 di)

    Add a sysfs file representing a Store Data entity

    :param name:
        Name of file
    :type name: const char \*

    :param di:
        DI value associated with this entity
    :type di: u8

.. _`sclp_sd_file_create.description`:

Description
-----------

Create a sysfs directory with the given \ ``name``\  located under

/sys/firmware/sclp_sd/

The files in this directory can be used to access the contents of the Store
Data entity associated with \ ``DI``\ .

Return pointer to resulting sclp_sd_file object on success, \ ``NULL``\  otherwise.
The object must be freed by calling \ :c:func:`kobject_put`\  on the embedded kobject
pointer after use.

.. _`sclp_sd_init`:

sclp_sd_init
============

.. c:function:: int sclp_sd_init( void)

    Initialize sclp_sd support and register sysfs files

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

