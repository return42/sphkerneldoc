.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/netlabel.h

.. _`netlbl_lsm_cache`:

struct netlbl_lsm_cache
=======================

.. c:type:: struct netlbl_lsm_cache

    NetLabel LSM security attribute cache

.. _`netlbl_lsm_cache.definition`:

Definition
----------

.. code-block:: c

    struct netlbl_lsm_cache {
        atomic_t refcount;
        void (*free)(const void *data);
        void *data;
    }

.. _`netlbl_lsm_cache.members`:

Members
-------

refcount
    atomic reference counter

free
    LSM supplied function to free the cache data

data
    LSM supplied cache data

.. _`netlbl_lsm_cache.description`:

Description
-----------

This structure is provided for LSMs which wish to make use of the NetLabel
caching mechanism to store LSM specific data/attributes in the NetLabel
cache.  If the LSM has to perform a lot of translation from the NetLabel
security attributes into it's own internal representation then the cache
mechanism can provide a way to eliminate some or all of that translation
overhead on a cache hit.

.. _`netlbl_lsm_secattr`:

struct netlbl_lsm_secattr
=========================

.. c:type:: struct netlbl_lsm_secattr

    NetLabel LSM security attributes

.. _`netlbl_lsm_secattr.definition`:

Definition
----------

.. code-block:: c

    struct netlbl_lsm_secattr {
        u32 flags;
    #define NETLBL_SECATTR_NONE 0x00000000
    #define NETLBL_SECATTR_DOMAIN 0x00000001
    #define NETLBL_SECATTR_DOMAIN_CPY (NETLBL_SECATTR_DOMAIN | \
        NETLBL_SECATTR_FREE_DOMAIN)#define NETLBL_SECATTR_CACHE 0x00000002;
    #define NETLBL_SECATTR_MLS_LVL 0x00000004
    #define NETLBL_SECATTR_MLS_CAT 0x00000008
    #define NETLBL_SECATTR_SECID 0x00000010
    #define NETLBL_SECATTR_FREE_DOMAIN 0x01000000
    #define NETLBL_SECATTR_CACHEABLE (NETLBL_SECATTR_MLS_LVL | \
        NETLBL_SECATTR_MLS_CAT | \NETLBL_SECATTR_SECID)u32 type;
        char *domain;
        struct netlbl_lsm_cache *cache;
        struct attr;
    }

.. _`netlbl_lsm_secattr.members`:

Members
-------

flags
    indicate structure attributes, see NETLBL_SECATTR\_\*

0x00000002
    *undescribed*

type
    indicate the NLTYPE of the attributes

domain
    the NetLabel LSM domain

cache
    NetLabel LSM specific cache

attr
    *undescribed*

attr.mls
    MLS sensitivity label

attr.mls.cat
    MLS category bitmap

attr.mls.lvl
    MLS sensitivity level

attr.secid
    LSM specific secid token

.. _`netlbl_lsm_secattr.description`:

Description
-----------

This structure is used to pass security attributes between NetLabel and the
LSM modules.  The flags field is used to specify which fields within the
struct are valid and valid values can be created by bitwise OR'ing the
NETLBL_SECATTR\_\* defines.  The domain field is typically set by the LSM to
specify domain specific configuration settings and is not usually used by
NetLabel itself when returning security attributes to the LSM.

.. _`netlbl_secattr_cache_alloc`:

netlbl_secattr_cache_alloc
==========================

.. c:function:: struct netlbl_lsm_cache *netlbl_secattr_cache_alloc(gfp_t flags)

    Allocate and initialize a secattr cache

    :param gfp_t flags:
        the memory allocation flags

.. _`netlbl_secattr_cache_alloc.description`:

Description
-----------

Allocate and initialize a netlbl_lsm_cache structure.  Returns a pointer
on success, NULL on failure.

.. _`netlbl_secattr_cache_free`:

netlbl_secattr_cache_free
=========================

.. c:function:: void netlbl_secattr_cache_free(struct netlbl_lsm_cache *cache)

    Frees a netlbl_lsm_cache struct

    :param struct netlbl_lsm_cache \*cache:
        the struct to free

.. _`netlbl_secattr_cache_free.description`:

Description
-----------

Frees \ ``secattr``\  including all of the internal buffers.

.. _`netlbl_catmap_alloc`:

netlbl_catmap_alloc
===================

.. c:function:: struct netlbl_lsm_catmap *netlbl_catmap_alloc(gfp_t flags)

    Allocate a LSM secattr catmap

    :param gfp_t flags:
        memory allocation flags

.. _`netlbl_catmap_alloc.description`:

Description
-----------

Allocate memory for a LSM secattr catmap, returns a pointer on success, NULL
on failure.

.. _`netlbl_catmap_free`:

netlbl_catmap_free
==================

.. c:function:: void netlbl_catmap_free(struct netlbl_lsm_catmap *catmap)

    Free a LSM secattr catmap

    :param struct netlbl_lsm_catmap \*catmap:
        the category bitmap

.. _`netlbl_catmap_free.description`:

Description
-----------

Free a LSM secattr catmap.

.. _`netlbl_secattr_init`:

netlbl_secattr_init
===================

.. c:function:: void netlbl_secattr_init(struct netlbl_lsm_secattr *secattr)

    Initialize a netlbl_lsm_secattr struct

    :param struct netlbl_lsm_secattr \*secattr:
        the struct to initialize

.. _`netlbl_secattr_init.description`:

Description
-----------

Initialize an already allocated netlbl_lsm_secattr struct.

.. _`netlbl_secattr_destroy`:

netlbl_secattr_destroy
======================

.. c:function:: void netlbl_secattr_destroy(struct netlbl_lsm_secattr *secattr)

    Clears a netlbl_lsm_secattr struct

    :param struct netlbl_lsm_secattr \*secattr:
        the struct to clear

.. _`netlbl_secattr_destroy.description`:

Description
-----------

Destroys the \ ``secattr``\  struct, including freeing all of the internal buffers.
The struct must be reset with a call to \ :c:func:`netlbl_secattr_init`\  before reuse.

.. _`netlbl_secattr_alloc`:

netlbl_secattr_alloc
====================

.. c:function:: struct netlbl_lsm_secattr *netlbl_secattr_alloc(gfp_t flags)

    Allocate and initialize a netlbl_lsm_secattr struct

    :param gfp_t flags:
        the memory allocation flags

.. _`netlbl_secattr_alloc.description`:

Description
-----------

Allocate and initialize a netlbl_lsm_secattr struct.  Returns a valid
pointer on success, or NULL on failure.

.. _`netlbl_secattr_free`:

netlbl_secattr_free
===================

.. c:function:: void netlbl_secattr_free(struct netlbl_lsm_secattr *secattr)

    Frees a netlbl_lsm_secattr struct

    :param struct netlbl_lsm_secattr \*secattr:
        the struct to free

.. _`netlbl_secattr_free.description`:

Description
-----------

Frees \ ``secattr``\  including all of the internal buffers.

.. This file was automatic generated / don't edit.
