.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/v9fs.h

.. _`p9_cache_modes`:

enum p9_cache_modes
===================

.. c:type:: enum p9_cache_modes

    user specified cache preferences

.. _`p9_cache_modes.definition`:

Definition
----------

.. code-block:: c

    enum p9_cache_modes {
        CACHE_NONE,
        CACHE_MMAP,
        CACHE_LOOSE,
        CACHE_FSCACHE
    };

.. _`p9_cache_modes.constants`:

Constants
---------

CACHE_NONE
    do not cache data, dentries, or directory contents (default)

CACHE_MMAP
    *undescribed*

CACHE_LOOSE
    cache data, dentries, and directory contents w/no consistency

CACHE_FSCACHE
    *undescribed*

.. _`p9_cache_modes.description`:

Description
-----------

eventually support loose, tight, time, session, default always none

.. _`v9fs_session_info`:

struct v9fs_session_info
========================

.. c:type:: struct v9fs_session_info

    per-instance session information

.. _`v9fs_session_info.definition`:

Definition
----------

.. code-block:: c

    struct v9fs_session_info {
        unsigned char flags;
        unsigned char nodev;
        unsigned short debug;
        unsigned int afid;
        unsigned int cache;
        #ifdef CONFIG_9P_FSCACHE
        char *cachetag;
        struct fscache_cookie *fscache;
        #endif
        char *uname;
        char *aname;
        unsigned int maxdata;
        kuid_t dfltuid;
        kgid_t dfltgid;
        kuid_t uid;
        struct p9_client *clnt;
        struct list_head slist;
        struct backing_dev_info bdi;
        struct rw_semaphore rename_sem;
    }

.. _`v9fs_session_info.members`:

Members
-------

flags
    session options of type \ :c:type:`struct p9_session_flags <p9_session_flags>`

nodev
    set to 1 to disable device mapping

debug
    debug level

afid
    authentication handle

cache
    cache mode of type \ :c:type:`struct p9_cache_modes <p9_cache_modes>`

cachetag
    the tag of the cache associated with this session

fscache
    session cookie associated with FS-Cache

uname
    string user name to mount hierarchy as

aname
    mount specifier for remote hierarchy

maxdata
    maximum data to be sent/recvd per protocol message

dfltuid
    default numeric userid to mount hierarchy as

dfltgid
    default numeric groupid to mount hierarchy as

uid
    if \ ``V9FS_ACCESS_SINGLE``\ , the numeric uid which mounted the hierarchy

clnt
    reference to 9P network client instantiated for this session

slist
    reference to list of registered 9p sessions

bdi
    *undescribed*

rename_sem
    *undescribed*

.. _`v9fs_session_info.description`:

Description
-----------

This structure holds state for each session instance established during
a \ :c:func:`sys_mount`\  .

.. _`v9fs_session_info.bugs`:

Bugs
----

there seems to be a lot of state which could be condensed and/or
removed.

.. _`v9fs_get_inode_from_fid`:

v9fs_get_inode_from_fid
=======================

.. c:function:: struct inode *v9fs_get_inode_from_fid(struct v9fs_session_info *v9ses, struct p9_fid *fid, struct super_block *sb)

    Helper routine to populate an inode by issuing a attribute request

    :param struct v9fs_session_info \*v9ses:
        session information

    :param struct p9_fid \*fid:
        fid to issue attribute request for

    :param struct super_block \*sb:
        superblock on which to create inode

.. _`v9fs_get_new_inode_from_fid`:

v9fs_get_new_inode_from_fid
===========================

.. c:function:: struct inode *v9fs_get_new_inode_from_fid(struct v9fs_session_info *v9ses, struct p9_fid *fid, struct super_block *sb)

    Helper routine to populate an inode by issuing a attribute request

    :param struct v9fs_session_info \*v9ses:
        session information

    :param struct p9_fid \*fid:
        fid to issue attribute request for

    :param struct super_block \*sb:
        superblock on which to create inode

.. This file was automatic generated / don't edit.

