.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pstore.h

.. _`pstore_record`:

struct pstore_record
====================

.. c:type:: struct pstore_record

    details of a pstore record entry

.. _`pstore_record.definition`:

Definition
----------

.. code-block:: c

    struct pstore_record {
        struct pstore_info *psi;
        enum pstore_type_id type;
        u64 id;
        struct timespec time;
        char *buf;
        ssize_t size;
        ssize_t ecc_notice_size;
        int count;
        enum kmsg_dump_reason reason;
        unsigned int part;
        bool compressed;
    }

.. _`pstore_record.members`:

Members
-------

psi
    pstore backend driver information

type
    pstore record type

id
    per-type unique identifier for record

time
    timestamp of the record

buf
    pointer to record contents

size
    size of \ ``buf``\ 

ecc_notice_size
    ECC information for \ ``buf``\ 

count
    Oops count since boot

reason
    kdump reason for notification

part
    position in a multipart record

compressed
    whether the buffer is compressed

.. _`pstore_record.description`:

Description
-----------

Valid for PSTORE_TYPE_DMESG \ ``type``\ :

.. _`pstore_info`:

struct pstore_info
==================

.. c:type:: struct pstore_info

    backend pstore driver structure

.. _`pstore_info.definition`:

Definition
----------

.. code-block:: c

    struct pstore_info {
        struct module *owner;
        char *name;
        spinlock_t buf_lock;
        char *buf;
        size_t bufsize;
        struct mutex read_mutex;
        int flags;
        void *data;
        int (*open)(struct pstore_info *psi);
        int (*close)(struct pstore_info *psi);
        ssize_t (*read)(struct pstore_record *record);
        int (*write)(struct pstore_record *record);
        int (*write_user)(struct pstore_record *record, const char __user *buf);
        int (*erase)(struct pstore_record *record);
    }

.. _`pstore_info.members`:

Members
-------

owner
    module which is repsonsible for this backend driver

name
    name of the backend driver

buf_lock
    spinlock to serialize access to \ ``buf``\ 

buf
    pointer to userspace contents to write to backend

bufsize
    size of \ ``buf``\  available for crash dump writes

read_mutex
    serializes \ ``open``\ , \ ``read``\ , \ ``close``\ , and \ ``erase``\  callbacks

flags
    bitfield of frontends the backend can accept writes for

data
    backend-private pointer passed back during callbacks

open

    Notify backend that pstore is starting a full read of backend
    records. Followed by one or more \ ``read``\  calls, and a final \ ``close``\ .

close
    Notify backend that pstore has finished a full read of backend
    records. Always preceded by an \ ``open``\  call and one or more \ ``read``\ 
    calls.

read
    Read next available backend record. Called after a successful
    \ ``open``\ .

write
    A newly generated record needs to be written to backend storage.

write_user
    Perform a frontend write to a backend record, using a specified
    buffer that is coming directly from userspace, instead of the
    \ ``record``\  \ ``buf``\ .

erase
    Delete a record from backend storage.  Different backends
    identify records differently, so entire original record is
    passed back to assist in identification of what the backend
    should remove from storage.

.. _`pstore_info.description`:

Description
-----------

Returns 0 on success, and non-zero on error.

Returns 0 on success, and non-zero on error. (Though pstore will
ignore the error.)

Returns record size on success, zero when no more records are
available, or negative on error.

Returns 0 on success, and non-zero on error.

Returns 0 on success, and non-zero on error.

Returns 0 on success, and non-zero on error.

.. This file was automatic generated / don't edit.

