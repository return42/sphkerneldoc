.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/9p/9p.h

.. _`p9_debug_flags`:

enum p9_debug_flags
===================

.. c:type:: enum p9_debug_flags

    bits for mount time debug parameter

.. _`p9_debug_flags.definition`:

Definition
----------

.. code-block:: c

    enum p9_debug_flags {
        P9_DEBUG_ERROR,
        P9_DEBUG_9P,
        P9_DEBUG_VFS,
        P9_DEBUG_CONV,
        P9_DEBUG_MUX,
        P9_DEBUG_TRANS,
        P9_DEBUG_SLABS,
        P9_DEBUG_FCALL,
        P9_DEBUG_FID,
        P9_DEBUG_PKT,
        P9_DEBUG_FSC,
        P9_DEBUG_VPKT
    };

.. _`p9_debug_flags.constants`:

Constants
---------

P9_DEBUG_ERROR
    more verbose error messages including original error string

P9_DEBUG_9P
    9P protocol tracing

P9_DEBUG_VFS
    VFS API tracing

P9_DEBUG_CONV
    protocol conversion tracing

P9_DEBUG_MUX
    trace management of concurrent transactions

P9_DEBUG_TRANS
    transport tracing

P9_DEBUG_SLABS
    memory management tracing

P9_DEBUG_FCALL
    verbose dump of protocol messages

P9_DEBUG_FID
    fid allocation/deallocation tracking

P9_DEBUG_PKT
    packet marshalling/unmarshalling

P9_DEBUG_FSC
    FS-cache tracing

P9_DEBUG_VPKT
    Verbose packet debugging (full packet dump)

.. _`p9_debug_flags.description`:

Description
-----------

These flags are passed at mount time to turn on various levels of
verbosity and tracing which will be output to the system logs.

.. _`p9_msg_t`:

enum p9_msg_t
=============

.. c:type:: enum p9_msg_t

    9P message types

.. _`p9_msg_t.definition`:

Definition
----------

.. code-block:: c

    enum p9_msg_t {
        P9_TLERROR,
        P9_RLERROR,
        P9_TSTATFS,
        P9_RSTATFS,
        P9_TLOPEN,
        P9_RLOPEN,
        P9_TLCREATE,
        P9_RLCREATE,
        P9_TSYMLINK,
        P9_RSYMLINK,
        P9_TMKNOD,
        P9_RMKNOD,
        P9_TRENAME,
        P9_RRENAME,
        P9_TREADLINK,
        P9_RREADLINK,
        P9_TGETATTR,
        P9_RGETATTR,
        P9_TSETATTR,
        P9_RSETATTR,
        P9_TXATTRWALK,
        P9_RXATTRWALK,
        P9_TXATTRCREATE,
        P9_RXATTRCREATE,
        P9_TREADDIR,
        P9_RREADDIR,
        P9_TFSYNC,
        P9_RFSYNC,
        P9_TLOCK,
        P9_RLOCK,
        P9_TGETLOCK,
        P9_RGETLOCK,
        P9_TLINK,
        P9_RLINK,
        P9_TMKDIR,
        P9_RMKDIR,
        P9_TRENAMEAT,
        P9_RRENAMEAT,
        P9_TUNLINKAT,
        P9_RUNLINKAT,
        P9_TVERSION,
        P9_RVERSION,
        P9_TAUTH,
        P9_RAUTH,
        P9_TATTACH,
        P9_RATTACH,
        P9_TERROR,
        P9_RERROR,
        P9_TFLUSH,
        P9_RFLUSH,
        P9_TWALK,
        P9_RWALK,
        P9_TOPEN,
        P9_ROPEN,
        P9_TCREATE,
        P9_RCREATE,
        P9_TREAD,
        P9_RREAD,
        P9_TWRITE,
        P9_RWRITE,
        P9_TCLUNK,
        P9_RCLUNK,
        P9_TREMOVE,
        P9_RREMOVE,
        P9_TSTAT,
        P9_RSTAT,
        P9_TWSTAT,
        P9_RWSTAT
    };

.. _`p9_msg_t.constants`:

Constants
---------

P9_TLERROR
    not used

P9_RLERROR
    response for any failed request for 9P2000.L

P9_TSTATFS
    file system status request

P9_RSTATFS
    file system status response

P9_TLOPEN
    *undescribed*

P9_RLOPEN
    *undescribed*

P9_TLCREATE
    prepare a handle for I/O on an new file for 9P2000.L

P9_RLCREATE
    response with file access information for 9P2000.L

P9_TSYMLINK
    make symlink request

P9_RSYMLINK
    make symlink response

P9_TMKNOD
    create a special file object request

P9_RMKNOD
    create a special file object response

P9_TRENAME
    rename request

P9_RRENAME
    rename response

P9_TREADLINK
    *undescribed*

P9_RREADLINK
    *undescribed*

P9_TGETATTR
    *undescribed*

P9_RGETATTR
    *undescribed*

P9_TSETATTR
    *undescribed*

P9_RSETATTR
    *undescribed*

P9_TXATTRWALK
    *undescribed*

P9_RXATTRWALK
    *undescribed*

P9_TXATTRCREATE
    *undescribed*

P9_RXATTRCREATE
    *undescribed*

P9_TREADDIR
    *undescribed*

P9_RREADDIR
    *undescribed*

P9_TFSYNC
    *undescribed*

P9_RFSYNC
    *undescribed*

P9_TLOCK
    *undescribed*

P9_RLOCK
    *undescribed*

P9_TGETLOCK
    *undescribed*

P9_RGETLOCK
    *undescribed*

P9_TLINK
    *undescribed*

P9_RLINK
    *undescribed*

P9_TMKDIR
    create a directory request

P9_RMKDIR
    create a directory response

P9_TRENAMEAT
    *undescribed*

P9_RRENAMEAT
    *undescribed*

P9_TUNLINKAT
    *undescribed*

P9_RUNLINKAT
    *undescribed*

P9_TVERSION
    version handshake request

P9_RVERSION
    version handshake response

P9_TAUTH
    request to establish authentication channel

P9_RAUTH
    response with authentication information

P9_TATTACH
    establish user access to file service

P9_RATTACH
    response with top level handle to file hierarchy

P9_TERROR
    not used

P9_RERROR
    response for any failed request

P9_TFLUSH
    request to abort a previous request

P9_RFLUSH
    response when previous request has been cancelled

P9_TWALK
    descend a directory hierarchy

P9_RWALK
    response with new handle for position within hierarchy

P9_TOPEN
    prepare a handle for I/O on an existing file

P9_ROPEN
    response with file access information

P9_TCREATE
    prepare a handle for I/O on a new file

P9_RCREATE
    response with file access information

P9_TREAD
    request to transfer data from a file or directory

P9_RREAD
    response with data requested

P9_TWRITE
    reuqest to transfer data to a file

P9_RWRITE
    response with out much data was transferred to file

P9_TCLUNK
    forget about a handle to an entity within the file system

P9_RCLUNK
    response when server has forgotten about the handle

P9_TREMOVE
    request to remove an entity from the hierarchy

P9_RREMOVE
    response when server has removed the entity

P9_TSTAT
    request file entity attributes

P9_RSTAT
    response with file entity attributes

P9_TWSTAT
    request to update file entity attributes

P9_RWSTAT
    response when file entity attributes are updated

.. _`p9_msg_t.description`:

Description
-----------

There are 14 basic operations in 9P2000, paired as
requests and responses.  The one special case is ERROR
as there is no \ ``P9_TERROR``\  request for clients to transmit to
the server, but the server may respond to any other request
with an \ ``P9_RERROR``\ .

See Also: http://plan9.bell-labs.com/sys/man/5/INDEX.html

.. _`p9_open_mode_t`:

enum p9_open_mode_t
===================

.. c:type:: enum p9_open_mode_t

    9P open modes

.. _`p9_open_mode_t.definition`:

Definition
----------

.. code-block:: c

    enum p9_open_mode_t {
        P9_OREAD,
        P9_OWRITE,
        P9_ORDWR,
        P9_OEXEC,
        P9_OTRUNC,
        P9_OREXEC,
        P9_ORCLOSE,
        P9_OAPPEND,
        P9_OEXCL
    };

.. _`p9_open_mode_t.constants`:

Constants
---------

P9_OREAD
    open file for reading only

P9_OWRITE
    open file for writing only

P9_ORDWR
    open file for reading or writing

P9_OEXEC
    open file for execution

P9_OTRUNC
    truncate file to zero-length before opening it

P9_OREXEC
    close the file when an exec(2) system call is made

P9_ORCLOSE
    remove the file when the file is closed

P9_OAPPEND
    open the file and seek to the end

P9_OEXCL
    only create a file, do not open it

.. _`p9_open_mode_t.description`:

Description
-----------

9P open modes differ slightly from Posix standard modes.
In particular, there are extra modes which specify different
semantic behaviors than may be available on standard Posix
systems.  For example, \ ``P9_OREXEC``\  and \ ``P9_ORCLOSE``\  are modes that
most likely will not be issued from the Linux VFS client, but may
be supported by servers.

See Also: http://plan9.bell-labs.com/magic/man2html/2/open

.. _`p9_perm_t`:

enum p9_perm_t
==============

.. c:type:: enum p9_perm_t

    9P permissions

.. _`p9_perm_t.definition`:

Definition
----------

.. code-block:: c

    enum p9_perm_t {
        P9_DMDIR,
        P9_DMAPPEND,
        P9_DMEXCL,
        P9_DMMOUNT,
        P9_DMAUTH,
        P9_DMTMP,
        P9_DMSYMLINK,
        P9_DMLINK,
        P9_DMDEVICE,
        P9_DMNAMEDPIPE,
        P9_DMSOCKET,
        P9_DMSETUID,
        P9_DMSETGID,
        P9_DMSETVTX
    };

.. _`p9_perm_t.constants`:

Constants
---------

P9_DMDIR
    mode bit for directories

P9_DMAPPEND
    mode bit for is append-only

P9_DMEXCL
    mode bit for excluse use (only one open handle allowed)

P9_DMMOUNT
    mode bit for mount points

P9_DMAUTH
    mode bit for authentication file

P9_DMTMP
    mode bit for non-backed-up files

P9_DMSYMLINK
    mode bit for symbolic links (9P2000.u)

P9_DMLINK
    mode bit for hard-link (9P2000.u)

P9_DMDEVICE
    mode bit for device files (9P2000.u)

P9_DMNAMEDPIPE
    mode bit for named pipe (9P2000.u)

P9_DMSOCKET
    mode bit for socket (9P2000.u)

P9_DMSETUID
    mode bit for setuid (9P2000.u)

P9_DMSETGID
    mode bit for setgid (9P2000.u)

P9_DMSETVTX
    mode bit for sticky bit (9P2000.u)

.. _`p9_perm_t.description`:

Description
-----------

9P permissions differ slightly from Posix standard modes.

See Also: http://plan9.bell-labs.com/magic/man2html/2/stat

.. _`p9_qid_t`:

enum p9_qid_t
=============

.. c:type:: enum p9_qid_t

    QID types

.. _`p9_qid_t.definition`:

Definition
----------

.. code-block:: c

    enum p9_qid_t {
        P9_QTDIR,
        P9_QTAPPEND,
        P9_QTEXCL,
        P9_QTMOUNT,
        P9_QTAUTH,
        P9_QTTMP,
        P9_QTSYMLINK,
        P9_QTLINK,
        P9_QTFILE
    };

.. _`p9_qid_t.constants`:

Constants
---------

P9_QTDIR
    directory

P9_QTAPPEND
    append-only

P9_QTEXCL
    excluse use (only one open handle allowed)

P9_QTMOUNT
    mount points

P9_QTAUTH
    authentication file

P9_QTTMP
    non-backed-up files

P9_QTSYMLINK
    symbolic links (9P2000.u)

P9_QTLINK
    hard-link (9P2000.u)

P9_QTFILE
    normal files

.. _`p9_qid_t.description`:

Description
-----------

QID types are a subset of permissions - they are primarily
used to differentiate semantics for a file system entity via
a jump-table.  Their value is also the most significant 16 bits
of the permission_t

See Also: http://plan9.bell-labs.com/magic/man2html/2/stat

.. _`p9_qid`:

struct p9_qid
=============

.. c:type:: struct p9_qid

    file system entity information

.. _`p9_qid.definition`:

Definition
----------

.. code-block:: c

    struct p9_qid {
        u8 type;
        u32 version;
        u64 path;
    }

.. _`p9_qid.members`:

Members
-------

type
    8-bit type \ :c:type:`struct p9_qid_t <p9_qid_t>`\ 

version
    16-bit monotonically incrementing version number

path
    64-bit per-server-unique ID for a file system element

.. _`p9_qid.description`:

Description
-----------

qids are identifiers used by 9P servers to track file system
entities.  The type is used to differentiate semantics for operations
on the entity (ie. read means something different on a directory than
on a file).  The path provides a server unique index for an entity
(roughly analogous to an inode number), while the version is updated
every time a file is modified and can be used to maintain cache
coherency between clients and serves.
Servers will often differentiate purely synthetic entities by setting
their version to 0, signaling that they should never be cached and
should be accessed synchronously.

See Also://plan9.bell-labs.com/magic/man2html/2/stat

.. _`p9_wstat`:

struct p9_wstat
===============

.. c:type:: struct p9_wstat

    file system metadata information

.. _`p9_wstat.definition`:

Definition
----------

.. code-block:: c

    struct p9_wstat {
        u16 size;
        u16 type;
        u32 dev;
        struct p9_qid qid;
        u32 mode;
        u32 atime;
        u32 mtime;
        u64 length;
        const char *name;
        const char *uid;
        const char *gid;
        const char *muid;
        char *extension;
        kuid_t n_uid;
        kgid_t n_gid;
        kuid_t n_muid;
    }

.. _`p9_wstat.members`:

Members
-------

size
    length prefix for this stat structure instance

type
    the type of the server (equivalent to a major number)

dev
    the sub-type of the server (equivalent to a minor number)

qid
    unique id from the server of type \ :c:type:`struct p9_qid <p9_qid>`\ 

mode
    Plan 9 format permissions of type \ :c:type:`struct p9_perm_t <p9_perm_t>`\ 

atime
    Last access/read time

mtime
    Last modify/write time

length
    file length

name
    last element of path (aka filename)

uid
    owner name

gid
    group owner

muid
    last modifier

extension
    area used to encode extended UNIX support

n_uid
    numeric user id of owner (part of 9p2000.u extension)

n_gid
    numeric group id (part of 9p2000.u extension)

n_muid
    numeric user id of laster modifier (part of 9p2000.u extension)

.. _`p9_wstat.description`:

Description
-----------

See Also: http://plan9.bell-labs.com/magic/man2html/2/stat

.. _`p9_iattr_dotl`:

struct p9_iattr_dotl
====================

.. c:type:: struct p9_iattr_dotl

    P9 inode attribute for setattr

.. _`p9_iattr_dotl.definition`:

Definition
----------

.. code-block:: c

    struct p9_iattr_dotl {
        u32 valid;
        u32 mode;
        kuid_t uid;
        kgid_t gid;
        u64 size;
        u64 atime_sec;
        u64 atime_nsec;
        u64 mtime_sec;
        u64 mtime_nsec;
    }

.. _`p9_iattr_dotl.members`:

Members
-------

valid
    bitfield specifying which fields are valid
    same as in struct iattr

mode
    File permission bits

uid
    user id of owner

gid
    group id

size
    File size

atime_sec
    Last access time, seconds

atime_nsec
    Last access time, nanoseconds

mtime_sec
    Last modification time, seconds

mtime_nsec
    Last modification time, nanoseconds

.. _`p9_fcall`:

struct p9_fcall
===============

.. c:type:: struct p9_fcall

    primary packet structure

.. _`p9_fcall.definition`:

Definition
----------

.. code-block:: c

    struct p9_fcall {
        u32 size;
        u8 id;
        u16 tag;
        size_t offset;
        size_t capacity;
        struct kmem_cache *cache;
        u8 *sdata;
    }

.. _`p9_fcall.members`:

Members
-------

size
    prefixed length of the structure

id
    protocol operating identifier of type \ :c:type:`struct p9_msg_t <p9_msg_t>`\ 

tag
    transaction id of the request

offset
    used by marshalling routines to track current position in buffer

capacity
    used by marshalling routines to track total malloc'd capacity

cache
    *undescribed*

sdata
    payload

.. _`p9_fcall.description`:

Description
-----------

\ :c:type:`struct p9_fcall <p9_fcall>`\  represents the structure for all 9P RPC
transactions.  Requests are packaged into fcalls, and reponses
must be extracted from them.

See Also: http://plan9.bell-labs.com/magic/man2html/2/fcall

.. This file was automatic generated / don't edit.

